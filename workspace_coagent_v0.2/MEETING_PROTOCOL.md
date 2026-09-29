# Meeting protocol (formatted)

**Extension:** Co-Agent Workspace v0.2  

---

## Room layout

```text
workspace/
  GROUND_RULES.md                 # standing
  extension/                      # coagent extension docs
  meetings/
    <MEETING_ID>/
      00_MEETING.md               # charter + status
      01_ROSTER.md
      02_MESSAGES.md              # append-only
      03_DECISIONS.md
      04_OUTCOME.md
      seats/                      # optional per-seat notes
        LEAD.md
        A1.md
```

Numbered prefixes = read order for any agent joining late.

---

## Status line (always top of 00_MEETING.md)

```text
STATUS: OPEN | PHASE: isolate|exchange|merge|SEALED | N: 2 | WORKSPACE: yes
```

---

## Phases (short)

| Phase | Parallel? | Rule |
|-------|-----------|------|
| **isolate** | **Yes** | Own branch only; one isolate block in 02_MESSAGES |
| **exchange** | **Yes** | LETTER/PIPELINE; append messages; pull |
| **merge** | LEAD leads | OUTCOME; disagreement OK |
| **SEALED** | No | Freeze room |

---

## Message format (strict)

```markdown
### T<n> · <YYYY-MM-DDTHH:MM:SSZ>

| FROM | SEAT | ROLE | TO | PHASE | TYPE |
|------|------|------|-----|-------|------|
| DESK | A1 | researcher | LEAD | exchange | LETTER |

<body>

---
```

Table header is preferred (scannable). Classic bracket headers still accepted.

---

**End meeting protocol.**
