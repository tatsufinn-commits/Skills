#!/usr/bin/env python3
"""
@mapua helper — schema template + pack validation (no live scrape engine).
Worker support for the superior AI; not a second mind.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


VALID_ACTIONS = {
    "course-pack",
    "exit-exam",
    "prof",
    "org",
    "official-search",
    "secondary-scan",
    "gap-expand",
}

VALID_STATUS = {
    "FOUND_OFFICIAL",
    "FOUND_SECONDARY_ONLY",
    "MIXED",
    "NOT_FOUND_PUBLIC",
    "BLOCKED",
}


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class MapuaPack:
    action: str
    query: str
    status: str
    claims: list[dict[str, Any]] = field(default_factory=list)
    sources: list[dict[str, Any]] = field(default_factory=list)
    hypotheses: list[dict[str, Any]] = field(default_factory=list)
    residuals: list[str] = field(default_factory=list)
    calendar_bonus: list[dict[str, Any]] = field(default_factory=list)
    next_acquisition: list[str] = field(default_factory=list)
    generated: str = field(default_factory=_utc)
    schema_version: str = "mapua_pack/0.1"

    def validate(self) -> list[str]:
        errors: list[str] = []
        if self.action not in VALID_ACTIONS:
            errors.append(f"invalid action: {self.action}")
        if self.status not in VALID_STATUS:
            errors.append(f"invalid status: {self.status}")
        for h in self.hypotheses:
            if h.get("label") != "UNVERIFIED":
                errors.append("hypothesis missing label UNVERIFIED")
        # Invention guard: NOT_FOUND should not carry factual claims
        if self.status == "NOT_FOUND_PUBLIC" and self.claims:
            errors.append("NOT_FOUND_PUBLIC must not include claims (use hypotheses/residuals)")
        return errors

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, ensure_ascii=False)

    def to_markdown(self) -> str:
        lines = [
            f"# MAPUA_PACK — {self.action}",
            "",
            f"- generated: `{self.generated}`",
            f"- query: {self.query}",
            f"- status: **{self.status}**",
            f"- schema: `{self.schema_version}`",
            "",
            "## Claims",
        ]
        if not self.claims:
            lines.append("- (none)")
        for c in self.claims:
            lines.append(f"- [{c.get('grade', '?')}] {c.get('text', '')} — `{c.get('source_url_or_id', '')}`")
        lines.append("")
        lines.append("## Sources")
        if not self.sources:
            lines.append("- (none)")
        for s in self.sources:
            lines.append(f"- {s.get('type', '')}: {s.get('url_or_id', '')} — {s.get('note', '')}")
        lines.append("")
        lines.append("## Hypotheses (UNVERIFIED only)")
        if not self.hypotheses:
            lines.append("- (none)")
        for h in self.hypotheses:
            lines.append(f"- {h.get('text', '')} _{h.get('label', '')}_")
        lines.append("")
        lines.append("## Residuals")
        for r in self.residuals or ["(none)"]:
            lines.append(f"- {r}")
        lines.append("")
        lines.append("## Calendar bonus (non-authoritative for exit exams)")
        if not self.calendar_bonus:
            lines.append("- (none)")
        for b in self.calendar_bonus:
            lines.append(f"- {b}")
        lines.append("")
        lines.append("## Next acquisition")
        for n in self.next_acquisition or ["(none)"]:
            lines.append(f"- {n}")
        lines.append("")
        return "\n".join(lines)


def template(action: str, query: str, status: str = "NOT_FOUND_PUBLIC") -> MapuaPack:
    pack = MapuaPack(action=action, query=query, status=status)
    if status == "NOT_FOUND_PUBLIC":
        pack.residuals.append("No public sources packaged in this template run")
        pack.next_acquisition.extend(
            [
                "Check official mapua.edu.ph / college pages for program assessment rules",
                "Commander: paste LMS announcement if auth-walled",
                "Secondary: site search and Reddit with course code — grade secondary only",
            ]
        )
        if action == "exit-exam":
            pack.hypotheses.append(
                {
                    "text": "Exit/assessment details may live on LMS or faculty channels not visible on ICS or public web",
                    "label": "UNVERIFIED",
                }
            )
            pack.residuals.append("Empty ICS must not be read as 'no exam'")
    return pack


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="@mapua pack template / validator")
    p.add_argument("action", choices=sorted(VALID_ACTIONS))
    p.add_argument("--query", required=True)
    p.add_argument("--status", default="NOT_FOUND_PUBLIC", choices=sorted(VALID_STATUS))
    p.add_argument("--json", action="store_true")
    p.add_argument("--validate-json", type=str, help="Validate an existing pack JSON file")
    args = p.parse_args(argv)

    if args.validate_json:
        data = json.loads(open(args.validate_json, encoding="utf-8").read())
        pack = MapuaPack(
            action=data["action"],
            query=data["query"],
            status=data["status"],
            claims=data.get("claims") or [],
            sources=data.get("sources") or [],
            hypotheses=data.get("hypotheses") or [],
            residuals=data.get("residuals") or [],
            calendar_bonus=data.get("calendar_bonus") or [],
            next_acquisition=data.get("next_acquisition") or [],
            generated=data.get("generated") or _utc(),
            schema_version=data.get("schema_version") or "mapua_pack/0.1",
        )
        errs = pack.validate()
        if errs:
            print("INVALID:", *errs, sep="\n- ")
            return 1
        print("VALID")
        return 0

    pack = template(args.action, args.query, args.status)
    errs = pack.validate()
    if errs:
        print("INVALID template:", *errs, sep="\n- ")
        return 1
    print(pack.to_json() if args.json else pack.to_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
