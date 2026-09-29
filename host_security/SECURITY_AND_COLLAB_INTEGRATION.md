# Security + collab integration map

**Version:** 0.1.0  
**Packages:** host_security · clarify v0.2 · collab_orchestration v0.1+  

---

## Pipeline (full)

```text
1. Magic words / boot (public grammar — no ARM field)
2. Host arming check (private Commander context only)
      unarmed → apply public/UNARMED_CAPABILITIES.md → dry line → STOP
      armed   → continue
3. Autonomous Scan (existing)
4. Problem-Formation Detection + clarify (v0.2)
5. Agency detection → maybe arm collab orchestration
6. Skills / Research / @educate / workers under LEAD
7. Single Commander voice
```

---

## What lives where

| Artifact | Location |
|----------|----------|
| Host mark | **Never** public repo; private bootstrap only |
| `HOST_ARMING_PUBLIC.md` | Safe to discuss / optional public docs |
| `COMMANDER_PRIVATE_BOOTSTRAP.md` | Copy offline; **do not commit** |
| `AGENCY_DETECTION.md` | Collab upgrade; archive until Patch |
| Style + cues | Recognition prior only |

---

## Upgrades included (collab)

1. **Agency detection** — arms collab on agentic/multi-role task shape  
2–7. Deferred to usage (prompt insert, charter templates, etc.) per prior verdict  

---

## Commander terms (locked)

- No `ARM:` in published magic words  
- No host mark in repository  
- Mark = Commander memory / private host config only  
- Style + cue ≠ unlock  

---

**End integration map.**


Hardening: see `hardening/HARDENING_ADDENDUM.md` (private pack, private bootstrap, checklist, mark hygiene).
