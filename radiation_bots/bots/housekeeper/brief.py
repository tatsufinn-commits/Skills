"""Short machine brief — lessens ceremony for the superior AI."""

from __future__ import annotations

from pathlib import Path

from shared.report import Report
from shared.paths import RepoPaths
from housekeeper.check import run_check


def run_brief(repo: RepoPaths | None = None) -> Report:
    repo = repo or RepoPaths()
    check_report = run_check(repo)

    version_line = None
    readme = repo.join("README.md")
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="replace").splitlines()[:30]:
            if "Version:" in line or "**Version:**" in line:
                version_line = line.strip()
                break

    results = check_report.data.get("results") or []
    absent = [r["name"] for r in results if r.get("status") == "ABSENT"]
    failed = [r["name"] for r in results if r.get("status") == "FAIL"]
    passed = [r["name"] for r in results if r.get("status") == "PASS"]

    ceremony_skip = []
    if passed and not failed:
        ceremony_skip.append("full validate re-audit optional if brief age fresh")
    if failed:
        ceremony_skip.append("do_not_skip: FAIL-class present — investigate findings")

    data = {
        "version_hint": version_line or "UNKNOWN",
        "check_ok": check_report.ok,
        "passed": passed,
        "failed": failed,
        "absent": absent,
        "ceremony_skip": ceremony_skip,
        "open_warns": check_report.warnings + check_report.findings,
    }

    return Report(
        bot="housekeeper",
        verb="brief",
        ok=check_report.ok,
        findings=check_report.findings,
        warnings=check_report.warnings,
        residuals=check_report.residuals,
        data=data,
    )
