# Problem-Formation Gate + `@clarify`

**Class:** Always-on **intake compliance** + scaffold; optional explicit skill pull  
**Version:** 0.2.0 (archive / design-of-record)  
**Date:** 2026-09-27  
**Status:** Prepared for future Patch — **not** on RADIATION main until Commander/DESK authorize  
**Parents:** Cue Autonomous Scan · Neuron sensory intake (`NEEDS_CLARIFY`) · BOOT ASK spirit · CTP honesty  
**Doctrine:** One superior AI. Fog must not become silent invention. Recognition of ambiguity must become **behavior**, not optional skill hope.
**Detection:** See `scaffolding/DETECTION.md` — severity consumes Scan; adds slot_fill, fork_materiality, error_cost → path bias.

---

## MISSION

When the Commander’s ask is **insufficient, unclear, or multi-interpretable**, the system **must not** proceed to PLAN/EXECUTE on a hidden guess.

Instead it runs a **Problem-Formation gate**:

1. Detect gaps (goal, success test, scope, constraints, irreversibility)  
2. Choose a path: **PROCEED · ASSUME · ASK · REFRAME · CONFIRM**  
3. Emit ranked questions **or** a reframed task with explicit assumptions  
4. Only then hand off to neurons / skills / `@educate` / Research  

**Evidence punchline:** LLMs often *recognize* ambiguity but *still answer directly* (“knowing but not showing”). Optional skills get skipped when overconfidence is highest. This capability is therefore **always-on compliance with a green pass**, not skill-only.

---

## ALWAYS-ON vs SKILL

| Layer | Role |
|-------|------|
| **Intake gate (always-on)** | Every post-Scan ask is checked; clear tasks pass with minimal ceremony |
| **Scaffold `proc_clarify-reframe`** | Full folds when path ≠ PROCEED |
| **Optional `@clarify` / `/reframe`** | Commander forces a re-run; mid-task fog; explicit pull |

**Primary = gate + scaffold. Skill = optional force, not the only path.**

---

## TRIGGERS (gate)

**Always:** run Detection (`scaffolding/DETECTION.md`) after Scan Declaration fields are available.

Fire **expanded** path (full scaffold) when Detection `path_bias` ≠ `PROCEED`, including when any hold:

- `scan_confidence = LOW` or Scan already requires ASK  
- `ambiguity_severity = medium|high`  
- Missing material slots (goal / success / scope / constraints)  
- `fork_materiality = high` (alternate reading changes work product)  
- `error_cost = high` (Core / motor / external / irreversible)  
- Neuron would mark `NEEDS_CLARIFY`  

**Green pass (PROCEED):** Detection rule — HIGH confidence, slots ok, fork low, error_cost low. One-line receipt; no interrogation.

---

## PATHS (normative)

Path **bias** comes from Detection policy (top-down rules in `DETECTION.md`). Human summary:

| Path | When | Behavior |
|------|------|----------|
| **PROCEED** | Severity low; slots ok; error_cost low | One-line intake note; no interrogation |
| **ASSUME** | Medium severity; minor gaps; reversible | State assumptions in one block; continue |
| **ASK** | High fork, LOW confidence, or exhaustive+missing slots | ≤3 ranked questions (blocking power first); wait |
| **REFRAME** | Problem can be sharpened with stated assumptions | Better problem statement + assumptions; Commander may veto |
| **CONFIRM** | High error_cost / irreversible / motor-class | State intended act + impact; require seal |

**Rule of value:** Ask only when the answer would **materially change the work** or **raise real risk**. Clarification is a means, not a ritual.  
**Merge rule:** If Scan already ASKs on mode/topic, merge into **≤3 total** questions with Problem-Formation slots.

---

## FORBIDDEN

- Silent assumption of intent when interpretations diverge materially  
- Question spam (no unbounded interviews)  
- Reframe that changes the ask **without** listing assumptions  
- Treating optional `@clarify` as the only mechanism  
- Proceeding to PLAN while path is ASK/CONFIRM unresolved  
- Inventing Commander preferences to fill gaps  

---

## OUTPUTS

### Gate receipt (always)

```text
PROBLEM_FORMATION
- path: PROCEED | ASSUME | ASK | REFRAME | CONFIRM
- gaps: [ … ]
- assumptions: [ … ]          # required for ASSUME / REFRAME
- questions: [ { rank, text, blocks } ]   # if ASK
- reframed_task: …            # if REFRAME
- status: OPEN | SEALED | WAITING_COMMANDER
```

### Hand-off

- `SEALED` / `PROCEED` / assumptions accepted → neuron PLAN or skill work  
- `WAITING_COMMANDER` → stop work on that TID until reply  

---

## COMPOSITION

| Peer | Relation |
|------|----------|
| Cue Scan / BOOT ASK | Mode-topic; this gate is **problem geometry** after/with Scan |
| Neuron sensory | `NEEDS_CLARIFY` **implements** this gate; reasoning record cites path |
| Origami / `/analyze` | Later: cannot execute *after* clear task |
| `@educate` | After task is sharp — deepen topic, don’t form the problem |
| CTP | Honesty on assumptions; no fake certainty |

---

## ACCEPTANCE TESTS (design)

| # | Test | Pass |
|---|------|------|
| T1 | Clear low-risk ask | PROCEED; no question list |
| T2 | Two deliverable-changing interpretations | ASK or REFRAME; not silent pick |
| T3 | ASK | ≤3 questions; ranked |
| T4 | ASSUME | Assumptions explicit in receipt |
| T5 | REFRAME | Original + reframed + assumptions |
| T6 | Optional skill only disabled | Gate still runs (compliance test) |
| T7 | Irreversible act | CONFIRM, not ASSUME |

---

## IMPLEMENTATION NOTES (Architect)

1. Doctrine pointer in cue / AI_RULES annex or CONTROL-adjacent intake law (Commander-ratified).  
2. Scaffold: `scaffolding/core/proc_clarify-reframe.md` (via improved/ → core when ratified).  
3. Neuron sensory templates reference gate receipt fields.  
4. Optional `subskills/active/clarify.md` for explicit `@clarify`.  
5. Optional `scripts/problem_formation_receipt.py` schema validate only.  
6. Single-purpose Patch; do not merge into `@educate` or Housekeeper.

---

**End of skill/gate card v0.1.**
