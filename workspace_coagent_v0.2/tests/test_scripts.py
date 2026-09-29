#!/usr/bin/env python3
"""Tests for the Co-Agent workspace scripts (TSSTM, S021).

Run exactly (from workspace_coagent_v0.2/):  python3 tests/test_scripts.py
Also works via:                              python3 -m unittest tests.test_scripts

Covers the v0.2.1 fixes:
  F-1  turn numbering ignores '### T' mentions inside message bodies
  F-3  append closes its file handle (no ResourceWarning)
  F-4  init_meeting.sh rejects unsafe MEETING_IDs before sed
plus core behaviors: room creation, placeholder substitution, header format,
append-only writes, full mini-cycle.
"""
import os
import re
import subprocess
import sys
import tempfile
import unittest
import warnings
from pathlib import Path

HERE = Path(os.path.abspath(os.path.dirname(__file__)))
PKG = HERE.parent
SCRIPTS = PKG / "scripts"

sys.path.insert(0, str(SCRIPTS))
import append_turn  # noqa: E402


def _bootstrap_room(path: Path) -> None:
    path.write_text(
        "# Messages `t`\n\n---\n\n### T0 · 2026-09-29T00:00:00Z\n\n"
        "Meeting open.\n\n---\n", encoding="utf-8")


class NextTurnTests(unittest.TestCase):
    def test_counts_anchored_headers_only(self):
        """F-1 regression: a body mentioning '### T' must not inflate the count."""
        room = ("# Messages `x`\n\n---\n\n### T0 · 2026-09-29T00:00:00Z\n\n"
                "warning: text.count('### T') is fragile\n\n---\n")
        self.assertEqual(append_turn.next_turn(room), 1)  # only T0 anchored

    def test_empty_room(self):
        self.assertEqual(append_turn.next_turn(""), 0)

    def test_multiple_turns(self):
        room = "### T0 · x\n\n---\n\n### T1 · x\n\n---\n"
        self.assertEqual(append_turn.next_turn(room), 2)


class AppendTurnTests(unittest.TestCase):
    def _room(self, tmp):
        path = Path(tmp) / "02_MESSAGES.md"
        _bootstrap_room(path)
        return path

    def _append(self, path, frm, body):
        with warnings.catch_warnings():
            warnings.simplefilter("error", ResourceWarning)  # F-3: no leaks
            append_turn.main_cli([str(path), "--from", frm, "--seat", frm,
                                  "--role", "verifier", "--to", "LEAD",
                                  "--phase", "exchange", "--type", "LETTER",
                                  "--body", body])

    def test_sequential_numbering_despite_body_mention(self):
        """The S020 pilot bug, end-to-end: a body containing '### T' must not
        skip the next turn number."""
        with tempfile.TemporaryDirectory() as tmp:
            path = self._room(tmp)
            self._append(path, "A1", "note: text.count('### T') is fragile")
            self._append(path, "A1", "second turn")
            final = path.read_text(encoding="utf-8")
            self.assertIn("### T1 ·", final)
            self.assertIn("### T2 ·", final)      # sequential — not T3
            headers = re.findall(r"^### T(\d+)", final, re.MULTILINE)
            self.assertEqual(headers, ["0", "1", "2"])

    def test_header_table_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._room(tmp)
            self._append(path, "DESK", "hello from the desk")
            final = path.read_text(encoding="utf-8")
            self.assertIn("| FROM | SEAT | ROLE | TO | PHASE | TYPE |", final)
            self.assertIn("| DESK |", final)

    def test_append_only(self):
        """Pre-existing content must survive appends untouched."""
        with tempfile.TemporaryDirectory() as tmp:
            path = self._room(tmp)
            before = path.read_text(encoding="utf-8")
            self._append(path, "A1", "appended")
            after = path.read_text(encoding="utf-8")
            self.assertTrue(after.startswith(before))

    def test_missing_file_exits(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit):
                append_turn.main_cli([str(Path(tmp) / "nope.md"), "--from",
                                      "x", "--seat", "x", "--to", "y",
                                      "--body", "b"])


class InitMeetingTests(unittest.TestCase):
    def _run(self, meeting_id, root):
        return subprocess.run(
            ["bash", str(SCRIPTS / "init_meeting.sh"), meeting_id, str(root)],
            capture_output=True, text=True, timeout=30)

    def test_creates_room_with_placeholders_filled(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self._run("2026-09-29-desk-link", tmp)
            self.assertEqual(result.returncode, 0, result.stderr)
            room = Path(tmp) / "meetings" / "2026-09-29-desk-link"
            for name in ("00_MEETING.md", "01_ROSTER.md", "02_MESSAGES.md",
                         "03_DECISIONS.md", "04_OUTCOME.md"):
                self.assertTrue((room / name).exists(), name)
            self.assertTrue((room / "seats").is_dir())
            text = (room / "00_MEETING.md").read_text(encoding="utf-8")
            self.assertIn("2026-09-29-desk-link", text)
            self.assertNotIn("<MEETING_ID>", text)
            self.assertNotIn("<ID>", text)

    def test_rejects_unsafe_ids(self):
        """F-4: IDs that would corrupt sed must fail fast."""
        for bad in ("a/b", "x&y", "semi;colon", "sp ace", ""):
            with tempfile.TemporaryDirectory() as tmp:
                result = self._run(bad, tmp)
                self.assertNotEqual(result.returncode, 0, "id=%r" % bad)
                self.assertFalse((Path(tmp) / "meetings").exists(),
                                 "id=%r created a room" % bad)


class FullCycleTests(unittest.TestCase):
    def test_init_append_outcome_cycle(self):
        """Room init → two appends → sequential numbering → outcome present."""
        with tempfile.TemporaryDirectory() as tmp:
            proc = subprocess.run(
                ["bash", str(SCRIPTS / "init_meeting.sh"), "cycle-test", tmp],
                capture_output=True, text=True, timeout=30)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            room = Path(tmp) / "meetings" / "cycle-test"
            msg = room / "02_MESSAGES.md"
            for i, body in enumerate(("first", "second")):
                run = subprocess.run(
                    [sys.executable, str(SCRIPTS / "append_turn.py"), str(msg),
                     "--from", "A%d" % i, "--seat", "A%d" % i, "--to", "LEAD",
                     "--body", body],
                    capture_output=True, text=True, timeout=30)
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertIn("ok T%d" % (i + 1), run.stdout)  # T1 then T2
            text = msg.read_text(encoding="utf-8")
            headers = re.findall(r"^### T(\d+)", text, re.MULTILINE)
            self.assertEqual(headers, ["0", "1", "2"])
            self.assertTrue((room / "04_OUTCOME.md").exists())


if __name__ == "__main__":
    unittest.main()
