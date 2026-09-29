"""Diff working tree hints vs EXPECTATION / README pins when present."""

from __future__ import annotations

import json
from pathlib import Path

from shared.report import Report
from shared.paths import RepoPaths


def run_diff_seal(repo: RepoPaths | None = None) -> Report:
    repo = repo or RepoPaths()
    residuals: list[str] = []
    data: dict = {}

    exp = repo.join("docs/RELEASE_TRUTH_GATE/EXPECTATION.json")
    if exp.is_file():
        try:
            payload = json.loads(exp.read_text(encoding="utf-8"))
            data["expectation_keys"] = list(payload.keys()) if isinstance(payload, dict) else []
            data["expectation_present"] = True
            # Soft: expose allowed_changes if present
            if isinstance(payload, dict) and "allowed_changes" in payload:
                data["allowed_changes"] = payload.get("allowed_changes")
        except json.JSONDecodeError as e:
            residuals.append(f"EXPECTATION.json unreadable: {e}")
            data["expectation_present"] = True
    else:
        data["expectation_present"] = False
        residuals.append("EXPECTATION.json ABSENT — diff-seal limited in skeleton mode")

    # Lightweight: list dirty-ish markers only if .git exists (no git required for skeleton)
    git_dir = repo.join(".git")
    data["git_present"] = git_dir.is_dir()

    return Report(
        bot="housekeeper",
        verb="diff-seal",
        ok=True,
        data=data,
        residuals=residuals,
        warnings=["full git-diff vs pin requires in-repo integration with EXPECTATION base"],
    )
