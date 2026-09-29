"""Build CALENDAR_BRIEF report for the superior AI."""

from __future__ import annotations

import os
from pathlib import Path

from shared.report import Report
from calendar_summary.parse_ics import (
    iter_vevents,
    load_ics_from_path,
    load_ics_from_url,
)
from calendar_summary.summarize import summarize_events
from urllib.error import URLError, HTTPError


def run_calendar_brief(
    ics_path: str | None = None,
    ics_url: str | None = None,
    redact_url: bool = True,
) -> Report:
    residuals: list[str] = []
    source_label = "none"
    text = None

    url = ics_url or os.environ.get("RADIATION_ICS_URL")
    if ics_path:
        try:
            text = load_ics_from_path(ics_path)
            source_label = f"file:{ics_path}"
        except OSError as e:
            return Report(
                bot="calendar_summary",
                verb="brief",
                ok=False,
                findings=[f"cannot read ICS path: {e}"],
                data={},
            )
    elif url:
        try:
            text = load_ics_from_url(url)
            source_label = "url:REDACTED" if redact_url else f"url:{url}"
        except (URLError, HTTPError, TimeoutError, ValueError) as e:
            return Report(
                bot="calendar_summary",
                verb="brief",
                ok=False,
                findings=[f"ICS fetch failed: {type(e).__name__}: {e}"],
                residuals=["Arm RADIATION_ICS_URL or pass --ics / --url"],
                data={"source": "url"},
            )
    else:
        return Report(
            bot="calendar_summary",
            verb="brief",
            ok=False,
            findings=["No ICS source: pass --ics PATH, --url URL, or set RADIATION_ICS_URL"],
            data={},
        )

    events = list(iter_vevents(text or ""))
    if not events:
        residuals.append("No VEVENT blocks parsed — feed empty or non-standard ICS")

    summary = summarize_events(events)
    summary["source"] = source_label

    # AI-facing flat deadline list (next 14 days default spotlight)
    spotlight = summary.get("by_window", {}).get("next_14_days") or []

    return Report(
        bot="calendar_summary",
        verb="brief",
        ok=True,
        data={
            "source": source_label,
            "spotlight_next_14_days": spotlight,
            "summary": summary,
        },
        residuals=residuals,
        warnings=[] if events else ["Zero events parsed"],
    )


def write_brief_files(report: Report, out_dir: Path) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    md = out_dir / "calendar_brief.md"
    js = out_dir / "calendar_brief.json"
    md.write_text(report.to_markdown(), encoding="utf-8")
    js.write_text(report.to_json(), encoding="utf-8")
    return [str(md), str(js)]
