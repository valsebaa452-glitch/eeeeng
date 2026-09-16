from copy import deepcopy
from decimal import localcontext
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from research_math import acquisition_cash_bridge, market_size


def market(**changes):
    return {"currency": "USD", "period_months": 12, "buyers": 1000,
            "serviceable_buyers": 400, "reachable_buyers": 100, "customer_capacity": 50,
            "spend_per_buyer": 120, "win_rate": 0.25, **changes}


def acquisition(**changes):
    return {"currency": "USD", "period_months": 12, "reported_ebitda": 100000,
            "nonrecurring_income": 20000, "verified_oneoff_expenses": 5000,
            "owner_salary_adjustment": 10000, "maintenance_capex": 15000,
            "working_capital_change": 10000, "debt_service": 12000, "cash_taxes": 8000,
            **changes}


class MarketSizeTests(unittest.TestCase):
    def test_market_amounts_and_scope(self):
        result = market_size(market())
        self.assertEqual((result["tam"], result["sam"], result["som_scenario"]),
                         ("120000.00", "48000.00", "3000.00"))
        self.assertEqual(result["scenario_customers"], 25)
        self.assertEqual((result["currency"], result["period_months"]), ("USD", 12))
        self.assertIs(result["not_a_forecast"], True)

    def test_capacity_is_applied_after_win_rate(self):
        for capacity, expected in [(50, 25), (10, 10), (0, 0)]:
            with self.subTest(capacity=capacity):
                result = market_size(market(customer_capacity=capacity))
                self.assertEqual(result["scenario_customers"], expected)
                self.assertEqual(result["som_scenario"], f"{expected * 120:.2f}")

    def test_zero_market_spend_and_win_rate(self):
        scenarios = [market(buyers=0, serviceable_buyers=0, reachable_buyers=0),
                     market(spend_per_buyer=0), market(win_rate=0)]
        for scenario in scenarios:
            with self.subTest(scenario=scenario):
                self.assertEqual(market_size(scenario)["som_scenario"], "0.00")

    def test_fractional_customers_and_half_up_rounding(self):
        result = market_size(market(reachable_buyers=3, win_rate=0.5, spend_per_buyer=0.01))
        self.assertEqual(result["scenario_customers"], 1.5)
        self.assertEqual(result["som_scenario"], "0.02")

    def test_period_does_not_multiply_period_spend(self):
        self.assertEqual(market_size(market(period_months=1))["tam"],
                         market_size(market(period_months=120))["tam"])

    def test_upper_bounds_and_currency_format_not_iso_membership(self):
        result = market_size(market(currency="ZZZ", period_months=120, buyers=100_000_000,
                                    serviceable_buyers=100_000_000, reachable_buyers=100_000_000,
                                    customer_capacity=100_000_000, spend_per_buyer=1_000_000_000,
                                    win_rate=1))
        self.assertEqual(result["som_scenario"], "100000000000000000.00")
        json.dumps(result, allow_nan=False)

    def test_invalid_market_chain(self):
        for changes in [{"serviceable_buyers": 1001}, {"reachable_buyers": 401},
                        {"buyers": 0}, {"serviceable_buyers": 0}]:
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "reachable_buyers <="):
                market_size(market(**changes))

    def test_integer_counts_are_strict_and_bounded(self):
        for field in ["buyers", "serviceable_buyers", "reachable_buyers", "customer_capacity"]:
            for value in [True, False, 1.0, "1", None, -1, 100_000_001, 10 ** 5000]:
                with self.subTest(field=field, kind=type(value).__name__), self.assertRaises(ValueError):
                    market_size(market(**{field: value}))

    def test_rates_and_spend_reject_non_numeric_nonfinite_and_out_of_range(self):
        for field in ["spend_per_buyer", "win_rate"]:
            for value in [True, False, None, "0.1", [], {}, float("nan"), float("inf"),
                          -float("inf"), -0.1, 1_000_000_001, 10 ** 5000]:
                with self.subTest(field=field, kind=type(value).__name__), self.assertRaises(ValueError):
                    market_size(market(**{field: value}))
        with self.assertRaises(ValueError):
            market_size(market(win_rate=1.01))


