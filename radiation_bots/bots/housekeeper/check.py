"""Run allowlisted integrity checkers; degrade honestly if scripts absent."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

from shared.report import Report
from shared.paths import RepoPaths


# Map logical name → candidate script paths relative to repo root
CHECKER_CANDIDATES: dict[str, list[str]] = {
    "validate": ["scripts/validate.py"],
    "cue_lint": ["scripts/cue_resolver.py"],
    "verify_cassette": ["scripts/verify_cassette_runner.py"],
    "preflight": ["scripts/push_preflight_check.py"],
}


def _run_checker(root: Path, name: str, script: Path) -> dict[str, Any]:
    if name == "cue_lint":
        cmd = [sys.executable, str(script), "--lint"]
    elif name == "verify_cassette":
        cmd = [sys.executable, str(script), "--json"]
    else:
        cmd = [sys.executable, str(script)]
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(root),
            capture_output=True,
            text=True,
            timeout=120,
        )
        return {
            "name": name,
            "script": str(script),
            "returncode": proc.returncode,
            "status": "PASS" if proc.returncode == 0 else "FAIL",
            "stdout_tail": (proc.stdout or "")[-500:],
            "stderr_tail": (proc.stderr or "")[-300:],
        }
    except subprocess.TimeoutExpired:
        return {"name": name, "status": "FAIL", "error": "timeout"}
    except OSError as e:
        return {"name": name, "status": "FAIL", "error": str(e)}


def run_check(repo: RepoPaths | None = None) -> Report:
    repo = repo or RepoPaths()
    results: list[dict[str, Any]] = []
    findings: list[str] = []
    warnings: list[str] = []
    residuals: list[str] = []

    for name, candidates in CHECKER_CANDIDATES.items():
        found = None
        for rel in candidates:
            p = repo.join(rel)
            if p.is_file():
                found = p
                break
        if found is None:
            results.append({"name": name, "status": "ABSENT"})
            residuals.append(f"{name}: script not found (ABSENT — not a fake PASS)")
            continue
        row = _run_checker(repo.root, name, found)
        results.append(row)
        if row.get("status") == "FAIL":
            findings.append(f"{name}: FAIL (rc={row.get('returncode', '?')})")
        elif row.get("status") == "PASS":
            pass
        else:
            warnings.append(f"{name}: {row.get('status')}")

    fail = any(r.get("status") == "FAIL" for r in results)
    present = [r for r in results if r.get("status") != "ABSENT"]
    if not present:
        warnings.append("No house checkers found — running in skeleton/out-of-tree mode")

    return Report(
        bot="housekeeper",
        verb="check",
        ok=not fail,
        findings=findings,
        warnings=warnings,
        residuals=residuals,
        data={"results": results, "checkers_present": len(present)},
    )
