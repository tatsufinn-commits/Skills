# Carrier templates (silent paste)

Copy blocks. Do not add coaching text.

---

## Bootstrap (LEAD posts first)

```text
[FROM: LEAD | SEAT: LEAD | ROLE: primary]
[TO: BROADCAST]
[PHASE: bootstrap]
[TYPE: ANSWER]

SCENARIO: <id or minimal>
GOAL: …
SUCCESS: …
N: …
STATE: truth-stress|council|adversarial
LETTER: on|off

Seats: LEAD, A1[, A2, A3, A4]
Reply with: CODENAME + role ack only.
```

---

## Code name ack (each seat)

```text
[FROM: <you> | SEAT: A1 | ROLE: <role>]
[TO: LEAD]
[PHASE: bootstrap]
[TYPE: REPORT]

CODENAME: <short>
ROLE_ACK: <role>
PROVIDER_PANE: <e.g. Arena-tab / Grok>
```

---

## Isolate

```text
[FROM: <codename> | SEAT: … | ROLE: …]
[TO: LEAD]
[PHASE: isolate]
[TYPE: ANSWER]

ANSWER:
REASONING:
EVIDENCE:
CONFIDENCE:
WOULD_CHANGE_MIND:
```

---

## LETTER

```text
[FROM: <codename> | SEAT: … | ROLE: …]
[TO: <codename or SEAT>]
[PHASE: letter]
[TYPE: LETTER]

RE: …
CLAIM/QUESTION:
EVIDENCE:
ASK:
```

---

## DELEGATE (LEAD)

```text
[FROM: LEAD | SEAT: LEAD | ROLE: primary]
[TO: <seat>]
[PHASE: delegate]
[TYPE: DELEGATE]

TASK:
SUCCESS:
CONSTRAINTS:
RETURN_TO: LEAD
```

---

## ATTACK / HOLD (debate)

```text
[FROM: …]
[TO: …]
[PHASE: pipeline|letter]
[TYPE: ATTACK|HOLD|CONCEDE]

TARGET_CLAIM:
EVIDENCE:
CONCEDE: yes/no
HOLD_REASON: (if hold)
```

---

## MERGE package (LEAD → Commander)

```text
[FROM: LEAD | SEAT: LEAD | ROLE: primary]
[TO: COMMANDER]
[PHASE: merge]
[TYPE: REPORT]

OUTCOME: MERGED|STRUCTURED_DISAGREEMENT|DUAL_CONFIRM
BEST_SUPPORTED:
RESIDUALS:
ROSTER: …
DIFF_SUMMARY:
SEAL: PENDING
```

---

**End templates.**
