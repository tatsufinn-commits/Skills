"""Smoke tests for housekeeper (works out-of-tree with ABSENT checkers)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from shared.paths import RepoPaths
from housekeeper.brief import run_brief
from housekeeper.hygiene import run_hygiene
from housekeeper.check import run_check


def test_check_skeleton_mode():
    # Use package root as fake repo — checkers ABSENT, should not crash
    repo = RepoPaths(ROOT)
    r = run_check(repo)
    assert r.bot == "housekeeper"
    assert "results" in r.data


def test_brief_runs():
    repo = RepoPaths(ROOT)
    r = run_brief(repo)
    assert r.verb == "brief"
    assert "ceremony_skip" in r.data or "passed" in r.data


def test_hygiene_dry_run():
    repo = RepoPaths(ROOT)
    r = run_hygiene(repo, apply=False)
    assert r.ok
    assert r.data.get("applied") is False
