#!/usr/bin/env python3
"""@reimagine v0.1 — grader tests.

Run exactly (from reimagine_v0.1/):  python3 evals/test_grader.py
Also works via:                      python3 -m unittest evals.test_grader
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grader  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
WITH_SKILL = os.path.join(HERE, "examples", "vector2_with_skill.md")
BASELINE = os.path.join(HERE, "examples", "vector2_baseline.md")


def _read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def _grade_text(text):
    """Write text to a temp worksheet and grade it."""
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "worksheet.md")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        return grader.grade(path)


class ReimagineGraderTests(unittest.TestCase):

    def test_with_skill_example_passes(self):
        passed, results = grader.grade(WITH_SKILL)
        self.assertTrue(
            passed,
            "with-skill exemplar should PASS:\n"
            + "\n".join("%s %s — %s" % (c, "PASS" if ok else "FAIL", d)
                        for c, ok, d in results if not ok))

    def test_baseline_fails_expected_checks(self):
        passed, results = grader.grade(BASELINE)
        self.assertFalse(passed, "no-skill baseline should FAIL")
        failed = {code for code, ok, _ in results if not ok}
        self.assertTrue(
            {"C2", "C4", "C6"} <= failed,
            "baseline must fail explicitness, QA decidability and disclosure; "
            "failed=%s" % sorted(failed))

    def test_forbidden_phrase_fails_law(self):
        text = _read(WITH_SKILL).replace(
            "warm timber rainscreen palette",
            "warm timber rainscreen palette and remove the watermark")
        passed, results = _grade_text(text)
        self.assertFalse(passed)
        failed = {code for code, ok, _ in results if not ok}
        self.assertIn("C3", failed, "watermark-removal language must fail C3")

    def test_bad_card_id_fails_traceability(self):
        text = _read(WITH_SKILL).replace("CARD: A02", "CARD: the facade one")
        passed, results = _grade_text(text)
        self.assertFalse(passed)
        failed = {code for code, ok, _ in results if not ok}
        self.assertIn("C5", failed, "non-atlas card ID must fail C5")


if __name__ == "__main__":
    unittest.main()
