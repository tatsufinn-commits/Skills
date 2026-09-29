# RADIATION Bots — Architecture & Infrastructure

**Version:** 0.1.0 (skeleton)  
**Date:** 2026-09-24  
**Doctrine:** Worker bots only — not second AIs. One superior AI + many skills remains intact.

---

## 1. Principles

| Rule | Meaning |
|------|---------|
| Worker, not peer | Bots check, parse, report, hygiene — they do not choose modes, author Patches, or govern |
| Allowlist paths | Writes only to declared paths; default dry-run for destructive ops |
| Stdlib-first | Prefer Python standard library; optional deps gated and honest if ABSENT |
| Report-shaped | Structured stdout / JSON / markdown briefs the superior AI can load |
| One purpose per bot | Housekeeper = house integrity; Calendar = time brief |
| No Core pollution | Never write Core cards, AI_RULES, or patch ledgers |
| Secrets outside tree | ICS Share URLs / tokens via env vars, never committed |

---

## 2. Package layout

```text
radiation_bots/
├── docs/
│   └── ARCHITECTURE.md          # this file
├── shared/
│   ├── __init__.py
│   ├── report.py                # common JSON/MD report helpers
│   └── paths.py                 # allowlist / path resolution
├── housekeeper/
│   ├── __init__.py
│   ├── cli.py                   # entry: python -m housekeeper
│   ├── check.py
│   ├── brief.py
│   ├── hygiene.py
│   ├── diff_seal.py
│   ├── registry_doctor.py
│   └── capability_snapshot.py
├── calendar_summary/
│   ├── __init__.py
│   ├── cli.py
│   ├── parse_ics.py
│   ├── summarize.py
│   └── brief.py
├── tests/
│   ├── test_housekeeper_brief.py
│   ├── test_calendar_parse.py
│   └── fixtures/
│       └── sample.ics
├── pyproject.toml               # optional; runnable as scripts
└── README.md
```

**When porting into RADIATION main:** map to `scripts/housekeeper.py`, `scripts/calendar_summary_bot.py`, `tests/`, and TOOL_REGISTRY entries — this package is a **portable skeleton**, not a silent main push.

---

## 3. Bot 1 — Housekeeper

### Mission
Reduce ceremony for the superior AI and keep the tree honest: integrity battery, short brief, safe hygiene, drift vs seal, registry health, capability snapshot.

### Verbs

| Verb | Function |
|------|----------|
| `check` | Run allowlisted checkers (validate, cue lint, cassette if present); aggregate PASS/WARN/FAIL |
| `brief` | Short machine brief for AI bootstrap |
| `hygiene` | Allowlisted scratch/generated cleanup; **default dry-run** |
| `diff-seal` | Paths changed vs pinned base / EXPECTATION allowed set (if files exist) |
| `registry-doctor` | Tool registry + catalog-style checks if scripts exist |
| `capability-snapshot` | pptx/video/session capability lines if CAPABILITIES / state files exist |
| `warn-board` | WARN-only collapse |
| `ledger-tail` | Last N lines of known ledger paths (read-only) |

### Infrastructure

```text
CLI → verb module → shared.report
                 → subprocess or import of existing house scripts (when in-repo)
                 → exit code: 0 ok/warn, 1 fail/misuse
```

**Graceful degradation:** If a checker script is missing (skeleton mode / not yet in RADIATION tree), report `ABSENT` for that check — never fake PASS.

### Write allowlist (hygiene)

- `__pycache__/`, `*.pyc`
- Configurable scratch dirs (e.g. `Brain/short_term/active/` expendables — **only when configured**)
- Temp render dirs outside canon
- **Never:** `docs/AI_RULES.md`, `09-nota/`, `docs/shrine/`, `.git/`, patch ledgers

---

## 4. Bot 2 — Calendar Summary

### Mission
Turn ICS bytes into an **organized deadlines/events brief** the superior AI can read in one load. Not a planner.

### Pipeline

```text
Source resolver
  1. --ics path
  2. env RADIATION_ICS_URL or --url (fetch)
  3. default feed path if configured
        ↓
  parse_ics → event records
        ↓
  summarize → by date, by course, upcoming windows
        ↓
  brief → CALENDAR_BRIEF markdown + JSON
```

### Outputs

- `calendar_brief.md` / `.json` (path configurable; default stdout + optional `--out`)
- Residuals: unparsed lines, fetch errors, empty feed

### Infrastructure

```text
CLI → source → parse (stdlib ical-ish or line-based VEVENT extractor)
    → summarize → report
```

**Stdlib note:** Full RFC 5545 is heavy; skeleton uses a **minimal VEVENT extractor** sufficient for deadlines. In-repo can later call existing `ics_normalize` if present.

### Secrets

- `RADIATION_ICS_URL` — Blackboard Share Calendar link (armed by Commander)
- Never print full URL in logs if `--redact-url`

---

## 5. Shared infrastructure

| Module | Role |
|--------|------|
| `shared.report` | `Report` dataclass → `to_json()` / `to_markdown()` |
| `shared.paths` | Resolve repo root, allowlist check, safe join |

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success (WARN allowed) |
| 1 | FAIL-class finding or invalid args |
| 2 | Source missing / misconfiguration |

### CI hook (future)

```yaml
# conceptual
- run: python -m housekeeper check --json
- run: python -m calendar_summary --ics path/to/feed.ics --out briefs/
```

---

## 6. Composition with superior AI

```text
Session start (optional):
  housekeeper brief     → system health, skip-ceremony hints
  calendar_summary      → deadlines window
Superior AI loads both briefs → chooses skills/modes
Bots never activate skills themselves
```

---

## 7. Non-goals

- Second AI / swarm member  
- Patch authoring or auto-push to main  
- “Enhance cognition” or task priority advice  
- Blackboard DOM scrape  
- Writing Core or constitution  

---

## 8. Porting checklist (when DESK/Architect accept)

1. Copy scripts under `scripts/` with house naming  
2. Add TOOL_REGISTRY records (report-only / network only for calendar fetch)  
3. Tests under `tests/` discoverable  
4. Doctrine one-liner in CAPABILITIES or bot README  
5. Single-purpose Patch tranche  
6. Arm ICS URL via env/secret, not commit  

---

**End architecture.**
