"""Bounded scenario arithmetic; monetary outputs use decimal half-up rounding."""

from decimal import Context, Decimal, ROUND_HALF_UP, localcontext
import math
import re

COUNT_LIMIT = 100_000_000
SPEND_LIMIT = 1_000_000_000
CASH_LIMIT = 1_000_000_000_000
MARKET_FIELDS = (
    "currency", "period_months", "buyers", "serviceable_buyers", "reachable_buyers",
    "customer_capacity", "spend_per_buyer", "win_rate",
)
CASH_MINIMUMS = {
    "reported_ebitda": -CASH_LIMIT,
    "nonrecurring_income": 0,
    "verified_oneoff_expenses": 0,
    "owner_salary_adjustment": -CASH_LIMIT,
    "maintenance_capex": 0,
    "working_capital_change": -CASH_LIMIT,
    "debt_service": 0,
    "cash_taxes": 0,
}
ACQUISITION_FIELDS = ("currency", "period_months", *CASH_MINIMUMS)


def require_fields(value, fields, label="scenario"):
    if type(value) is not dict:
        raise ValueError(f"{label} must be an object")
    if len(value) > len(fields):
        raise ValueError(f"{label} contains unsupported fields")
    for field in fields:
        if field not in value:
            raise ValueError(f"{label}.{field} is required")


def bounded_integer(value, field, minimum=0, maximum=COUNT_LIMIT):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{field} must be an integer from {minimum} to {maximum}")
    return value


def bounded_decimal(value, field, minimum=0, maximum=SPEND_LIMIT):
    if (type(value) not in (int, float)
            or (type(value) is float and not math.isfinite(value))
            or not minimum <= value <= maximum):
        raise ValueError(f"{field} must be a finite number from {minimum} to {maximum}")
    return Decimal(str(value))


def _common(scenario, fields):
    require_fields(scenario, fields)
    currency = scenario["currency"]
    if type(currency) is not str or re.fullmatch(r"[A-Z]{3}", currency) is None:
        raise ValueError("currency must contain exactly three uppercase ASCII letters")
    period = bounded_integer(scenario["period_months"], "period_months", 1, 120)
    return currency, period


def _money(value):
    rounded = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return format(rounded, ".2f") if rounded else "0.00"


def market_size(scenario):
    currency, period = _common(scenario, MARKET_FIELDS)
    counts = {
        field: bounded_integer(scenario[field], field)
        for field in ("buyers", "serviceable_buyers", "reachable_buyers", "customer_capacity")
    }
    if not counts["reachable_buyers"] <= counts["serviceable_buyers"] <= counts["buyers"]:
        raise ValueError("Require reachable_buyers <= serviceable_buyers <= buyers")
    spend = bounded_decimal(scenario["spend_per_buyer"], "spend_per_buyer")
    win_rate = bounded_decimal(scenario["win_rate"], "win_rate", maximum=1)
    with localcontext(Context(prec=64, rounding=ROUND_HALF_UP)):
        customers = min(counts["reachable_buyers"] * win_rate, Decimal(counts["customer_capacity"]))
        return {
            "currency": currency,
            "period_months": period,
            "tam": _money(counts["buyers"] * spend),
            "sam": _money(counts["serviceable_buyers"] * spend),
            "scenario_customers": float(customers),
            "som_scenario": _money(customers * spend),
            "not_a_forecast": True,
            "scope": (
                "Scenario only, not observed demand or guaranteed revenue. Spend per buyer covers "
                "the whole stated period. Capacity limits customers after applying win_rate; "
                "scenario_customers may be fractional. Currency format is checked, not ISO membership."
            ),
        }


def acquisition_cash_bridge(scenario):
    currency, period = _common(scenario, ACQUISITION_FIELDS)
    amounts = {
        field: bounded_decimal(scenario[field], field, minimum, CASH_LIMIT)
        for field, minimum in CASH_MINIMUMS.items()
    }
    with localcontext(Context(prec=64, rounding=ROUND_HALF_UP)):
        normalized = (amounts["reported_ebitda"] - amounts["nonrecurring_income"]
                      + amounts["verified_oneoff_expenses"] - amounts["owner_salary_adjustment"])
        cash = (normalized - amounts["maintenance_capex"] - amounts["working_capital_change"]
                - amounts["debt_service"] - amounts["cash_taxes"])
        return {
            "currency": currency,
            "period_months": period,
            "normalized_ebitda": _money(normalized),
            "cash_after_listed_costs": _money(cash),
            "not_a_forecast": True,
            "scope": (
                "Scenario only; not a valuation, audit, or guarantee of cash. All inputs must cover "
                "the same currency and period; unlisted costs remain excluded. Positive working "
                "capital change uses cash; negative change releases it. Owner salary adjustment "
                "is the net wage gap. EBITDA excludes depreciation and amortization: do not subtract "
                "them again; maintenance capex is subtracted once. Currency format is checked, "
                "not ISO membership."
            ),
        }
