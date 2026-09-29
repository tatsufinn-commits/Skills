#!/usr/bin/env python3
"""Append a formatted turn to 02_MESSAGES.md (Co-Agent workspace extension).

v0.2.1 fixes (TSSTM, S021, 2026-09-29 — Commander-ordered polish):
  F-1  turn numbering now counts ANCHORED headers only (^### T<n>), so a
       message body that merely mentions '### T' cannot inflate the count
       (the S020 pilot self-demonstrated this bug live).
  F-3  the file handle is closed properly (with-block).
CLI unchanged. Stdlib only.
"""
from __future__ import annotations

import argparse
import sys
import re
from datetime import datetime, timezone
from pathlib import Path

_HEADER_RE = re.compile(r"^### T(\d+)", re.MULTILINE)


def next_turn(text: str) -> int:
    """Next turn number = number of anchored turn headers in the room file."""
    return len(_HEADER_RE.findall(text))


def render_block(frm: str, seat: str, role: str, to: str, phase: str, typ: str,
                 body: str, turn: int, ts: str) -> str:
    """Render one headed turn block (append-only payload)."""
    return f"""
### T{turn} · {ts}

| FROM | SEAT | ROLE | TO | PHASE | TYPE |
|------|------|------|-----|-------|------|
| {frm} | {seat} | {role} | {to} | {phase} | {typ} |

{body.strip()}

---
"""


def main_cli(argv) -> None:
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
    args = p.parse_args(argv)

    path = args.messages
    if not path.exists():
        raise SystemExit(f"missing {path}")

    text = path.read_text(encoding="utf-8")
    turn = args.turn if args.turn is not None else next_turn(text)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    block = render_block(args.frm, args.seat, args.role, args.to, args.phase,
                         args.typ, args.body, turn, ts)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(block)
    print(f"ok T{turn} -> {path}")


def main() -> None:
    main_cli(sys.argv[1:])


if __name__ == "__main__":
    main()
