import os
import sys
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(ROOT, "ai-readiness"))
import scorer  # noqa: E402


def row(**kw):
    base = dict(volume=5, rule_clarity=5, data_availability=5, exception_rate=1, error_cost=1, judgment_risk=1)
    base.update(kw)
    return base


class ScorerTests(unittest.TestCase):
    def test_ideal_step_automates(self):
        self.assertEqual(scorer.recommend(row())[1], "AUTOMATE")

    def test_max_judgment_risk_is_always_human_led(self):
        self.assertEqual(scorer.recommend(row(judgment_risk=5))[1], "HUMAN-LED")

    def test_risk_four_caps_at_augment(self):
        self.assertEqual(scorer.recommend(row(judgment_risk=4))[1], "AUGMENT")

    def test_potential_bounds(self):
        self.assertEqual(scorer.potential(row()), 100)
        self.assertEqual(scorer.potential(row(volume=1, rule_clarity=1, data_availability=1,
                                              exception_rate=5, error_cost=5)), 0)

    def test_sample_file_scores(self):
        rows = scorer.score_file(os.path.join(ROOT, "ai-readiness", "sample_steps.csv"))
        self.assertEqual(len(rows), 16)
        recs = dict((r["step"], r["recommendation"]) for r in rows)
        self.assertEqual(recs["Judgmental accruals and provisions"], "HUMAN-LED")
        self.assertEqual(recs["Cash application and remittance matching"], "AUTOMATE")


if __name__ == "__main__":
    unittest.main()
