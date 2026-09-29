# Host security hardening addendum

**Version:** 0.1.0  
**Parent:** host_security v0.1 → v0.2  
**Date:** 2026-09-28  
**Goal:** Make unarmed sessions **harder** to fully open — not claim cryptographic airtightness  

---

## 1. Reality check

| Claim | Truth |
|-------|--------|
| Prompt refuse = vault | **False** |
| Public repo unreadable | **False** if public |
| Unarmed can be *behavioral-capped* | **True** with private policy + private pack + checklist |
| Style + cues = unlock | **False** (recognition only) |

Hardening = **cost and default-lock**, not impossibility of jailbreak or clone.

---

## 2. Hardening controls (ordered)

### H1 — Private Commander pack (highest leverage)

Keep **off public git**:

- Personal Brain, real calendar/ICS paths, readiness, private lexicon edges  
- Filled private bootstrap with host mark  
- Any file that makes *your* house uniquely runnable  

Public tree = method. Private pack = *you*.

### H2 — Private host bootstrap on every daily host

Arena / Claude / GPT / local **custom instructions** (outside repo) contain:

- Unarmed → dry line + obey `UNARMED_CAPABILITIES`  
- Armed only when mark present in **that** private context  
- No unlock tutorial  

Strangers with only GitHub never load this.

### H3 — Behavioral checklist

Obey `public/UNARMED_CAPABILITIES.md` as a **forbidden list**, not a suggestion.

### H4 — Public surface minimization

- Magic words without arming field  
- Optional one dry public line (`HOST_ARMING_PUBLIC.md`)  
- Avoid one-paste “full OS boot kit” in README  

### H5 — Mark hygiene

- Random API-style mark only (no PII)  
- Never in git, issues, or public samples  
- Rotate if exposed in chat/screenshot  

### H6 — Optional second factor (still soft)

Short rotating session nonce in private notes — not published. Raises cost after one leak.

### H7 — Real airtight (only if required)

Private repo/submodule for personal data; or server-side agent that checks a key **before** injecting system context. Prompt-only cannot match this.

---

## 3. “Guardrails remain locked if unarmed”

**Locked** means all of:

1. Private refuse policy loaded on Commander’s hosts (H2)  
2. Private pack not in the clone (H1)  
3. Forbidden checklist applied (H3 / UNARMED_CAPABILITIES)  
4. No mark in repository (Commander terms)  
5. Unarmed never proceeds to full clarify theater, collab fan-out, or personal Brain  

**Not guaranteed:** random third-party model with full public tree pasted in, under adversarial jailbreak.

---

## 4. Pipeline with hardening

```text
Invoke RADIATION / magic words
  → Host arm present in private context?
       NO  → UNARMED checklist → dry line → STOP
       YES → Scan → Clarify → Agency/collab? → skills
```

---

## 5. Desk / Architect notes

- Safe to place `UNARMED_CAPABILITIES.md` and `HOST_ARMING_PUBLIC.md` in public docs if Commander drops them  
- **Reject** commits of filled private bootstrap or live marks  
- Hardening addendum is operational guidance; not a claim that main is sealed against clone  

---

**End hardening addendum.**
