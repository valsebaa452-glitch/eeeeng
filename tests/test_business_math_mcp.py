from contextlib import asynccontextmanager, redirect_stderr
from copy import deepcopy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import anyio
from jsonschema import Draft202012Validator
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "tools/hoplite-research/scripts"
sys.path.insert(0, str(SCRIPTS))
import business_math_mcp as bridge
import run_business_math_mcp as launcher


def fixtures():
    return {
        "monthly_economics": {"scenario": {
            "name": "Synthetic service", "clients": 10, "new_clients": 2, "price": 100,
            "refund_rate": 0.05, "payment_fee_rate": 0.03, "technology_per_client": 10,
            "delivery_hours_per_client": 1, "hourly_labor_cost": 20,
            "onboarding_hours_per_new_client": 2, "sales_hours": 3, "admin_hours": 2,
            "fixed_costs": 50,
        }},
        "cohort_retention": {"rows": [
            {"cohort": "Synthetic A", "period": 1, "eligible": 10, "retained": 8},
            {"cohort": "Synthetic B", "period": 1, "eligible": 5, "retained": 1},
            {"cohort": "Unobserved", "period": 2, "eligible": 5, "retained": None},
        ]},
        "market_size": {"scenario": {
            "currency": "USD", "period_months": 12, "buyers": 1000, "serviceable_buyers": 400,
            "reachable_buyers": 100, "customer_capacity": 10, "spend_per_buyer": 120, "win_rate": 0.25,
        }},
        "acquisition_cash_bridge": {"scenario": {
            "currency": "USD", "period_months": 12, "reported_ebitda": 100000,
            "nonrecurring_income": 20000, "verified_oneoff_expenses": 5000,
            "owner_salary_adjustment": 10000, "maintenance_capex": 15000,
            "working_capital_change": 10000, "debt_service": 12000, "cash_taxes": 8000,
        }},
    }


def invalid_calls():
    calls = [("not_a_tool", {}), ("monthly_economics", {}),
             ("monthly_economics", {"scenario": None}),
             ("cohort_retention", {"rows": "not an array"}),
             ("cohort_retention", {"rows": [fixtures()["cohort_retention"]["rows"][0]] * 129})]
    for name, arguments in fixtures().items():
        calls.append((name, {**arguments, "path": "/not/read"}))
    for field, value in [("clients", 0), ("clients", True), ("clients", 1.0),
                         ("clients", 100_000_001), ("new_clients", 11), ("price", -1),
                         ("price", "NaN"), ("price", "Infinity"), ("price", True),
                         ("name", " "), ("name", "x" * 121), ("sales_hours", 1_000_001),
                         ("refund_rate", 0.98)]:
        args = fixtures()["monthly_economics"]
        args["scenario"][field] = value
        calls.append(("monthly_economics", args))
    for field, value in [("cohort", "x" * 121), ("period", True), ("period", 121),
                         ("eligible", -1), ("retained", 11), ("retained", False)]:
        row = {**fixtures()["cohort_retention"]["rows"][0], field: value}
        calls.append(("cohort_retention", {"rows": [row]}))
    row = fixtures()["cohort_retention"]["rows"][0]
    calls.extend([("cohort_retention", {"rows": [row, row]}),
                  ("cohort_retention", {"rows": [{**row, "file": "/not/read"}]}),
                  ("cohort_retention", {"rows": [{"cohort": "Missing fields"}]})])
    for name, field, value in [("market_size", "reachable_buyers", 401),
                               ("market_size", "win_rate", True),
                               ("market_size", "period_months", 0),
                               ("acquisition_cash_bridge", "currency", "usd"),
                               ("acquisition_cash_bridge", "maintenance_capex", -1)]:
        args = fixtures()[name]
        args["scenario"][field] = value
        calls.append((name, args))
    return calls


def payload(test, response):
    test.assertEqual(len(response.content), 1)
    text = response.content[0].text
    test.assertIn("\n", text)
    value = json.loads(text)
    test.assertEqual(value, response.structuredContent)
    json.dumps(value, allow_nan=False)
    return value


@asynccontextmanager
async def local_session():
    parameters = StdioServerParameters(command="python3", args=[str(SCRIPTS / "run_business_math_mcp.py")])
    with anyio.fail_after(30):
        async with stdio_client(parameters) as (reader, writer):
            async with ClientSession(reader, writer) as client:
                initialized = await client.initialize()
                yield client, initialized


