# Identity & Routing (Co-Agent substrate)

**Version:** 0.2.0  
**Parent:** `@coagent`  
**Purpose:** Stop multi-Arena / multi-provider tab soup. Every message is addressable.

---

## 1. Seats

| Seat | Meaning |
|------|---------|
| **LEAD** | Superior AI — single voice to Commander |
| **A1 … A4** | Co-agent seats (max 4 under LEAD) |

Seat IDs are **fixed for the run**. Roles may change; seats do not vanish mid-run without LEAD record.

---

## 2. Code names

- Each seat chooses a **short unique callsign** at bootstrap (DESK pattern).  
- Same provider, two panes → **different** code names required.  
- Code name ≠ authority. Authority = seat + LEAD + Commander.  
- Roster freezes after bootstrap unless LEAD logs a rename.

**Roster line (carrier keeps this visible):**

```text
LEAD = <codename> (<provider/pane>) role=primary
A1   = <codename> (...) role=...
A2   = ...
```

---

## 3. Message header (mandatory)

```text
[FROM: <codename> | SEAT: LEAD|A1|A2|A3|A4 | ROLE: <role>]
[TO:   <codename|SEAT|BROADCAST>]
[PHASE: bootstrap|isolate|diff|pipeline|letter|delegate|merge|seal]
[TYPE: ANSWER|ATTACK|CONCEDE|HOLD|DELEGATE|REPORT|LETTER]
```

**Carrier rule:** Do not paste body-only messages. No header → no relay.

---

## 4. Routing modes

### PIPELINE (default for structured phases)

```text
LEAD → A1 → A2 → A3 → A4 → LEAD
```

Use for: isolate collection, ordered critique, final return to LEAD.

### LETTER (targeted)

- After roster exists  
- `TO:` one seat (preferred) or small set  
- Allowed when scenario enables LETTER  
- **Forbidden during pure isolate** (Fold 2)  
- Prefer over BROADCAST spam  

Role path example (scenario-defined):

```text
A1(researcher) → A3(fact-checker) → A2 → LEAD
```

---

## 5. Delegation

| Who | May delegate mission work |
|-----|---------------------------|
| Commander | Always |
| LEAD | Yes, inside scenario |
| A1–A4 | Only peer **checks** if scenario allows — not mission reassignment |

```text
[FROM: LEAD][TO: <seat>][TYPE: DELEGATE][PHASE: delegate]
TASK: …
SUCCESS: …
CONSTRAINTS: …
RETURN_TO: LEAD
```

---

## 6. Bootstrap sequence

1. Commander: Co-Agent yes + N + scenario (or minimal)  
2. LEAD states goal + seats  
3. Each seat: `CODENAME` + role ack  
4. Carrier posts roster  
5. Proceed Fold 2 isolate  

---

## 7. Anti-soup rules

- Max **one** active LETTER thread per carrier focus (mitigate paste load)  
- Collision of code names → LEAD assigns suffix (`DESK-2`)  
- Provider field on roster for same-model panes  

---

**End identity & routing.**
