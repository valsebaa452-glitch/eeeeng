"""Local, read-only arithmetic for public or synthetic business scenarios."""

from decimal import DecimalException
import json
from pathlib import Path
import sys

import anyio
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp.types import CallToolResult, TextContent, Tool, ToolAnnotations

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))
import business_math
from research_math import (
    CASH_LIMIT, CASH_MINIMUMS, COUNT_LIMIT, SPEND_LIMIT,
    acquisition_cash_bridge, bounded_decimal, bounded_integer, market_size, require_fields,
)


def object_schema(properties):
    return {"type": "object", "properties": properties, "required": list(properties),
            "additionalProperties": False}


COUNT = {"type": "integer", "minimum": 0, "maximum": COUNT_LIMIT}
AMOUNT = {"type": "number", "minimum": 0, "maximum": SPEND_LIMIT}
RATE = {"type": "number", "minimum": 0, "maximum": 1}
HOURS = {"type": "number", "minimum": 0, "maximum": 1_000_000}
NAME = {"type": "string", "minLength": 1, "maxLength": 120, "pattern": r"\S"}
PERIOD = {"type": "integer", "minimum": 1, "maximum": 120}
CURRENCY = {
    "type": "string", "minLength": 3, "maxLength": 3, "pattern": "^[A-Z]{3}$",
    "description": "Three uppercase ASCII letters; this does not validate ISO membership.",
}
MONTHLY_PROPERTIES = {
    "name": NAME,
    "clients": {**COUNT, "minimum": 1},
    "new_clients": COUNT,
    "price": AMOUNT,
    "refund_rate": RATE,
    "payment_fee_rate": RATE,
    "technology_per_client": AMOUNT,
    "delivery_hours_per_client": HOURS,
    "hourly_labor_cost": AMOUNT,
    "onboarding_hours_per_new_client": HOURS,
    "sales_hours": HOURS,
    "admin_hours": HOURS,
    "fixed_costs": {"type": "number", "minimum": 0, "maximum": CASH_LIMIT},
}
ROW_PROPERTIES = {
    "cohort": NAME,
    "period": {"type": "integer", "minimum": 0, "maximum": 120},
    "eligible": COUNT,
    "retained": {**COUNT, "type": ["integer", "null"]},
}
INPUT_SCHEMAS = {
    "monthly_economics": object_schema({"scenario": object_schema(MONTHLY_PROPERTIES)}),
    "cohort_retention": object_schema({"rows": {
        "type": "array", "minItems": 0, "maxItems": 128, "items": object_schema(ROW_PROPERTIES),
    }}),
    "market_size": object_schema({"scenario": object_schema({
        "currency": CURRENCY, "period_months": PERIOD, "buyers": COUNT,
        "serviceable_buyers": COUNT, "reachable_buyers": COUNT, "customer_capacity": COUNT,
        "spend_per_buyer": AMOUNT, "win_rate": RATE,
    })}),
    "acquisition_cash_bridge": object_schema({"scenario": object_schema({
        "currency": CURRENCY, "period_months": PERIOD,
        **{field: {"type": "number", "minimum": minimum, "maximum": CASH_LIMIT}
           for field, minimum in CASH_MINIMUMS.items()},
    })}),
}
DESCRIPTIONS = {
    "monthly_economics": (
        "Public/synthetic one-month economics, reusing the project's calculator. "
        "Uses active clients and one consistent currency; result is before tax, not guaranteed earnings."
    ),
    "cohort_retention": (
        "Descriptive, denominator-weighted retention from at most 128 public/synthetic rows. "
        "Relative periods are integers 0–120. Null retained means unobserved, not zero retention."
    ),
    "market_size": (
        "Public/synthetic TAM, SAM and conditional SOM for a stated period; not a revenue forecast. "
        "Requires reachable <= serviceable <= buyers. Apply win_rate before the capacity ceiling."
    ),
    "acquisition_cash_bridge": (
        "Public/synthetic EBITDA normalization and cash after listed costs for one currency/period. "
        "Owner adjustment is the net wage gap. Not a valuation, audit or cash guarantee; "
        "subtract maintenance capex once, not depreciation again."
    ),
}
TOOLS = [
    Tool(name=name, description=DESCRIPTIONS[name], inputSchema=schema,
         annotations=ToolAnnotations(readOnlyHint=True, destructiveHint=False,
                                     idempotentHint=True, openWorldHint=False))
    for name, schema in INPUT_SCHEMAS.items()
]
server = Server(
    "business-math", version="0.1.0",
    instructions=("Use only public or synthetic inputs. All arithmetic is local; no network, "
                  "user-selected files, commands, credentials or telemetry are used."),
)


def _name(value, field):
    if type(value) is not str or not 1 <= len(value) <= 120 or not value.strip():
        raise ValueError(f"{field} must be nonblank text of at most 120 characters")


def calculate(name, arguments):
    if type(name) is not str or name not in INPUT_SCHEMAS:
        raise ValueError("Unknown business-math tool")
    require_fields(arguments, ("rows",) if name == "cohort_retention" else ("scenario",), "arguments")
    if name == "cohort_retention":
        rows = arguments["rows"]
        if type(rows) is not list or len(rows) > 128:
            raise ValueError("rows must be an array of at most 128 entries")
        for row in rows:
            require_fields(row, ROW_PROPERTIES, "row")
            _name(row["cohort"], "cohort")
            bounded_integer(row["period"], "period", 0, 120)
            bounded_integer(row["eligible"], "eligible")
            if row["retained"] is not None:
                bounded_integer(row["retained"], "retained")
        return business_math.retention_by_period(rows)
    scenario = arguments["scenario"]
    if name == "market_size":
        return market_size(scenario)
    if name == "acquisition_cash_bridge":
        return acquisition_cash_bridge(scenario)
    require_fields(scenario, MONTHLY_PROPERTIES)
    _name(scenario["name"], "name")
    for field, definition in MONTHLY_PROPERTIES.items():
        if definition["type"] == "integer":
            bounded_integer(scenario[field], field, definition["minimum"], definition["maximum"])
        elif definition["type"] == "number":
            bounded_decimal(scenario[field], field, definition["minimum"], definition["maximum"])
    return business_math.monthly_economics(scenario)


def _result(payload, error=False):
    return CallToolResult(
        content=[TextContent(type="text", text=json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False))],
        structuredContent=payload, isError=error,
    )


@server.list_tools()
async def list_tools():
    return TOOLS


# Validate explicitly so schema errors cannot echo entire submitted objects.
@server.call_tool(validate_input=False)
async def call_tool(name, arguments):
    try:
        return _result(calculate(name, arguments))
    except ValueError as exc:
        return _result({"error": str(exc)}, error=True)
    except (DecimalException, OverflowError):
        return _result({"error": "Calculation exceeds supported numeric precision"}, error=True)


async def main():
    async with stdio_server() as (incoming, outgoing):
        await server.run(incoming, outgoing, server.create_initialization_options())


if __name__ == "__main__":
    anyio.run(main)
