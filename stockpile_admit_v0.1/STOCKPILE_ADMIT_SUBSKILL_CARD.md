# `@stockpile` / `@admit` — Epistemic Admission

**Class:** Active skill · research-quality memory gate  
**Version:** 0.1.0 (archive / design-of-record)  
**Date:** 2026-09-29  
**Status:** Prepared for placement — **not** live canon until Desk/Commander authorize  
**Parents:** Stockpile doctrine · Evidence taxonomy · Triangulation · Inspect / Overhaul / Nota  
**Doctrine:** Triangulation remains the only elevator to Core / long-term. This skill **executes** admission with a receipt — it does not bypass law.

---

## MISSION

Decide what may become **house knowledge** (session harvest, claim set, or candidate Brain items):

| Decision | Meaning |
|----------|---------|
| **ADMIT** | Meets grade + triangulation rules → eligible path toward long-term / Core per existing law |
| **QUARANTINE** | Useful but under-sourced or conflicted — hold, do not elevate |
| **REJECT** | Contamination, single-source-as-fact, or fails zero-contamination |
| **DECAY-PROPOSE** | New triangulated evidence undermines an existing stored item → propose decay/update |

**Goal:** Make zero-contamination and triangulation **operable**, not only constitutional.

---

## TRIGGER

```text
@[MODE] | STYLE: […] | TOPIC: [claim set | session harvest | “admit these”]
| Skill: @stockpile | @admit
```

Commander-triggered or after Research/Educate/Coagent when permanence is at stake.  
**Not** always-on for every chat sentence.

---

## INPUTS

- Candidate claims / findings (from session or explicit list)  
- Optional: pointer to existing Brain items to re-check  
- Evidence already gathered (sources, grades if present)  

---

## PROTOCOL SUMMARY (`proc_stockpile-admit`)

1. **Inventory** — list candidates as atomic claims  
2. **Grade** — apply `[D][O][I][R][N][S]` (or house taxonomy in force)  
3. **Triangulate** — independent source count / independence check  
4. **Conflict scan** — vs known Brain / prior admits  
5. **Decide** — ADMIT | QUARANTINE | REJECT | DECAY-PROPOSE per claim  
6. **Receipt** — machine-readable + Commander-facing summary  
7. **Hand-off** — Nota / Patch proposal only; AI does not write Core unilaterally  

---

## FORBIDDEN

- Admit without triangulation when law requires it for that tier  
- Silent elevation to Core  
- Treating coagent agreement as triangulation  
- Admitting personal speculation as `[D]` primary  
- Bypassing Commander seal on decay of sealed knowledge  

---

## OUTPUT

```text
ADMIT_RUN
- candidates: n
- decisions: [{ claim, decision, grades, sources_n, notes }]
- admit[] quarantine[] reject[] decay_propose[]
- residuals: …
- next: Nota / Patch / none
- commander_seal: PENDING
```

---

## ACCEPTANCE TESTS

| # | Test | Pass |
|---|------|------|
| T1 | Single-source hard claim | REJECT or QUARANTINE, not ADMIT to Core path |
| T2 | Two independent sources + grades | ADMIT path allowed per law |
| T3 | Conflicts with Brain | surface conflict; DECAY-PROPOSE or QUARANTINE |
| T4 | Receipt produced | required |
| T5 | No unilateral Core write | only proposal / hand-off |

---

## RELATED

- Live: Stockpile doctrine, EVIDENCE_TAXONOMY, 06-triangulate, 09-nota  
- Archive: `@educate` (depth before admit), `@coagent` (stress before admit), clarify (sharp claims)  

---

**End skill card v0.1.**
