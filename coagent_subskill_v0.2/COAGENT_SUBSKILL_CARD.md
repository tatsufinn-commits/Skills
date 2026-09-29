# `@coagent` — Co-Agent Truth-Stress (v0.2)

**Class:** Commander-triggered skill · external multi-seat verification  
**Version:** 0.2.0 (archive / design-of-record)  
**Date:** 2026-09-29  
**Status:** Prepared for placement — **not** live canon until Desk/Commander authorize  
**Supersedes:** coagent_subskill v0.1 (folds retained; identity + scenario + weakness mitigations added)

---

## MISSION

Opt-in cross-seat truth-stress:

1. **Roster** (seats + code names + headers)  
2. **Scenario** (goals, roles, hierarchy, N, topology)  
3. **Isolate** (blind)  
4. **Diff**  
5. **Pipeline and/or LETTER** exchange  
6. **Merge or STRUCTURED_DISAGREEMENT**  
7. **Commander seal**  

**Goal:** Best-supported answer + residuals — **not** absolute truth, **not** forced consensus, **not** peer government.

**Depth:** No token caps. Stop on evidence exhaustion, holds complete, success test, or Commander halt.

**Runtime bus:** Commander (or designated carrier) **silent paste** between panes — no coaching text.

---

## TRIGGER (mode console — no public ARM)

```text
@[MODE] | STYLE: [style|AUTO] | TOPIC: [task]
| Co-Agent: yes|no
| Challengers: …          # optional shorthand
| Configuration State: truth-stress|council|adversarial
| Scenario: [id or inline] # optional; loads playbook
| N: 1|2|3|4               # seats under LEAD; default 1
```

| Field | Default |
|-------|---------|
| Co-Agent | **no** |
| Configuration State | `truth-stress` if Co-Agent yes |
| N | **1** (LEAD + one challenger seat) |
| Scenario | none → minimal charter from TOPIC + state |

---

## LAYER MAP

| Layer | Location | Job |
|-------|----------|-----|
| Skill law | this card | when / forbidden / tests |
| Identity & routing | `identity/IDENTITY_AND_ROUTING.md` | seats, code names, headers, PIPELINE vs LETTER, delegation |
| Scenarios | `scenarios/` | N=1..4 playbooks; goals/roles/hierarchy |
| Process scaffold | `scaffolding/PROC_COAGENT_DEBATE.md` | folds 0–8 |
| Carrier templates | `templates/` | paste blocks |
| Weakness mitigations | `WEAKNESS_MITIGATIONS.md` | explicit counters |

---

## ROLES (authority)

| Actor | Authority |
|-------|-----------|
| **Commander** | Seal, halt, mission override, silent relay |
| **LEAD (superior AI)** | Single voice to Commander; delegates tasks; owns merge package |
| **A1–A4** | Execute role; LETTER only as allowed; no mission hijack |

**Hivemind = shared process, not shared crown.**

---

## FORBIDDEN

- Absolute-truth claims  
- Forced consensus when conflict is informative  
- Skipping isolate / roster  
- Body-only pastes (no FROM/TO/PHASE)  
- Agents reordering government without LEAD/Commander  
- Always-on Co-Agent from silence  
- Vote count as truth  

---

## OUTPUT

```text
COAGENT_RUN v0.2
- scenario / N / state
- roster: [{seat, codename, role, provider}]
- isolate summaries
- diff: agree[] conflict[]
- routing_log: pipeline|letter entries
- outcome: MERGED | STRUCTURED_DISAGREEMENT | DUAL_CONFIRM
- best_supported / residuals
- commander_seal: PENDING|ACCEPTED|OVERRIDE
```

---

## ACCEPTANCE TESTS

| # | Test | Pass |
|---|------|------|
| T1 | Co-Agent omitted | idle |
| T2 | No roster before LETTER | blocked |
| T3 | Isolate blind | no cross-read in Fold 2 |
| T4 | Disagreement legal | STRUCTURED_DISAGREEMENT ok |
| T5 | Header missing | carrier refuses relay |
| T6 | N>4 without override | reject |
| T7 | LEAD remains Commander-facing | one package |

---

**End skill card v0.2.**