class AcquisitionBridgeTests(unittest.TestCase):
    def test_normalization_cash_and_scope(self):
        result = acquisition_cash_bridge(acquisition())
        self.assertEqual(result["normalized_ebitda"], "75000.00")
        self.assertEqual(result["cash_after_listed_costs"], "30000.00")
        self.assertEqual((result["currency"], result["period_months"]), ("USD", 12))
        self.assertIs(result["not_a_forecast"], True)
        for term in ["not a valuation", "audit", "net wage gap", "depreciation", "subtracted once"]:
            self.assertIn(term, result["scope"])

    def test_signed_owner_gap_and_working_capital_release(self):
        self.assertEqual(acquisition_cash_bridge(acquisition(owner_salary_adjustment=-10000))
                         ["normalized_ebitda"], "95000.00")
        self.assertEqual(acquisition_cash_bridge(acquisition(working_capital_change=-10000))
                         ["cash_after_listed_costs"], "50000.00")

    def test_zero_loss_and_capex_subtracted_once(self):
        empty = {field: 0 for field in acquisition() if field not in {"currency", "period_months"}}
        for ebitda, capex, expected in [(0, 0, "0.00"), (-100, 0, "-100.00"),
                                      (100, 20, "80.00"), (-0.004, 0, "0.00")]:
            with self.subTest(ebitda=ebitda, capex=capex):
                result = acquisition_cash_bridge(acquisition(**{**empty, "reported_ebitda": ebitda,
                                                                 "maintenance_capex": capex}))
                self.assertEqual(result["cash_after_listed_costs"], expected)

    def test_signed_limits_and_two_decimal_output(self):
        result = acquisition_cash_bridge(acquisition(
            reported_ebitda=-1e12, nonrecurring_income=1e12, verified_oneoff_expenses=0,
            owner_salary_adjustment=1e12, maintenance_capex=1e12, working_capital_change=1e12,
            debt_service=1e12, cash_taxes=1e12,
        ))
        self.assertEqual(result["cash_after_listed_costs"], "-7000000000000.00")
        for field in ["normalized_ebitda", "cash_after_listed_costs"]:
            self.assertRegex(result[field], r"^-?\d+\.\d{2}$")
        json.dumps(result, allow_nan=False)

    def test_every_amount_rejects_bools_missing_nonfinite_and_excessive_values(self):
        for field in acquisition():
            if field in {"currency", "period_months"}:
                continue
            for value in [True, False, None, "0", [], {}, float("nan"), float("inf"),
                          -float("inf"), 1e12 + 1, -1e12 - 1, 10 ** 5000]:
                with self.subTest(field=field, kind=type(value).__name__), self.assertRaises(ValueError):
                    acquisition_cash_bridge(acquisition(**{field: value}))

    def test_only_signed_fields_accept_negative_values(self):
        for field in ["nonrecurring_income", "verified_oneoff_expenses", "maintenance_capex",
                      "debt_service", "cash_taxes"]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                acquisition_cash_bridge(acquisition(**{field: -1}))


class SharedValidationTests(unittest.TestCase):
    def test_closed_required_scenarios(self):
        for calculate, fixture in [(market_size, market), (acquisition_cash_bridge, acquisition)]:
            for field in fixture():
                scenario = fixture()
                del scenario[field]
                with self.subTest(function=calculate.__name__, field=field), self.assertRaisesRegex(ValueError, "required"):
                    calculate(scenario)
            for bad in [None, [], "scenario", True, {**fixture(), "file": "/not/read"}]:
                with self.subTest(function=calculate.__name__), self.assertRaises(ValueError):
                    calculate(bad)

    def test_currency_and_period(self):
        for calculate, fixture in [(market_size, market), (acquisition_cash_bridge, acquisition)]:
            for currency in ["", "usd", "US", "USDD", "1US", "USD\n", "ＵＳＤ", 1, True, None]:
                with self.subTest(currency=currency), self.assertRaises(ValueError):
                    calculate(fixture(currency=currency))
            for period in [0, 121, True, False, 1.0, "12", None, float("nan"), float("inf")]:
                with self.subTest(period=period), self.assertRaises(ValueError):
                    calculate(fixture(period_months=period))

    def test_no_mutation_and_caller_decimal_context_does_not_change_money(self):
        for calculate, fixture in [(market_size, market), (acquisition_cash_bridge, acquisition)]:
            scenario = fixture()
            original = deepcopy(scenario)
            expected = calculate(scenario)
            with localcontext() as context:
                context.prec = 3
                self.assertEqual(calculate(scenario), expected)
            self.assertEqual(scenario, original)

    def test_small_finite_numbers_and_negative_zero_do_not_leak_nonfinite_output(self):
        for value in [5e-324, -0.0]:
            result = market_size(market(spend_per_buyer=value))
            self.assertEqual(result["som_scenario"], "0.00")
            json.dumps(result, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
