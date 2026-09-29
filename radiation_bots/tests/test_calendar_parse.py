"""Smoke tests for calendar summary bot."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from calendar_summary.parse_ics import iter_vevents, load_ics_from_path
from calendar_summary.summarize import summarize_events
from calendar_summary.brief import run_calendar_brief


FIXTURE = Path(__file__).parent / "fixtures" / "sample.ics"


def test_parse_sample_ics():
    text = load_ics_from_path(str(FIXTURE))
    events = list(iter_vevents(text))
    assert len(events) == 3
    assert "Midterm" in events[0].summary


def test_summarize():
    text = load_ics_from_path(str(FIXTURE))
    events = list(iter_vevents(text))
    s = summarize_events(events)
    assert s["total_events"] == 3
    assert s["dated"] == 3


def test_brief_from_file():
    report = run_calendar_brief(ics_path=str(FIXTURE))
    assert report.ok
    assert report.bot == "calendar_summary"
    assert "summary" in report.data