class AdapterTests(unittest.IsolatedAsyncioTestCase):
    async def test_existing_functions_are_reused_without_mutating_inputs(self):
        for tool, function, key in [("monthly_economics", "monthly_economics", "scenario"),
                                    ("cohort_retention", "retention_by_period", "rows")]:
            arguments = fixtures()[tool]
            original = deepcopy(arguments)
            implementation = getattr(bridge.business_math, function)
            with patch.object(bridge.business_math, function, wraps=implementation) as calculate:
                response = await bridge.call_tool(tool, arguments)
            self.assertFalse(response.isError)
            self.assertEqual(payload(self, response), implementation(arguments[key]))
            calculate.assert_called_once_with(arguments[key])
            self.assertEqual(arguments, original)

    async def test_nonfinite_numbers_are_rejected_for_all_numeric_inputs(self):
        for tool, arguments in fixtures().items():
            if tool == "cohort_retention":
                properties = bridge.ROW_PROPERTIES
            else:
                properties = bridge.INPUT_SCHEMAS[tool]["properties"]["scenario"]["properties"]
            for field, definition in properties.items():
                if definition["type"] == "string":
                    continue
                for value in [float("nan"), float("inf"), -float("inf")]:
                    args = deepcopy(arguments)
                    target = args["rows"][0] if tool == "cohort_retention" else args["scenario"]
                    target[field] = value
                    with self.subTest(tool=tool, field=field):
                        response = await bridge.call_tool(tool, args)
                        self.assertTrue(response.isError)
                        self.assertIn("error", payload(self, response))

    async def test_errors_do_not_echo_large_values_or_unknown_keys(self):
        for tool, arguments in fixtures().items():
            args = deepcopy(arguments)
            target = args["rows"][0] if tool == "cohort_retention" else args["scenario"]
            target["untrusted_" + "x" * 100_000] = "y" * 100_000
            response = await bridge.call_tool(tool, args)
            self.assertTrue(response.isError)
            self.assertLess(len(response.content[0].text), 300)
            self.assertNotIn("untrusted_", response.content[0].text)
        args = fixtures()["monthly_economics"]
        args["scenario"]["name"] = "x" * 100_000
        response = await bridge.call_tool("monthly_economics", args)
        self.assertTrue(response.isError)
        self.assertLess(len(response.content[0].text), 300)

    async def test_calculations_do_not_open_files_network_or_processes(self):
        with (patch("builtins.open", side_effect=AssertionError("Unexpected file read")),
              patch("pathlib.Path.open", side_effect=AssertionError("Unexpected path read")),
              patch("socket.getaddrinfo", side_effect=AssertionError("Unexpected DNS")),
              patch("socket.socket.connect", side_effect=AssertionError("Unexpected network")),
              patch("subprocess.Popen", side_effect=AssertionError("Unexpected subprocess")),
              patch("os.system", side_effect=AssertionError("Unexpected shell"))):
            for tool, arguments in fixtures().items():
                response = await bridge.call_tool(tool, arguments)
                self.assertFalse(response.isError)
                payload(self, response)


class StdioTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_stdio_catalog_and_four_successful_calculations(self):
        async with local_session() as (client, initialized):
            self.assertEqual(initialized.serverInfo.name, "business-math")
            self.assertIsNone(initialized.capabilities.resources)
            self.assertIsNone(initialized.capabilities.prompts)
            tools = (await client.list_tools()).tools
            self.assertEqual({tool.name for tool in tools}, set(fixtures()))
            self.assertEqual(len(tools), 4)
            for tool in tools:
                Draft202012Validator.check_schema(tool.inputSchema)
                Draft202012Validator(tool.inputSchema).validate(fixtures()[tool.name])
                self.assertFalse(tool.inputSchema["additionalProperties"])
                nested = tool.inputSchema["properties"].get("scenario")
                if nested is None:
                    rows = tool.inputSchema["properties"]["rows"]
                    self.assertEqual(rows["maxItems"], 128)
                    nested = rows["items"]
                self.assertFalse(nested["additionalProperties"])
                self.assertEqual(set(nested["required"]), set(nested["properties"]))
                for definition in nested["properties"].values():
                    if definition["type"] == "string":
                        self.assertLessEqual(definition["maxLength"], 120)
                    else:
                        self.assertIn("minimum", definition)
                        self.assertIn("maximum", definition)
                self.assertTrue(tool.annotations.readOnlyHint)
                self.assertFalse(tool.annotations.openWorldHint)
            results = {}
            for tool, arguments in fixtures().items():
                response = await client.call_tool(tool, arguments)
                self.assertFalse(response.isError)
                results[tool] = payload(self, response)
            self.assertEqual(results["monthly_economics"]["operating_result_before_tax"], 390)
            self.assertEqual(results["cohort_retention"]["periods"][0]["retention"], 0.6)
            self.assertIsNone(results["cohort_retention"]["periods"][1]["retention"])
            self.assertEqual(results["market_size"]["som_scenario"], "1200.00")
            self.assertEqual(results["market_size"]["scenario_customers"], 10)
            self.assertEqual(results["acquisition_cash_bridge"]["cash_after_listed_costs"], "30000.00")

    async def test_real_stdio_errors_and_recovery(self):
        async with local_session() as (client, _):
            for tool, arguments in invalid_calls():
                with self.subTest(tool=tool):
                    response = await client.call_tool(tool, arguments)
                    self.assertTrue(response.isError)
                    self.assertIn("error", payload(self, response))
                    self.assertLess(len(response.content[0].text), 300)
            response = await client.call_tool("market_size", fixtures()["market_size"])
            self.assertFalse(response.isError)
            self.assertEqual(payload(self, response)["som_scenario"], "1200.00")

    async def test_real_stdio_empty_unobserved_and_maximum_cohorts(self):
        async with local_session() as (client, _):
            empty = payload(self, await client.call_tool("cohort_retention", {"rows": []}))
            self.assertEqual(empty, {"rows": [], "periods": []})
            rows = [{"cohort": f"Synthetic {i}", "period": 120, "eligible": 100_000_000,
                     "retained": None if i % 2 else 50_000_000} for i in range(128)]
            result = payload(self, await client.call_tool("cohort_retention", {"rows": rows}))
            self.assertEqual(len(result["rows"]), 128)
            self.assertEqual(result["periods"][0]["eligible_observed"], 6_400_000_000)
            self.assertEqual(result["periods"][0]["retention"], 0.5)


class LauncherTests(unittest.TestCase):
    def test_fixed_venv_command_and_isolated_environment(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            python = root / ".venv/bin/python"
            python.parent.mkdir(parents=True)
            python.touch()
            with (patch.object(launcher, "ROOT", root), patch.object(sys, "argv", ["launcher"]),
                  patch("run_business_math_mcp.os.chdir") as chdir,
                  patch("run_business_math_mcp.os.execve") as execute,
                  patch.dict("os.environ", {"OPENAI_API_KEY": "synthetic", "HTTP_PROXY": "synthetic",
                                            "PYTHONPATH": "synthetic"}, clear=True),
                  patch.object(launcher, "isolated_environment", wraps=lambda: bridge_environment(root))):
                launcher.main()
            chdir.assert_called_once_with(root)
            program, arguments, environment = execute.call_args.args
            self.assertEqual(program, python)
            self.assertEqual(arguments, [str(python), "-B", str(root / "scripts/business_math_mcp.py")])
            self.assertEqual(environment["HOME"], str(root / ".research/home"))
            self.assertEqual(set(environment), {"HOME", "PATH", "LANG", "PYTHONUNBUFFERED",
                                                "PYTHONUTF8", "REQUEST_TIMEOUT", "MAX_RESULTS"})

    def test_missing_venv_fails_without_exec(self):
        with tempfile.TemporaryDirectory() as folder:
            with (patch.object(launcher, "ROOT", Path(folder)), patch.object(sys, "argv", ["launcher"]),
                  patch("run_business_math_mcp.os.execve") as execute, redirect_stderr(io.StringIO()) as errors):
                with self.assertRaises(SystemExit) as failure:
                    launcher.main()
                self.assertEqual(failure.exception.code, 2)
                self.assertIn("Dependencies are not installed", errors.getvalue())
                execute.assert_not_called()


def bridge_environment(root):
    from mcp_runtime import isolated_environment
    return isolated_environment(root)


if __name__ == "__main__":
    unittest.main()
