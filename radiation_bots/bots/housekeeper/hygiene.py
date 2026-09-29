"""Allowlisted hygiene — default dry-run. Never touches canon."""

from __future__ import annotations

import shutil
from pathlib import Path

from shared.report import Report
from shared.paths import RepoPaths, allowlisted, DEFAULT_HYGIENE_GLOBS


def _collect_candidates(root: Path) -> list[Path]:
    found: list[Path] = []
    for p in root.rglob("*"):
        if allowlisted(p, root, DEFAULT_HYGIENE_GLOBS):
            found.append(p)
    return found


def run_hygiene(repo: RepoPaths | None = None, apply: bool = False) -> Report:
    repo = repo or RepoPaths()
    candidates = _collect_candidates(repo.root)
    planned = [repo.rel(p) for p in candidates]
    removed: list[str] = []
    residuals: list[str] = []

    if not apply:
        return Report(
            bot="housekeeper",
            verb="hygiene",
            ok=True,
            warnings=["dry-run (pass --apply to delete allowlisted paths)"],
            data={"planned": planned, "count": len(planned), "applied": False},
            residuals=residuals,
        )

    for p in candidates:
        try:
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=False)
            elif p.is_file():
                p.unlink()
            removed.append(repo.rel(p))
        except OSError as e:
            residuals.append(f"failed {repo.rel(p)}: {e}")

    return Report(
        bot="housekeeper",
        verb="hygiene",
        ok=len(residuals) == 0,
        findings=[f"removed {len(removed)} paths"] if removed else [],
        data={"removed": removed, "count": len(removed), "applied": True},
        residuals=residuals,
    )
