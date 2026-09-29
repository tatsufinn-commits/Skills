#!/usr/bin/env python3
"""Append a formatted turn to 02_MESSAGES.md (Co-Agent workspace extension)."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("messages", type=Path)
    p.add_argument("--from", dest="frm", required=True)
    p.add_argument("--seat", required=True)
    p.add_argument("--role", default="")
    p.add_argument("--to", required=True)
    p.add_argument("--phase", default="exchange")
    p.add_argument("--type", dest="typ", default="LETTER")
    p.add_argument("--body", required=True)
    p.add_argument("--turn", type=int, default=None)
    args = p.parse_args()

    path = args.messages
    if not path.exists():
        raise SystemExit(f"missing {path}")

    text = path.read_text(encoding="utf-8")
    turn = args.turn if args.turn is not None else text.count("### T")
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    block = f"""
### T{turn} · {ts}

| FROM | SEAT | ROLE | TO | PHASE | TYPE |
|------|------|------|-----|-------|------|
| {args.frm} | {args.seat} | {args.role} | {args.to} | {args.phase} | {args.typ} |

{args.body.strip()}

---
"""
    path.open("a", encoding="utf-8").write(block)
    print(f"ok T{turn} -> {path}")


if __name__ == "__main__":
    main()
