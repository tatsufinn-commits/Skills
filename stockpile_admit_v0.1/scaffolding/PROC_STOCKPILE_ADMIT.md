# `proc_stockpile-admit` v0.1

**Skill:** `@stockpile` / `@admit`  
**Goal:** Executable admission decisions + receipt  

---

## Fold 0 — Gate

- Explicit `@stockpile` / `@admit` or Commander “admit these”  
- If claims are foggy → clarify atoms first  
- Load evidence taxonomy + triangulation rules in force  

---

## Fold 1 — Inventory

- Split into **atomic claims** (one proposition each)  
- Tag origin: session / research / coagent / user-supplied  

---

## Fold 2 — Grade

- For each claim: assign taxonomy grades available  
- Mark missing grade fields as incomplete (blocks ADMIT to high tiers)  

---

## Fold 3 — Triangulate

- Count independent sources  
- Flag same-root retellings as **one voice**  
- Apply house rule: Core / long-term elevation needs triangulation elevator  

---

## Fold 4 — Conflict scan

- Compare to Brain / prior receipts if in context  
- Outcomes: none | soft tension | hard contradiction  

---

## Fold 5 — Decide (per claim)

| Decision | When |
|----------|------|
| ADMIT | Grades complete enough + triangulation satisfied for target tier |
| QUARANTINE | Useful, insufficient independence or incomplete grades |
| REJECT | Contamination, fabrication risk, or fails zero-contamination |
| DECAY-PROPOSE | Hard contradiction with stored item + stronger new support |

---

## Fold 6 — Receipt

Emit `ADMIT_RUN` block.  
No silent Core edit — hand off to Nota / Commander Patch path.

---

## Fold 7 — Seal

Commander accepts decisions or overrides.

---

**End scaffold.**
