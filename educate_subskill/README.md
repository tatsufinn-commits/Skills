# `@educate` — Horizon Expansion package v0.1

**Archive / design-of-record** for RADIATION. Not live canon until Patch.

## Problem

LLMs often provide **coverage without depth**. Research (shallow learning from LLM summaries; unused latent knowledge; weak multi-hop integration) and industry Deep Research products both support a dedicated **depth mandate**.

## Contents

| Path | Role |
|------|------|
| `EDUCATE_SUBSKILL_CARD.md` | Full skill card |
| `scaffolding/HORIZON_FOLDS.md` | Seed → Pack ordered folds + stop criteria |
| `evidence/EVIDENCE_APPENDIX.md` | Literature / industry backing |
| `schemas/horizon_pack_template.json` | Empty pack schema |
| `horizon_pack.py` | Template + validator (no research engine) |

## Quick test

```bash
python horizon_pack.py --topic "exit exams off ICS" --use-case "Mapua term planning"
python horizon_pack.py --topic "test" --json
```

## Magic words

- Educate yourself on …
- Widen the horizon on …
- Go deep on …
- `@educate` / `/educate` + topic

## Doctrine

- One superior AI; this is a skill + scaffold, not a swarm  
- CTP against volume tourism  
- Hypotheses UNVERIFIED only  
- Stop on use-case / quota / halt / blocked — not on fluency  

## Port (when authorized)

1. `subskills/active/educate.md`  
2. `scaffolding/` horizon proc  
3. Optional `scripts/horizon_pack.py`  
4. Single-purpose Patch — compose with Research, do not replace it  
