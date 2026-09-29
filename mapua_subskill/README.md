# `@mapua` subskill package v0.1

Mapúa domain acquisition playbook for RADIATION — **archive skeleton**, not live canon.

## Contents

| Path | Role |
|------|------|
| `MAPUA_SUBSKILL_CARD.md` | Full skill card (MISSION → acceptance tests) |
| `playbook/OFFICIAL_HOSTS.md` | Preferred hosts (Commander-editable) |
| `playbook/EXIT_EXAM_HUNT.md` | Off-ICS exam hunt procedure |
| `playbook/PROF_HUNT.md` | Public faculty footprint procedure |
| `mapua_pack.py` | Pack template + validator (no scraper) |

## Quick test

```bash
python mapua_pack.py exit-exam --query "AR173 exit exam 2026" --json
python mapua_pack.py prof --query "AR153P instructor"
```

## Doctrine reminders

- Empty ICS ≠ no exam  
- Hypotheses labeled UNVERIFIED only  
- Secondary social/Reddit never silent-Core  
- One superior AI runs the skill; this package is playbook + schema help  

## Port to main (when authorized)

1. `subskills/active/mapua.md` from the skill card  
2. Optional `scripts/mapua_pack.py`  
3. TOOL_REGISTRY if scripted  
4. Single-purpose Patch — do not merge into Housekeeper or Calendar bots  
