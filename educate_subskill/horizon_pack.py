#!/usr/bin/env python3
"""
@educate helper — Horizon Pack template + light validation (no research engine).
Worker support for the superior AI; not a second mind.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


VALID_STATUS = {"ADEQUATE", "PARTIAL", "BLOCKED", "NOT_STARTED"}
VALID_STOP = {
    "use_case_met",
    "quota_met",
    "commander_halt",
    "blocked",
    None,
}
FOLDS = ["seed", "core", "necessary", "adjacent", "integrate", "gaps", "pack"]


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class HorizonPack:
    topic: str
    use_case: str
    status: str = "NOT_STARTED"
    folds_completed: list[str] = field(default_factory=list)
    core: list[dict[str, Any]] = field(default_factory=list)
    necessary: list[dict[str, Any]] = field(default_factory=list)
    adjacent: list[dict[str, Any]] = field(default_factory=list)
    integrations: list[dict[str, Any]] = field(default_factory=list)
    hypotheses: list[dict[str, Any]] = field(default_factory=list)
    residuals: list[str] = field(default_factory=list)
    depth_tags: dict[str, int] = field(
        default_factory=lambda: {"D1_count": 0, "D2_count": 0, "D3_count": 0}
    )
    sources_index: list[dict[str, Any]] = field(default_factory=list)
    stop_reason: str | None = None
    next_acquisition: list[str] = field(default_factory=list)
    generated: str = field(default_factory=_utc)
    schema_version: str = "educate/horizon/0.1"

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.status not in VALID_STATUS:
            errs.append(f"invalid status: {self.status}")
        if self.stop_reason not in VALID_STOP:
            errs.append(f"invalid stop_reason: {self.stop_reason}")
        for h in self.hypotheses:
            if h.get("label") != "UNVERIFIED":
                errs.append("hypothesis must have label UNVERIFIED")
        if self.status == "ADEQUATE" and not self.stop_reason:
            errs.append("ADEQUATE requires stop_reason")
        if self.status == "ADEQUATE" and not self.core and not self.necessary:
            errs.append("ADEQUATE should not have empty core and necessary")
        for f in self.folds_completed:
            if f not in FOLDS:
                errs.append(f"unknown fold: {f}")
        return errs

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, ensure_ascii=False)

    def to_markdown(self) -> str:
        lines = [
            f"# HORIZON_PACK — {self.topic}",
            "",
            f"- generated: `{self.generated}`",
            f"- use_case: {self.use_case}",
            f"- status: **{self.status}**",
            f"- stop_reason: `{self.stop_reason}`",
            f"- schema: `{self.schema_version}`",
            f"- folds: {', '.join(self.folds_completed) or '(none)'}",
            "",
            "## Core",
        ]
        if not self.core:
            lines.append("- (none)")
        for c in self.core:
            lines.append(
                f"- [{c.get('grade', '?')}] {c.get('claim', '')} — `{c.get('source', '')}`"
            )
        lines.append("")
        lines.append("## Necessary (to use under use-case)")
        if not self.necessary:
            lines.append("- (none)")
        for c in self.necessary:
            lines.append(
                f"- [{c.get('grade', '?')}] {c.get('claim', '')} — `{c.get('source', '')}`"
            )
        lines.append("")
        lines.append("## Adjacent / akin")
        if not self.adjacent:
            lines.append("- (none)")
        for a in self.adjacent:
            lines.append(
                f"- **{a.get('topic', '')}** ({a.get('relation', '')}): {a.get('claims', a.get('note', ''))}"
            )
        lines.append("")
        lines.append("## Integrations (multi-hop)")
        if not self.integrations:
            lines.append("- (none)")
        for i in self.integrations:
            lines.append(
                f"- {i.get('from', '')} → {i.get('to', '')}: {i.get('note', i.get('link', ''))}"
            )
        lines.append("")
        lines.append("## Hypotheses (UNVERIFIED)")
        if not self.hypotheses:
            lines.append("- (none)")
        for h in self.hypotheses:
            lines.append(f"- {h.get('text', '')} _{h.get('label', '')}_")
        lines.append("")
        lines.append("## Residuals")
        for r in self.residuals or ["(none)"]:
            lines.append(f"- {r}")
        lines.append("")
        lines.append("## Next acquisition")
        for n in self.next_acquisition or ["(none)"]:
            lines.append(f"- {n}")
        lines.append("")
        return "\n".join(lines)


def template(topic: str, use_case: str) -> HorizonPack:
    pack = HorizonPack(topic=topic, use_case=use_case, status="NOT_STARTED")
    pack.folds_completed = ["seed"]
    pack.residuals.append(
        "Template only — superior AI must run Horizon folds with real sources"
    )
    pack.next_acquisition.extend(
        [
            "Scout-gated fetch for core definitions and primary sources",
            "List prerequisites required by use_case (necessary fold)",
            "Identify 3–7 adjacent topics with relation tags",
            "Integrate multi-hop links; log conflicts side-by-side",
        ]
    )
    pack.hypotheses.append(
        {
            "text": "Parametric coverage may exceed expressed depth until folds complete",
            "label": "UNVERIFIED",
        }
    )
    return pack


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="@educate Horizon Pack template / validator")
    p.add_argument("--topic", required=False, help="Topic for template")
    p.add_argument("--use-case", default="general depth for session work")
    p.add_argument("--json", action="store_true")
    p.add_argument("--validate-json", type=str, help="Validate existing pack JSON")
    args = p.parse_args(argv)

    if args.validate_json:
        data = json.loads(open(args.validate_json, encoding="utf-8").read())
        pack = HorizonPack(
            topic=data.get("topic", ""),
            use_case=data.get("use_case", ""),
            status=data.get("status", "NOT_STARTED"),
            folds_completed=data.get("folds_completed") or [],
            core=data.get("core") or [],
            necessary=data.get("necessary") or [],
            adjacent=data.get("adjacent") or [],
            integrations=data.get("integrations") or [],
            hypotheses=data.get("hypotheses") or [],
            residuals=data.get("residuals") or [],
            depth_tags=data.get("depth_tags")
            or {"D1_count": 0, "D2_count": 0, "D3_count": 0},
            sources_index=data.get("sources_index") or [],
            stop_reason=data.get("stop_reason"),
            next_acquisition=data.get("next_acquisition") or [],
            generated=data.get("generated") or _utc(),
            schema_version=data.get("schema_version") or "educate/horizon/0.1",
        )
        errs = pack.validate()
        if errs:
            print("INVALID:", *errs, sep="\n- ")
            return 1
        print("VALID")
        return 0

    if not args.topic:
        print("Provide --topic or --validate-json", file=sys.stderr)
        return 2

    pack = template(args.topic, args.use_case)
    errs = pack.validate()
    if errs:
        print("INVALID:", *errs, sep="\n- ")
        return 1
    print(pack.to_json() if args.json else pack.to_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
