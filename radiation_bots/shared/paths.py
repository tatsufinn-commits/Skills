"""Repo path resolution and hygiene allowlists."""

from __future__ import annotations

import os
from pathlib import Path


# Default hygiene allowlist (relative to repo root). Expand only by config.
DEFAULT_HYGIENE_GLOBS = [
    "**/__pycache__",
    "**/*.pyc",
    "**/*.pyo",
    "**/.pytest_cache",
    "**/tmp_housekeeper_*",
]

# Never touch — even if someone misconfigures.
FORBIDDEN_PREFIXES = [
    ".git/",
    "docs/AI_RULES.md",
    "docs/shrine/",
    "09-nota/",
    "docs/PATCH_LEDGER.md",
    "docs/PATCH_PROTOCOL.md",
]


class RepoPaths:
    def __init__(self, root: Path | None = None):
        if root is None:
            env = os.environ.get("RADIATION_ROOT")
            root = Path(env) if env else Path.cwd()
        self.root = root.resolve()

    def join(self, *parts: str) -> Path:
        return (self.root.joinpath(*parts)).resolve()

    def rel(self, path: Path) -> str:
        try:
            return str(path.resolve().relative_to(self.root))
        except ValueError:
            return str(path)


def allowlisted(path: Path, root: Path, globs: list[str] | None = None) -> bool:
    """Return True if path may be deleted/cleaned under hygiene rules."""
    globs = globs or DEFAULT_HYGIENE_GLOBS
    try:
        rel = path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    rel_s = rel.as_posix()
    for bad in FORBIDDEN_PREFIXES:
        if rel_s == bad.rstrip("/") or rel_s.startswith(bad):
            return False
    # Match simple suffix / name patterns from globs
    for g in globs:
        g = g.replace("**/", "")
        if g.startswith("*") and rel_s.endswith(g[1:]):
            return True
        if g in ("__pycache__",) and path.name == g:
            return True
        if path.name == g or rel_s.endswith("/" + g):
            return True
    return False
