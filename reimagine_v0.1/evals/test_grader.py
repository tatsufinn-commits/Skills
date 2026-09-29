#!/usr/bin/env python3
"""@reimagine v0.1.1 — grader regression tests.

Run (from reimagine_v0.1/): python3 -W error::ResourceWarning evals/test_grader.py
Also works via: python3 -m unittest evals.test_grader
"""

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grader  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
WITH_SKILL = os.path.join(HERE, "examples", "vector2_with_skill.md")
BASELINE = os.path.join(HERE, "examples", "vector2_baseline.md")
PACKAGE = os.path.dirname(HERE)


def _read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def _grade_text(text):
    """Write text to a temporary worksheet and grade it."""
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "worksheet.md")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        return grader.grade(path)


def _result(results, code):
    return next((ok, detail) for found, ok, detail in results if found == code)


def _replace(text, old, new):
    if old not in text:
        raise AssertionError("fixture text not found: %r" % old)
    return text.replace(old, new, 1)


class ReimagineGraderTests(unittest.TestCase):

    def test_with_skill_example_passes(self):
        passed, results = grader.grade(WITH_SKILL)
        self.assertTrue(
            passed,
            "with-skill exemplar should PASS:\n"
            + "\n".join("%s %s — %s" % (c, "PASS" if ok else "FAIL", d)
                        for c, ok, d in results if not ok))
        self.assertEqual(len(results), 7)

    def test_baseline_fails_expected_checks(self):
        passed, results = grader.grade(BASELINE)
        self.assertFalse(passed, "no-skill baseline should FAIL")
        failed = {code for code, ok, _ in results if not ok}
        self.assertTrue({"C2", "C4", "C6"} <= failed, "failed=%s" % sorted(failed))

    def test_forbidden_phrase_fails_law(self):
        text = _replace(_read(WITH_SKILL), "warm timber rainscreen palette",
                        "warm timber palette and delete the watermark")
        passed, results = _grade_text(text)
        self.assertFalse(passed)
        self.assertFalse(_result(results, "C3")[0])

    def test_each_cmi_verb_and_mark_combination_is_blocked(self):
        for phrase in ("delete the watermark", "obscure logo", "erase attribution",
                       "strip CMI", "clean the credit", "remove watermark"):
            with self.subTest(phrase=phrase):
                text = _replace(_read(WITH_SKILL), "warm timber rainscreen palette",
                                "warm timber palette; " + phrase)
                self.assertFalse(_result(_grade_text(text)[1], "C3")[0])

    def test_bad_card_id_fails_traceability(self):
        text = _replace(_read(WITH_SKILL), "CARD: A02", "CARD: the facade one")
        self.assertFalse(_result(_grade_text(text)[1], "C5")[0])

    def test_only_enumerated_atlas_card_ids_pass(self):
        for card in ("A01", "A12", "P01", "P10", "D01", "D10", "T01", "T02"):
            with self.subTest(card=card):
                text = _replace(_read(WITH_SKILL), "CARD: A02", "CARD: " + card)
                self.assertTrue(_result(_grade_text(text)[1], "C5")[0])
        for card in ("A00", "A13", "P11", "D99", "T03", "X01"):
            with self.subTest(card=card):
                text = _replace(_read(WITH_SKILL), "CARD: A02", "CARD: " + card)
                self.assertFalse(_result(_grade_text(text)[1], "C5")[0])

    def test_rationale_must_be_substantive_not_repeated(self):
        original = _read(WITH_SKILL)
        rationale_line = next(line for line in original.splitlines()
                              if line.startswith("RATIONALE: "))
        for rationale in ("x" * 30, "reason reason reason reason", "short"):
            with self.subTest(rationale=rationale):
                text = _replace(original, rationale_line, "RATIONALE: " + rationale)
                self.assertFalse(_result(_grade_text(text)[1], "C5")[0])
        text = _replace(original, rationale_line,
                        "RATIONALE: Card A02 because this is a bounded facade finish study.")
        self.assertTrue(_result(_grade_text(text)[1], "C5")[0])

    def test_photo_yes_accepts_only_own_licensed_or_cleared(self):
        original = _read(WITH_SKILL)
        for source in ("own", "licensed", "cleared"):
            with self.subTest(source=source):
                text = _replace(original, "PHOTO_SOURCE: own", "PHOTO_SOURCE: " + source)
                self.assertTrue(_result(_grade_text(text)[1], "C3")[0])
        for source in ("none", "internet-untraced", "unknown", "other", ""):
            with self.subTest(source=source):
                text = _replace(original, "PHOTO_SOURCE: own", "PHOTO_SOURCE: " + source)
                passed, results = _grade_text(text)
                ok, detail = _result(results, "C3")
                self.assertFalse(passed)
                self.assertFalse(ok)
                self.assertIn("Gate 0 — rights unresolved; do not emit.", detail)

    def test_photo_no_allows_none_rights_status(self):
        text = _read(WITH_SKILL)
        text = _replace(text, "PHOTO: yes", "PHOTO: no")
        text = _replace(text, "PHOTO_SOURCE: own", "PHOTO_SOURCE: none")
        text = _replace(text,
                        "- East elevation view at eye level — same camera and framing as the dated render (projection invariant)",
                        "- N/A — text-only brief; fidelity claims dropped")
        text = _replace(text,
                        "- Cladding mood across the selected facade zone: warm timber rainscreen palette (finish study only — not a specification)",
                        "- N/A")
        results = _grade_text(text)[1]
        self.assertTrue(_result(results, "C3")[0])
        self.assertTrue(_result(results, "C2")[0])

    def test_photo_no_requires_literal_documented_na_items(self):
        text = _read(WITH_SKILL)
        text = _replace(text, "PHOTO: yes", "PHOTO: no")
        text = _replace(text, "PHOTO_SOURCE: own", "PHOTO_SOURCE: none")
        text = _replace(text,
                        "- East elevation view at eye level — same camera and framing as the dated render (projection invariant)",
                        "- N/A — text-only brief; fidelity claims dropped")
        text = _replace(text,
                        "- Cladding mood across the selected facade zone: warm timber rainscreen palette (finish study only — not a specification)",
                        "- N/A")
        self.assertTrue(_result(_grade_text(text)[1], "C2")[0])
        bad_preserve = _replace(text, "N/A — text-only brief; fidelity claims dropped",
                                "N/A — fidelity claims dropped")
        self.assertFalse(_result(_grade_text(bad_preserve)[1], "C2")[0])
        bad_alter = _replace(text, "- N/A\n", "- nothing to alter\n")
        self.assertFalse(_result(_grade_text(bad_alter)[1], "C2")[0])
        ok, detail = _result(_grade_text(bad_alter)[1], "C2")
        self.assertFalse(ok)
        self.assertIn("alter list must contain an N/A item", detail)
        self.assertNotIn("fidelity claims dropped", detail)

    def test_placeholders_are_checked_in_each_section_and_keys(self):
        original = _read(WITH_SKILL)
        mutations = (
            ("## Paste text\n", "## Paste text\nTODO draft\n"),
            ("## Preserve list\n", "## Preserve list\n- TODO confirm this\n"),
            ("## Alter list\n", "## Alter list\n- TBD finish\n"),
            ("## QA gate\n", "## QA gate\n- [ ] Verify TODO values\n"),
            ("## Disclosure\n", "## Disclosure\nTBD prompt attribution\n"),
            ("## Tool settings\n", "## Tool settings\n- TODO settings\n"),
            ("## Log\n", "## Log\n- TBD record\n"),
            ("TASK: Re-imagine", "TASK: Re-imagine TODO"),
        )
        for old, new in mutations:
            with self.subTest(old=old):
                self.assertFalse(_result(_grade_text(_replace(original, old, new))[1], "C1")[0])

    def test_task_todos_are_not_word_boundary_false_positives(self):
        original = _read(WITH_SKILL)
        for task in ("Review todos: preserve facade bays", "Review TBDs: preserve facade bays"):
            with self.subTest(task=task):
                text = _replace(original,
                                "TASK: Re-imagine the dated east-elevation render with a timber-cladding mood while keeping the six bays, entrance, roofline and camera",
                                "TASK: " + task)
                self.assertTrue(_result(_grade_text(text)[1], "C1")[0])

    def test_named_style_variants_fail_with_reformulation(self):
        original = _read(WITH_SKILL)
        for phrase in ("style of Zaha Hadid", "manner of Frank Lloyd Wright",
                       "work of Tadao Ando", "inspired by Lina Bo Bardi"):
            with self.subTest(phrase=phrase):
                text = _replace(original,
                                "Movement/palette rung — warm timber rainscreen language; no named architect",
                                "Movement/palette rung — " + phrase)
                ok, detail = _result(_grade_text(text)[1], "C3")
                self.assertFalse(ok)
                self.assertIn("reformulate", detail)

    def test_reject_drift_rule_must_be_anchored_affirmative_and_escalate(self):
        original = _read(WITH_SKILL)
        valid_line = "REJECT-DRIFT RULE: on drift, reject the output and redo in an authoritative editor."
        invalid_lines = (
            "we never reject outputs; drift is acceptable; redo in an editor",
            "REJECT-DRIFT RULE: drift is acceptable; do not reject; redo in an editor",
            "note: REJECT-DRIFT RULE: reject drift and redo in an authoritative editor",
            "REJECT-DRIFT RULE: reject drift but try again with adjectives",
            "REJECT-DRIFT RULE: reject drift; no authoritative editor, never redo",
        )
        for line in invalid_lines:
            with self.subTest(line=line):
                text = _replace(original,
                                "REJECT-DRIFT RULE: on drift of any LOCKED invariant — reject, redo in an authoritative CAD/photo editor or attach better measured inputs; never re-prompt adjectives at a drifted output.",
                                line)
                self.assertFalse(_result(_grade_text(text)[1], "C4")[0])
        text = _replace(original,
                        "REJECT-DRIFT RULE: on drift of any LOCKED invariant — reject, redo in an authoritative CAD/photo editor or attach better measured inputs; never re-prompt adjectives at a drifted output.",
                        valid_line)
        self.assertTrue(_result(_grade_text(text)[1], "C4")[0])

    def test_arbitrary_key_like_qa_lines_do_not_override_header(self):
        original = _read(WITH_SKILL)
        text = _replace(original,
                        "## QA gate\n",
                        "## QA gate\nBAY_COUNT_WAIVER_APPROVED: yes\n")
        keys, sections = grader.parse(text)
        self.assertEqual(keys["CARD"], "A02")
        self.assertNotIn("BAY_COUNT_WAIVER_APPROVED", keys)
        self.assertIn("BAY_COUNT_WAIVER_APPROVED: yes", "\n".join(sections["qa gate"]))
        self.assertTrue(_grade_text(text)[0])

    def test_photo_yes_requires_nonempty_tool_settings_section(self):
        original = _read(WITH_SKILL)
        missing = _replace(original, "## Tool settings\n", "## Empty settings\n")
        self.assertFalse(_result(_grade_text(missing)[1], "F11")[0])
        empty = _replace(original, "- Image 1 = A (geometry/base):", "")
        empty = _replace(empty, "- No style reference attached", "")
        empty = _replace(empty, "- img2img denoise 0.45", "")
        self.assertFalse(_result(_grade_text(empty)[1], "F11")[0])

    def test_c2_failure_explanation_contains_reason_not_pass_copy(self):
        text = _replace(_read(WITH_SKILL),
                        "- East elevation view at eye level — same camera and framing as the dated render (projection invariant)\n",
                        "")
        ok, detail = _result(_grade_text(text)[1], "C2")
        self.assertFalse(ok)
        self.assertIn("lacks the projection/view invariant", detail)
        self.assertNotIn("explicit", detail)

    def test_c6_failure_explanation_contains_reason_not_pass_copy(self):
        text = _replace(_read(WITH_SKILL), "https://github.com/tatsufinn-commits/Skills", "missing-source")
        ok, detail = _result(_grade_text(text)[1], "C6")
        self.assertFalse(ok)
        self.assertIn("lacks a URL", detail)
        self.assertNotIn("complete", detail)

    def test_missing_file_is_clean_usage_error_exit_two(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            status = grader.main(["grader.py", "/definitely/missing/worksheet.md"])
        self.assertEqual(status, 2)
        self.assertIn("error: worksheet not found", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_invalid_usage_exits_two(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            status = grader.main(["grader.py"])
        self.assertEqual(status, 2)
        self.assertIn("usage:", stderr.getvalue())

    def test_documented_gate_ids_claims_and_version_are_reconciled(self):
        def read(relative):
            with open(os.path.join(PACKAGE, relative), encoding="utf-8") as handle:
                return handle.read()
        card = read("REIMAGINE_SKILL_CARD.md")
        proc = read("scaffolding/PROC_REIMAGINE.md")
        legal = read("references/legal-postures.md")
        readme = read("README.md")
        self.assertIn("**G3 PD 1096", card)
        self.assertIn("**G5 Style authority", card)
        self.assertNotIn("G3 style", proc)
        self.assertIn("G5", proc)
        self.assertIn("## G5 — Style authority", legal)
        phrase = "16-item audit (15 captured practitioner prompts + 1 own comparator)"
        clause = "(single-plate, 3-run calibration; the winning run still retained only 25.4% of required-annotation pixels — measured, not magic)"
        for document in (readme, card):
            self.assertIn(phrase, document)
            self.assertIn("2 of the 15 captured prompts", document)
            self.assertIn(clause, document)
            self.assertIn("0.1.1", document)
        self.assertIn("v0.1.1", read("evals/grader.py"))

    def test_text_only_schema_and_named_style_limit_are_documented(self):
        def read(relative):
            with open(os.path.join(PACKAGE, relative), encoding="utf-8") as handle:
                return handle.read()
        config = read("scaffolding/CONFIG_WORKSHEET.md")
        evidence = read("evidence/EVIDENCE_APPENDIX.md")
        with open(os.path.join(PACKAGE, "schemas/worksheet.schema.json"),
                  encoding="utf-8") as handle:
            schema = json.load(handle)
        self.assertIn("N/A — text-only brief; fidelity claims dropped", config)
        self.assertIn("alter list must contain an `N/A` item", config)
        self.assertEqual(len(schema["properties"]["CARD"]["enum"]), 34)
        self.assertEqual(grader.CARD_IDS, set(schema["properties"]["CARD"]["enum"]))
        self.assertIn("N/A — text-only brief; fidelity claims dropped",
                      schema["properties"]["sections"]["properties"]["preserve list"]["description"])
        self.assertIn("does not detect", evidence)


if __name__ == "__main__":
    unittest.main()
