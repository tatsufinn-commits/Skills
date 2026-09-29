"""Minimal ICS VEVENT extractor (stdlib only)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, date, timezone
from typing import Iterator
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


@dataclass
class CalEvent:
    uid: str
    summary: str
    dtstart: str
    dtend: str | None
    description: str | None
    location: str | None
    raw_start: date | datetime | None = None


def _unfold(text: str) -> str:
    # RFC 5545 line folding: CRLF + space/tab continuation
    return re.sub(r"\r?\n[ \t]", "", text)


def _parse_dt(value: str) -> date | datetime | None:
    value = value.strip()
    # strip TZID=...: prefix
    if ":" in value and value.upper().startswith("TZID") or value.upper().startswith("VALUE"):
        value = value.split(":", 1)[-1]
    if value.endswith("Z") and "T" in value:
        try:
            return datetime.strptime(value, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    if "T" in value:
        for fmt in ("%Y%m%dT%H%M%S", "%Y%m%dT%H%M%S%z"):
            try:
                return datetime.strptime(value.replace("Z", ""), fmt) if "%z" not in fmt else datetime.strptime(value, fmt)
            except ValueError:
                continue
        try:
            return datetime.strptime(value[:15], "%Y%m%dT%H%M%S")
        except ValueError:
            return None
    try:
        return datetime.strptime(value[:8], "%Y%m%d").date()
    except ValueError:
        return None


def iter_vevents(ics_text: str) -> Iterator[CalEvent]:
    text = _unfold(ics_text)
    blocks = re.split(r"BEGIN:VEVENT", text, flags=re.I)
    for block in blocks[1:]:
        end = re.split(r"END:VEVENT", block, maxsplit=1, flags=re.I)[0]
        fields: dict[str, str] = {}
        for line in end.splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue
            key, val = line.split(":", 1)
            key = key.split(";")[0].upper()
            fields[key] = val
        summary = fields.get("SUMMARY", "(no title)")
        dtstart = fields.get("DTSTART", "")
        raw = _parse_dt(dtstart) if dtstart else None
        yield CalEvent(
            uid=fields.get("UID", ""),
            summary=summary,
            dtstart=dtstart,
            dtend=fields.get("DTEND"),
            description=fields.get("DESCRIPTION"),
            location=fields.get("LOCATION"),
            raw_start=raw,
        )


def load_ics_from_path(path: str) -> str:
    return open(path, encoding="utf-8", errors="replace").read()


def load_ics_from_url(url: str, timeout: int = 30) -> str:
    req = Request(url, headers={"User-Agent": "radiation-calendar-summary/0.1"})
    with urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")
