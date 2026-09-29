"""Calendar summary CLI — ICS → organized brief for the superior AI."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from calendar_summary.brief import run_calendar_brief, write_brief_files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="calendar_summary",
        description="RADIATION Calendar Summary — ICS to AI-readable deadlines/events (not a planner)",
    )
    parser.add_argument("--ics", type=str, default=None, help="Path to .ics file")
    parser.add_argument("--url", type=str, default=None, help="ICS URL (or env RADIATION_ICS_URL)")
    parser.add_argument("--out", type=str, default=None, help="Directory for calendar_brief.md/json")
    parser.add_argument("--json", action="store_true", help="JSON to stdout")
    parser.add_argument(
        "--no-redact-url",
        action="store_true",
        help="Show full URL in report (default redacts)",
    )
    args = parser.parse_args(argv)

    report = run_calendar_brief(
        ics_path=args.ics,
        ics_url=args.url,
        redact_url=not args.no_redact_url,
    )

    if args.out:
        paths = write_brief_files(report, Path(args.out))
        report.data["written"] = paths

    print(report.to_json() if args.json else report.to_markdown())
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
