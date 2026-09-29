#!/usr/bin/env python3
"""
Problem-Formation receipt template + validator + detection helpers (v0.2).
Always-on clarify/reframe gate support — no second AI, no research engine.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


VALID_PATHS = {"PROCEED", "ASSUME", "ASK", "REFRAME", "CONFIRM"}
VALID_STATUS = {"OPEN", "SEALED", "WAITING_COMMANDER"}
VALID_LEVELS = {"low", "medium", "high"}
VALID_CONF = {"HIGH", "MEDIUM", "LOW"}


def _utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class Detection:
    """Severity layer — consumes Scan-like signals (DETECTION.md)."""

    scan_confidence: str = "MEDIUM"
    tuple_depth: str = "working"
    slot_fill: dict[str, str] = field(
        default_factory=lambda: {
            "goal": "missing",
            "success": "missing",
            "scope": "missing",
            "constraints": "missing",
        }
    )
    fork_materiality: str = "medium"
    error_cost: str = "low"
    ambiguity_severity: str = "medium"
    path_bias: str = "ASK"
    notes: str = ""

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.scan_confidence not in VALID_CONF:
            errs.append(f"bad scan_confidence: {self.scan_confidence}")
        for name in ("fork_materiality", "error_cost", "ambiguity_severity"):
            if getattr(self, name) not in VALID_LEVELS:
                errs.append(f"bad {name}")
        if self.path_bias not in VALID_PATHS:
            errs.append(f"bad path_bias: {self.path_bias}")
        return errs


def score_severity(
    scan_confidence: str,
    slots_missing: float,
    fork_materiality: str,
    error_cost: str,
) -> str:
    conf = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(scan_confidence, 1)
    slots = 0 if slots_missing <= 0 else (1 if slots_missing < 2 else 2)
    fork = {"low": 0, "medium": 1, "high": 2}.get(fork_materiality, 1)
    cost = {"low": 0, "medium": 1, "high": 2}.get(error_cost, 0)
    total = conf + slots + fork + cost
    if total <= 1:
        return "low"
    if total <= 3:
        return "medium"
    return "high"


def path_bias_from_detection(
    scan_confidence: str,
    tuple_depth: str,
    fork_materiality: str,
    error_cost: str,
    ambiguity_severity: str,
    slots_missing: float,
) -> str:
    """DETECTION.md §7 top-down (simplified)."""
    if error_cost == "high" and (
        slots_missing > 0 or scan_confidence in ("MEDIUM", "LOW")
    ):
        return "CONFIRM"
    if fork_materiality == "high" or scan_confidence == "LOW":
        return "ASK"
    if ambiguity_severity == "high":
        return "ASK"
    if (
        ambiguity_severity == "medium"
        and error_cost in ("low", "medium")
        and slots_missing <= 1
    ):
        return "ASSUME"
    if tuple_depth == "exhaustive" and slots_missing > 0:
        return "ASK"
    if (
        scan_confidence == "HIGH"
        and slots_missing == 0
        and fork_materiality == "low"
        and error_cost == "low"
    ):
        return "PROCEED"
    return "ASK"


@dataclass
class ProblemFormationReceipt:
    path: str
    original_ask: str
    gaps: list[str] = field(default_factory=list)
    known: list[str] = field(default_factory=list)
    assumed: list[str] = field(default_factory=list)
    unknown: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    questions: list[dict[str, Any]] = field(default_factory=list)
    reframed_task: str | None = None
    status: str = "OPEN"
    why_path: str = ""
    detection: dict[str, Any] | None = None
    generated: str = field(default_factory=_utc)
    schema_version: str = "clarify/problem_formation/0.2"

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.path not in VALID_PATHS:
            errs.append(f"invalid path: {self.path}")
        if self.status not in VALID_STATUS:
            errs.append(f"invalid status: {self.status}")
        if self.path == "ASK":
            if not self.questions:
                errs.append("ASK requires questions")
            if len(self.questions) > 3:
                errs.append("ASK allows at most 3 questions")
            if self.status not in ("WAITING_COMMANDER", "OPEN"):
                errs.append("ASK should be WAITING_COMMANDER or OPEN until answered")
        if self.path == "ASSUME" and not self.assumptions:
            errs.append("ASSUME requires assumptions list")
        if self.path == "REFRAME":
            if not self.reframed_task:
                errs.append("REFRAME requires reframed_task")
            if not self.assumptions:
                errs.append("REFRAME requires assumptions")
        if self.path == "PROCEED" and self.questions:
            errs.append("PROCEED must not carry questions")
        return errs

    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2, ensure_ascii=False)

    def to_markdown(self) -> str:
        lines = [
            "# PROBLEM_FORMATION",
            "",
            f"- generated: `{self.generated}`",
            f"- path: **{self.path}**",
            f"- status: **{self.status}**",
            f"- schema: `{self.schema_version}`",
            f"- why: {self.why_path or '(none)'}",
            "",
        ]
        if self.detection:
            lines.append("## Detection")
            for k, v in self.detection.items():
                lines.append(f"- **{k}:** {v}")
            lines.append("")
        lines.append("## Original ask")
        lines.append(self.original_ask or "(empty)")
        lines.append("")
        lines.append("## Gaps")
        for g in self.gaps or ["(none)"]:
            lines.append(f"- {g}")
        lines.append("")
        lines.append("## Assumptions")
        for a in self.assumptions or ["(none)"]:
            lines.append(f"- {a}")
        lines.append("")
        lines.append("## Questions (max 3)")
        if not self.questions:
            lines.append("- (none)")
        for q in self.questions:
            lines.append(
                f"- R{q.get('rank', '?')}: {q.get('text', '')} _(blocks: {q.get('blocks', '')})_"
            )
        lines.append("")
        lines.append("## Reframed task")
        lines.append(self.reframed_task or "(none)")
        lines.append("")
        return "\n".join(lines)


def template_proceed(ask: str) -> ProblemFormationReceipt:
    det = Detection(
        scan_confidence="HIGH",
        tuple_depth="surface",
        slot_fill={
            "goal": "present",
            "success": "present",
            "scope": "present",
            "constraints": "present",
        },
        fork_materiality="low",
        error_cost="low",
        ambiguity_severity="low",
        path_bias="PROCEED",
        notes="Green path demo",
    )
    return ProblemFormationReceipt(
        path="PROCEED",
        original_ask=ask,
        status="SEALED",
        why_path="Detection: HIGH confidence, slots ok, fork low, error_cost low",
        detection=asdict(det),
    )


def template_ask(ask: str, questions: list[dict[str, Any]]) -> ProblemFormationReceipt:
    det = Detection(
        scan_confidence="LOW",
        tuple_depth="working",
        slot_fill={
            "goal": "weak",
            "success": "missing",
            "scope": "weak",
            "constraints": "missing",
        },
        fork_materiality="high",
        error_cost="medium",
        ambiguity_severity="high",
        path_bias="ASK",
        notes="Vague ask; material fork",
    )
    return ProblemFormationReceipt(
        path="ASK",
        original_ask=ask,
        gaps=["Material interpretation fork", "success missing"],
        questions=questions[:3],
        status="WAITING_COMMANDER",
        why_path="Detection: LOW confidence, fork high, severity high",
        detection=asdict(det),
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Problem-Formation receipt helper v0.2")
    p.add_argument("--ask", type=str, default="")
    p.add_argument("--demo", choices=["proceed", "ask"], default="proceed")
    p.add_argument("--json", action="store_true")
    p.add_argument("--validate-json", type=str)
    args = p.parse_args(argv)

    if args.validate_json:
        data = json.loads(open(args.validate_json, encoding="utf-8").read())
        rec = ProblemFormationReceipt(
            path=data["path"],
            original_ask=data.get("original_ask", ""),
            gaps=data.get("gaps") or [],
            known=data.get("known") or [],
            assumed=data.get("assumed") or [],
            unknown=data.get("unknown") or [],
            assumptions=data.get("assumptions") or [],
            questions=data.get("questions") or [],
            reframed_task=data.get("reframed_task"),
            status=data.get("status", "OPEN"),
            why_path=data.get("why_path", ""),
            detection=data.get("detection"),
            generated=data.get("generated") or _utc(),
            schema_version=data.get("schema_version") or "clarify/problem_formation/0.2",
        )
        errs = rec.validate()
        if errs:
            print("INVALID:", *errs, sep="\n- ")
            return 1
        print("VALID")
        return 0

    ask = args.ask or "(demo ask)"
    if args.demo == "ask":
        rec = template_ask(
            ask,
            [
                {
                    "rank": 1,
                    "text": "Which deliverable shape do you want: outline only or full graded pack?",
                    "blocks": "output type",
                },
                {
                    "rank": 2,
                    "text": "Is this for exam review or permanent Core admission?",
                    "blocks": "stakes / depth",
                },
            ],
        )
    else:
        rec = template_proceed(ask)

    errs = rec.validate()
    if errs:
        print("INVALID:", *errs, sep="\n- ")
        return 1
    print(rec.to_json() if args.json else rec.to_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
