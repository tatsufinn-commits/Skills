# Co-Agent extension: Workspace & GitHub carrier

**Kind:** Extension to `@coagent` (not a separate skill)  
**Version:** 0.2.0  
**Parent:** `@coagent` v0.2 (identity · scenario · `proc_coagent-debate`)  
**Date:** 2026-09-29  

---

## What this extension adds

| Capability | Meaning |
|------------|---------|
| **Git-carrier runtime** | Seats work on **task branches** in a Commander-owned repo (e.g. `skills` or a meeting repo) |
| **Parallel team** | LEAD + A1–A4 run **at the same time** on isolated branches / worktrees |
| **Workspace meeting room** | Shared markdown for roster, messages, decisions, outcome |
| **Magic-word fields** | Console flags for Co-Agent arrival + workspace binding |
| **Plane safety** | Design/skills plane ≠ FIX/RADIATION `main` without Patch |

Chat-carrier (Commander paste) remains valid. This extension adds **repo-native** parallel execution.

---

## Theory (operational)

```text
Commander opens Co-Agent + Workspace
  → roster + scenario
  → each seat gets branch: coagent/<meeting-id>/<seat|-codename>
  → seats work in parallel (worktree or separate clone)
  → exchange via MESSAGES.md (append) + optional LETTER
  → LEAD merges package → OUTCOME
  → Commander seals
  → polished result → PR/Patch to RADIATION when FIX allows
```

**Same time** = parallel branches, not one WD fighting over files.

---

## Non-goals

- Not a second skill name in SKILLS.md  
- Not peer government  
- Not auto-write to FIX-owned RADIATION branches  
- Not CRDT multiplayer (git near-real-time is enough)  

---

**End extension overview.**
