# Horizon Scaffolding — Ordered Folds for `@educate`

**Version:** 0.1.0  
**Constitutional idea:** Scaffolding shapes the *work*; styles shape the *deliverable*. This scaffold detaches; the Horizon Pack remains.

---

## Neuron gate (optional, when capability state exists)

```text
IF topic requires external sources AND capability says search/fetch UNAVAILABLE
  → residual BLOCKED; still emit parametric activation section labeled INFERRED/parametric only
ELSE
  → proceed folds
```

---

## Fold 1 — Seed

**Obligation:**  
- Bind **topic X**  
- Bind **use-case** (why depth is needed: exam, design decision, lecture, patch, etc.)  
- Bound scope (what is *out*): reject pure “everything forever”  
- Record success criterion in one sentence  

**Exit:** Seed block written.

---

## Fold 2 — Core

**Obligation:**  
- Canonical definitions, mechanisms, primary framings of X  
- Prefer primary/official sources when domain-bound  
- Grade every claim  
- CTP: residence in sources, not model riff  

**Exit:** `core[]` non-empty or residual why empty.

---

## Fold 3 — Necessary

**Obligation:**  
- Prerequisites and dependencies required to **use** X under the use-case  
- Procedural floor (how-to elements) when use-case is operational  
- Depth bias: prefer D2-style application over more D1 trivia  

**Exit:** `necessary[]` or explicit “none required for use-case.”

---

## Fold 4 — Adjacent / Akin

**Obligation:**  
- Near-neighbors, contrasts, sister topics (quota: default 3–7, configurable)  
- Each adjacent item: relation tag (contrast | dependency | application | debate) + graded claims  
- Do not invent neighbors; if search finds none, residual  

**Exit:** `adjacent[]` and/or residual.

---

## Fold 5 — Integrate

**Obligation:**  
- Explicit multi-hop links among core / necessary / adjacent  
- Counters “great memory, shallow reasoning”: force combination, not parallel lists  
- Conflicts logged side-by-side  

**Exit:** `integrations[]` (may be empty only if single-fold topic with residual).

---

## Fold 6 — Gaps

**Obligation:**  
- Missing, blocked, unused-but-hinted knowledge  
- Hypotheses **UNVERIFIED** only  
- `next_acquisition` list for Commander or later `@educate gap-fill`  

**Exit:** `residuals` + `hypotheses` honest.

---

## Fold 7 — Pack

**Obligation:**  
- Emit Horizon Pack (md + optional json)  
- `status`: ADEQUATE | PARTIAL | BLOCKED  
- `stop_reason` required  
- No scaffold residue in final Commander-facing prose beyond the pack structure  

**Exit:** Pack delivered; scaffold may file to short_term working papers.

---

## Stop criteria (normative)

Stop when **any** holds:

1. **Use-case met** — seed success criterion satisfied with graded support  
2. **Quota met** — core + necessary filled; adjacent quota hit or honestly residual  
3. **Commander halt**  
4. **Blocked** — critical sources inaccessible; pack PARTIAL/BLOCKED  

Do **not** stop because the model produced a fluent summary.

---

## Anti-patterns

| Anti-pattern | Correction |
|--------------|------------|
| One long essay | Force fold sections in pack |
| Ten adjacent trivia facts | Prefer fewer, linked, use-case-relevant |
| “As an AI I know…” | Source or label parametric |
| Rerun forever | stop_reason mandatory |
