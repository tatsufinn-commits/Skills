#!/usr/bin/env bash
# Init a Co-Agent workspace meeting room from templates.
# v0.2.1 fix (TSSTM, S021): MEETING_ID charset validated before sed use
# (F-4 — an ID containing '/', '&' or ';' previously corrupted substitution).
set -euo pipefail
ID="${1:?usage: init_meeting.sh MEETING_ID [target_dir]}"
ROOT="${2:-.}"
DEST="$ROOT/meetings/$ID"
TPL="$(cd "$(dirname "$0")/.." && pwd)/templates"

case "$ID" in
  ''|*[!A-Za-z0-9._-]*)
    echo "error: MEETING_ID must contain only letters, digits, '.', '_' or '-' (got: $ID)" >&2
    exit 1
    ;;
esac

mkdir -p "$DEST/seats"
for f in 00_MEETING 01_ROSTER 02_MESSAGES 03_DECISIONS 04_OUTCOME; do
  sed -e "s/<MEETING_ID>/$ID/g" -e "s/<ID>/$ID/g" "$TPL/${f}.md" > "$DEST/${f}.md"
done
echo "initialized $DEST"
echo "next: fill 00_MEETING.md + 01_ROSTER.md; create branches coagent/$ID/LEAD …"
