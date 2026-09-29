# RADIATION Worker Bots (skeleton v0.1)

**Housekeeper** + **Calendar Summary** — Python worker bots for one superior AI + many skills.

These are **portable skeletons**. They do not push to `main`. Port into RADIATION via Patch when DESK/Commander authorize.

## Quick start

```bash
cd radiation_bots

# Housekeeper
python housekeeper/cli.py brief
python housekeeper/cli.py check --json
python housekeeper/cli.py hygiene          # dry-run
python housekeeper/cli.py hygiene --apply  # allowlisted only

# Calendar summary
python calendar_summary/cli.py --ics tests/fixtures/sample.ics
python calendar_summary/cli.py --ics tests/fixtures/sample.ics --out /tmp/cal_brief --json

# Optional live feed (Commander-armed URL)
export RADIATION_ICS_URL='https://…blackboard-share-ics…'
python calendar_summary/cli.py --json
```

## Tests

```bash
python -m pytest tests/ -q
# or without pytest:
python tests/test_calendar_parse.py
python tests/test_housekeeper_brief.py
```

## Architecture

See `docs/ARCHITECTURE.md`.

## Doctrine

- Workers only — not second AIs  
- Hygiene default dry-run; forbidden paths never deleted  
- Calendar bot summarizes; it does not plan study  
- Secrets via env (`RADIATION_ICS_URL`, `RADIATION_ROOT`)  
