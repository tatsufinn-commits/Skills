"""Housekeeper CLI — worker bot entrypoint."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running from package root without install
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from shared.paths import RepoPaths
from housekeeper.check import run_check
from housekeeper.brief import run_brief
from housekeeper.hygiene import run_hygiene
from housekeeper.diff_seal import run_diff_seal
from housekeeper.registry_doctor import run_registry_doctor
from housekeeper.capability_snapshot import run_capability_snapshot


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="housekeeper",
        description="RADIATION Housekeeper — integrity, brief, hygiene (not a second AI)",
    )
    parser.add_argument(
        "verb",
        choices=[
            "check",
            "brief",
            "hygiene",
            "diff-seal",
            "registry-doctor",
            "capability-snapshot",
        ],
    )
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--root", type=str, default=None, help="Repo root (or RADIATION_ROOT)")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="hygiene only: actually delete allowlisted paths",
    )
    args = parser.parse_args(argv)

    repo = RepoPaths(Path(args.root) if args.root else None)

    if args.verb == "check":
        report = run_check(repo)
    elif args.verb == "brief":
        report = run_brief(repo)
    elif args.verb == "hygiene":
        report = run_hygiene(repo, apply=args.apply)
    elif args.verb == "diff-seal":
        report = run_diff_seal(repo)
    elif args.verb == "registry-doctor":
        report = run_registry_doctor(repo)
    else:
        report = run_capability_snapshot(repo)

    out = report.to_json() if args.json else report.to_markdown()
    print(out)
    if not report.ok:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
