# `proc_clarify-reframe` — Problem-Formation Scaffold

**Version:** 0.2.0  
**Use when:** Detection `path_bias` ≠ PROCEED (or Commander invokes `@clarify`)  
**Prerequisite:** `scaffolding/DETECTION.md` fields filled (or Scan + slot pass)  
**Fadeability:** Receipt may remain in short_term / TID intake; deliverables carry no scaffold residue.

---

## Fold 0 — Ingest detection (always)

Copy into working context: `scan_confidence`, `tuple_depth`, `slot_fill`, `fork_materiality`, `error_cost`, `ambiguity_severity`, `path_bias`.

If Detection missing, run minimal slot_fill + fork + error_cost from prompt before Fold 1.

---

## Fold 1 — Detect gaps

Checklist (evidence per item: present / missing / ambiguous):

1. **Goal** — what done looks like  
2. **Success test** — how we know it’s done  
3. **Scope** — in / out  
4. **Constraints** — time, format, tools, sources, budget  
5. **Audience / stakes** — who consumes; reversible vs irreversible  
6. **Interpretation fork** — would alt readings change the work product?

Exit: `gaps[]` list.

---

## Fold 2 — Known / Assumed / Unknown

| Bucket | Content |
|--------|---------|
| Known | Explicit in Commander text or sealed prior TID |
| Assumed | Inferred; must be listed if used |
| Unknown | Blocking or non-blocking |

Exit: three lists. No silent promotion of Assumed → Known.

---

## Fold 3 — Path select

1. Start from Detection `path_bias` (authoritative default).  
2. Adjust only if Fold 1–2 revealed new facts (e.g. gap closed mid-scaffold).  
3. Apply `DETECTION.md` §7 top-down rules if bias was provisional.  
4. Record **why** in one line: severity + fork + error_cost (value-of-information).  

Override hierarchy: Commander explicit path > Detection policy > heuristic guess.

---

## Fold 4 — Act

### If ASK

- Emit **≤3** questions  
- Rank by **blocking power** (which answer splits the work most)  
- Prefer concrete options when possible  
- Stop condition: answers received or Commander overrides  

### If REFRAME

- Write **reframed_task** (single sharp paragraph)  
- List **assumptions**  
- Preserve original ask verbatim in receipt  
- Mark `WAITING_COMMANDER` unless standing order allows sealed reframe  

### If ASSUME

- Assumptions block (bullets)  
- Continue; do not pretend gaps were stated by Commander  

### If CONFIRM

- State intended action, impact, rollback if any  
- Wait for seal  

---

## Fold 5 — Receipt + hand-off

Emit `PROBLEM_FORMATION` (see skill card).  
Status → neuron PLAN only when `SEALED` / `PROCEED` / allowed ASSUME.

---

## Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| Five open essay questions | Cap 3; rank |
| Reframe that swaps goal quietly | Assumptions + original preserved |
| “Any preference?” filler | Only material forks |
| Gate on every factual lookup | PROCEED green path |
