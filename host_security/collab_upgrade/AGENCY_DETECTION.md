# Agency detection (collab_orchestration upgrade)

**Version:** 0.1.0  
**Parent:** `proc_collab-orchestration`  
**Depends on:** Problem-Formation / `@clarify` first; host arming for full personal depth  

---

## Purpose

Detect whether the session needs **collaboration orchestration** (lead/worker discipline), without fingerprinting a vendor (“Arena”) as a hard requirement.

**Detect task/agency shape**, not platform.

---

## Agency posture

| Value | Meaning |
|-------|---------|
| `chat` | Single-turn or simple Q&A; no multi-step tool loop expected |
| `agentic` | Multi-step plan, tools, sandbox, iterate-to-deliverable |
| `multi-role` | Explicit lead/helpers or parallel specialist angles |

---

## Signals (any strong pair → consider arming collab)

**Explicit**

- User names Agent Mode / agentic workflow / lead+workers  
- Magic-word modes that imply full multi-skill chains (`@Autopilot`, full `@Radiation`, etc.) when paired with multi-stage verbs  

**Task shape**

- Multi-stage deliverable (research → build → test / report)  
- Parallel independent angles  
- Code + files + search in one job  
- “Build / debug / deep research / multi-step” without a single factual answer  

**Not enough alone**

- Single definition question  
- Pure style preference  
- Battle/side-by-side comparison requests  

---

## Policy

```text
AFTER clarify path is PROCEED | sealed ASSUME | resolved ASK:

  IF agency_posture in {agentic, multi-role}
     AND complexity ≥ threshold (multi-step or parallel subjobs)
     → ARM proc_collab-orchestration
  ELSE
     → skip collab scaffold
```

**Host arming:**

- Unarmed (no private host mark in Commander context): collab scaffold may still apply **generic** lead/merge discipline for method-only work, but **no** personal Brain / Commander-only depth.  
- Full personal OS force requires host arm per public host-arming note + private bootstrap.

---

## Output

```text
AGENCY
- posture: chat | agentic | multi-role
- collab_armed: true | false
- notes: one line
```

Feeds Fold 0+ of `proc_collab-orchestration`.

---

## Acceptance

| Case | collab_armed |
|------|----------------|
| “What is 2+2?” | false |
| “Deep research X then build a site in sandbox” | true |
| “Lead research, critic, formatter on Y” | true |
| Magic words + one-line fact | false |

---

**End agency detection.**
