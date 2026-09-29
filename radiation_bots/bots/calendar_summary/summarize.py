"""Organize events into deadline-oriented structures."""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from typing import Any

from calendar_summary.parse_ics import CalEvent


def _as_date(v: date | datetime | None) -> date | None:
    if v is None:
        return None
    if isinstance(v, datetime):
        return v.date()
    return v


def summarize_events(
    events: list[CalEvent],
    today: date | None = None,
    windows: list[int] | None = None,
) -> dict[str, Any]:
    today = today or date.today()
    windows = windows or [7, 14, 30]

    dated: list[tuple[date, CalEvent]] = []
    undated: list[CalEvent] = []
    for e in events:
        d = _as_date(e.raw_start)
        if d is None:
            undated.append(e)
        else:
            dated.append((d, e))
    dated.sort(key=lambda x: x[0])

    by_window: dict[str, list[dict[str, str]]] = {}
    for days in windows:
        end = today + timedelta(days=days)
        key = f"next_{days}_days"
        by_window[key] = [
            {
                "date": d.isoformat(),
                "summary": e.summary,
                "location": e.location or "",
            }
            for d, e in dated
            if today <= d <= end
        ]

    upcoming = [
        {"date": d.isoformat(), "summary": e.summary, "location": e.location or ""}
        for d, e in dated
        if d >= today
    ][:50]

    past_recent = [
        {"date": d.isoformat(), "summary": e.summary}
        for d, e in dated
        if today - timedelta(days=14) <= d < today
    ]

    return {
        "today": today.isoformat(),
        "total_events": len(events),
        "dated": len(dated),
        "undated": len(undated),
        "by_window": by_window,
        "upcoming": upcoming,
        "past_14_days": past_recent,
        "undated_titles": [e.summary for e in undated[:20]],
    }
