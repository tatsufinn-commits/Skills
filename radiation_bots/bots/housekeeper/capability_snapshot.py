"""Snapshot capability lines from CAPABILITIES / README when present."""

from __future__ import annotations

import re

from shared.report import Report
from shared.paths import RepoPaths


def run_capability_snapshot(repo: RepoPaths | None = None) -> Report:
    repo = repo or RepoPaths()
    hits: list[str] = []
    for rel in ("docs/CAPABILITIES.md", "README.md"):
        p = repo.join(rel)
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for line in text.splitlines():
            if re.search(r"pptx|AVAILABLE|ABSENT-UNKNOWN|capability", line, re.I):
                if "pptx" in line.lower() or "AVAILABLE" in line or "ABSENT" in line:
                    hits.append(f"{rel}: {line.strip()[:200]}")
    return Report(
        bot="housekeeper",
        verb="capability-snapshot",
        ok=True,
        data={"lines": hits[:20], "count": len(hits)},
        residuals=[] if hits else ["No capability lines found (out-of-tree or docs missing)"],
    )
