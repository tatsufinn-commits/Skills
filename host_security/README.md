# Host security pack v0.2

Soft host-arming + unarmed behavioral lock + agency/collab upgrade.
**No live host mark is stored in this pack.**

## Layout

| Path | Sensitivity |
|------|-------------|
| `public/HOST_ARMING_PUBLIC.md` | Public-safe one-liner doctrine |
| `public/UNARMED_CAPABILITIES.md` | **v0.2** Forbidden/allowed checklist when unarmed |
| `hardening/HARDENING_ADDENDUM.md` | **v0.2** How to make unarmed harder to open |
| `private_template/COMMANDER_PRIVATE_BOOTSTRAP.md` | **Do not commit filled** — copy offline |
| `collab_upgrade/AGENCY_DETECTION.md` | Task-shape detection → arm collab |
| `SECURITY_AND_COLLAB_INTEGRATION.md` | Pipeline map |

## Commander terms (locked)

- No `ARM:` in published magic words
- No host mark in the repository
- Style + cues = recognition only
- Unarmed = checklist lock, not vibes

## Pipeline

```text
Magic words → private arm check → UNARMED stop OR armed Scan → Clarify → Agency/collab → skills
```

## Related archive

- clarify_subskill v0.2
- collab_orchestration v0.1
- educate / mapua / radiation_bots as separate packs
