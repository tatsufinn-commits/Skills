#!/usr/bin/env bash
# Init a Co-Agent workspace meeting room from templates.
set -euo pipefail
ID="${1:?usage: init_meeting.sh MEETING_ID [target_dir]}"
ROOT="${2:-.}"
DEST="$ROOT/meetings/$ID"
TPL="$(cd "$(dirname "$0")/.." && pwd)/templates"
mkdir -p "$DEST/seats"
for f in 00_MEETING 01_ROSTER 02_MESSAGES 03_DECISIONS 04_OUTCOME; do
  sed "s/<MEETING_ID>/$ID/g; s/\`\$ID\`/$ID/g" "$TPL/${f}.md" > "$DEST/${f}.md" 2>/dev/null \
    || sed "s/<MEETING_ID>/$ID/g" "$TPL/${f}.md" > "$DEST/${f}.md"
done
# fix ID placeholders
for f in "$DEST"/*.md; do
  sed -i "s/<MEETING_ID>/$ID/g; s/<ID>/$ID/g" "$f"
done
echo "initialized $DEST"
echo "next: fill 00_MEETING.md + 01_ROSTER.md; create branches coagent/$ID/LEAD …"
