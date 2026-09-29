# Scenario Playbooks (N = 1..4)

**Version:** 0.2.0  
**Parent:** `@coagent`  
**Rule:** Every run with N>0 should load a scenario charter (named or minimal).

---

## Charter template

```text
SCENARIO
- id:
- goal:
- success_test:
- N: 1|2|3|4
- state: truth-stress|council|adversarial
- hierarchy: LEAD > …
- roles: { LEAD: …, A1: …, … }
- topology: star|pair|pipeline|council
- letter: on|off
- stop: evidence|hold|success|commander_halt
```

---

## N=1 — Dual confirm / self-stress

| Seat | Role |
|------|------|
| LEAD | Primary solver |
| A1 | Challenger (prefer **other provider**) |

- Topology: pair  
- LETTER: off until after isolate  
- Typical state: truth-stress or council  

**Note:** Two seats on **same** model family = weak diversity; still allowed if Commander accepts.

---

## N=2 — Truth-stress standard

| Seat | Role |
|------|------|
| LEAD | Primary / merge owner |
| A1 | Adversary / challenger |
| A2 | Evidence auditor (attacks support quality, not ego) |

- Topology: pipeline LEAD→A1→A2→LEAD or star (both report to LEAD)  
- LETTER: on after isolate for A1↔A2 checks  
- State: truth-stress  

---

## N=3 — Full stress

| Seat | Role |
|------|------|
| LEAD | Primary / Commander-facing merge |
| A1 | Researcher / solver-alt |
| A2 | Adversary |
| A3 | Fact-checker / auditor |

- Topology: pipeline or scenario path (e.g. A1→A3→A2→LEAD)  
- LETTER: on, **capped** (one active thread)  
- Prefer cross-provider on A1 or A2  

---

## N=4 — Maximum (rare)

| Seat | Role |
|------|------|
| LEAD | Merge + seal package |
| A1 | Research |
| A2 | Adversary |
| A3 | Fact-check |
| A4 | Red-team / residual hunter |

- **Default off** unless Commander explicit  
- LETTER strict cap; prefer pipeline phases  
- Higher conformity risk — mitigations mandatory  

---

## Council variant (any N)

- All isolate  
- No rebuttal rounds  
- LEAD synthesizes only  
- LETTER: off  

---

## Adversarial variant

- Named claim  
- Explicit SUPPORT vs CHALLENGE seats  
- Same evidence / concede-or-hold rules  

---

## Minimal scenario (no id)

If Commander only sets Co-Agent yes + TOPIC:

```text
goal = TOPIC
success_test = answer TOPIC correctly with graded support
N = 1
state = truth-stress
roles = LEAD primary, A1 challenger
letter = off until post-isolate
```

---

**End scenario playbooks.**
