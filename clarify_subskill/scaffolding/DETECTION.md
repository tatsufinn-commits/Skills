# Problem-Formation Detection Layer

**Version:** 0.2.0  
**Role:** Score **severity of fog** before path select — consumes Autonomous Scan; does not replace it.  
**Package:** clarify_subskill  

---

## 1. Principle

```text
Autonomous Scan (existing)     →  task nature + confidence
Detection layer (this doc)     →  ambiguity severity + error cost
Problem-Formation paths        →  PROCEED | ASSUME | ASK | REFRAME | CONFIRM
```

- **Always run detection** (cheap structured fields).  
- **Do not** always expand into full clarify folds.  
- Clear + low-cost → green **PROCEED**.  
- Fog + high stakes → structured path.

---

## 2. Inputs (from Scan + prompt)

| Input | Source | Values |
|-------|--------|--------|
| `scan_confidence` | Scan Phase 4 | `HIGH` \| `MEDIUM` \| `LOW` |
| `tuple_depth` | Scan tuple DEPTH | `surface` \| `working` \| `exhaustive` |
| `deliverable` | Scan tuple | `answer` \| `corpus` \| `paper` \| `comprehension-map` \| … |
| `permanence` | Scan tuple | `ephemeral` \| `stored` \| `canonical` |
| `competing_readings` | Phase 2 Step 3 | list (may be empty) |
| `original_ask` | Prompt | verbatim |

Detection **adds** (not in classic Scan):

| Field | Meaning |
|-------|---------|
| `slot_fill` | Which of goal / success / scope / constraints are present |
| `fork_materiality` | Would an alternate reading change the **work product**? |
| `error_cost` | Cost if we guess wrong |
| `ambiguity_severity` | Composite used for path bias |

---

## 3. Slot fill

For each slot, mark `present` | `weak` | `missing`:

| Slot | Present when |
|------|----------------|
| **goal** | Clear artifact or outcome stated or firmly implied |
| **success** | How “done” is judged (even informal) |
| **scope** | In/out or bounded topic |
| **constraints** | Format, deadline, sources, tools, or “none stated” explicitly acceptable |

`slots_missing_count` = number of `missing` (weak counts as 0.5 for policy thresholds if useful).

---

## 4. Fork materiality

| Level | Criterion |
|-------|-----------|
| **low** | Alternates differ only in tone, length, or minor wording |
| **medium** | Alternates change sectioning, depth, or audience but same artifact class |
| **high** | Alternates change deliverable class, mode, Core vs ephemeral, or tool path |

If Scan listed competing readings on **two+** tuple elements → fork at least **medium**.  
If two full modes equally plausible (Scan LOW rule) → fork **high**.

---

## 5. Error cost

| Level | Criterion |
|-------|-----------|
| **low** | Reversible session prose; no Core; no motor; no external publish |
| **medium** | Stored Brain / dossier / multi-step research time cost |
| **high** | Canonical / Core admission, patch proposal framed as ready, push/motor, external send, irreversible config |

Heuristics:

- `permanence = canonical` → error_cost at least **medium**, often **high**  
- Control-plane effect beyond read → **high** until CONFIRM/order  
- `@Data` ephemeral answer → often **low** if slots ok  

---

## 6. Ambiguity severity (composite)

```text
severity_score:
  scan_confidence:  HIGH=0  MEDIUM=1  LOW=2
  slots_missing:    0 / 1 / 2+
  fork_materiality: low=0  medium=1  high=2
  error_cost:       low=0  medium=1  high=2

ambiguity_severity:
  0–1  → low
  2–3  → medium
  4+   → high
```

(Implement as integer sum; document ties as medium.)

---

## 7. Path bias policy (normative)

Evaluate **top-down**; first match wins:

| # | Condition | Path |
|---|-----------|------|
| 1 | `error_cost = high` AND any material gap or MEDIUM/LOW confidence | **CONFIRM** if act is irreversible; else **ASK** |
| 2 | `fork_materiality = high` OR `scan_confidence = LOW` | **ASK** or **REFRAME** (prefer ASK if only Commander can split; REFRAME if problem can be sharpened with stated assumptions) |
| 3 | `ambiguity_severity = high` | **ASK** (or REFRAME) |
| 4 | `ambiguity_severity = medium` AND `error_cost ≤ medium` AND gaps minor | **ASSUME** (list assumptions) |
| 5 | `tuple_depth = exhaustive` AND any `missing` slot | Prefer **ASK** over ASSUME |
| 6 | `scan_confidence = HIGH` AND slots ok AND `fork_materiality = low` AND `error_cost = low` | **PROCEED** |
| 7 | Default when unsure between ASSUME and ASK | **ASK** one blocking question rather than silent guess |

**Green path:** Rule 6 — detection runs, receipt may be one line, no interrogation.

---

## 8. Interaction with existing Scan ASK

Scan Phase 4 **LOW** already requires ASK with 2–3 mode/style readings.

Problem-Formation **extends** that:

| Scan says | Detection adds |
|-----------|----------------|
| LOW → ask mode/topic | Also slot/fork/cost → may add success/scope questions |
| HIGH → proceed | Still run error_cost; CONFIRM if high-impact act |
| MEDIUM → name runner-up | May ASSUME or single ASK if fork medium |

Do **not** double-interrogate: merge questions into **≤3 total** ranked.

---

## 9. Detection receipt (machine-friendly)

```text
DETECTION
- scan_confidence: HIGH|MEDIUM|LOW
- tuple_depth: surface|working|exhaustive
- slot_fill: { goal, success, scope, constraints }
- fork_materiality: low|medium|high
- error_cost: low|medium|high
- ambiguity_severity: low|medium|high
- path_bias: PROCEED|ASSUME|ASK|REFRAME|CONFIRM
- notes: one line
```

Feeds `PROBLEM_FORMATION.why_path` and path select (Fold 3 of proc_clarify-reframe).

---

## 10. Acceptance tests

| # | Scenario | Expected path bias |
|---|----------|-------------------|
| D1 | “What is 2+2?” | PROCEED |
| D2 | “Look into Mapua” (vague, no success) | ASK or REFRAME |
| D3 | “Write Core card on X” + thin brief | ASK or CONFIRM-leaning |
| D4 | “Polish this paragraph, keep meaning” | PROCEED or ASSUME |
| D5 | Two modes equally plausible in Scan | ASK (aligns Scan LOW) |
| D6 | Exhaustive depth + missing success test | ASK not silent ASSUME |

---

## 11. Non-goals

- No second neural “judge model” required for v0.2  
- No replacement of cue lexicon or Scan phases  
- No severity theater on every factual ping  

---

**End of detection layer.**
