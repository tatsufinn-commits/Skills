# Problem-Formation / `@clarify` package v0.2

**Always-on intake gate** for insufficient or unclear tasks + optional explicit skill pull.  
**v0.2:** Detection layer — severity before path select (consumes Autonomous Scan).

## Why

Research: LLMs often **recognize** ambiguity but **answer anyway** (“knowing but not showing”).  
Optional skills fail under that bias. This package makes clarify/reframe **compliance with a green pass**.

## Contents

| Path | Role |
|------|------|
| `CLARIFY_SUBSKILL_CARD.md` | Gate law + optional `@clarify` |
| `scaffolding/DETECTION.md` | **v0.2** severity: slots, fork, error_cost → path bias |
| `scaffolding/PROC_CLARIFY_REFRAME.md` | Folds when path ≠ PROCEED |
| `evidence/EVIDENCE_APPENDIX.md` | Literature / provider backing |
| `schemas/problem_formation_receipt.json` | Receipt schema |
| `problem_formation_receipt.py` | Template + validator + severity helpers |

## Paths

`PROCEED` · `ASSUME` · `ASK` (≤3) · `REFRAME` · `CONFIRM`

## Detection (v0.2)

Consumes Scan confidence + DEPTH; adds:

- slot_fill (goal / success / scope / constraints)
- fork_materiality (low / medium / high)
- error_cost (low / medium / high)
- ambiguity_severity → path_bias

See `scaffolding/DETECTION.md`.

## Quick test

```bash
python problem_formation_receipt.py --demo proceed
python problem_formation_receipt.py --demo ask --ask "do the mapua thing"
python problem_formation_receipt.py --demo ask --json
```

## Port (when authorized)

1. Intake doctrine pointer (cue / rules annex)  
2. Detection fields on Scan Declaration or neuron intake  
3. `proc_clarify-reframe` toward core via improved/  
4. Optional `subskills/active/clarify.md`  
5. Single-purpose Patch — not merged into `@educate`  

## Related

- `@educate` — topic depth **after** ask is sharp  
- Origami — incapability **after** clear task still fails  
- Neurons — live TID pipeline; this gate feeds `NEEDS_CLARIFY` with real process  
