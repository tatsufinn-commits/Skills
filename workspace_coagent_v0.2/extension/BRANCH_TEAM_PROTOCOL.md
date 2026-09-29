# Branch team protocol — parallel Co-Agent

**Extension to:** `@coagent` identity & routing  

---

## 1. Parallel model

| Seat | Branch | Worktree (recommended) |
|------|--------|------------------------|
| LEAD | `coagent/<ID>/LEAD` | `../wt-<ID>-LEAD` |
| A1 | `coagent/<ID>/A1-<code>` | `../wt-<ID>-A1` |
| A2 | … | … |

Agents **do not** share one working directory for concurrent edits.

```bash
# example from Workspace-Repo root
git worktree add ../wt-MEET-LEAD -b coagent/MEET/LEAD
git worktree add ../wt-MEET-A1   -b coagent/MEET/A1-DESK
```

---

## 2. What each seat may write

| Path | Who writes |
|------|------------|
| `workspace/meetings/<ID>/02_MESSAGES.md` | Any seat **append only** (or carrier) |
| `workspace/meetings/<ID>/01_ROSTER.md` | LEAD (bootstrap); seats ack only |
| `workspace/meetings/<ID>/03_DECISIONS.md` | LEAD or designated |
| `workspace/meetings/<ID>/04_OUTCOME.md` | LEAD only |
| Seat task files under branch tree | **That seat only** |
| RADIATION `main` / FIX branches | **Nobody** from this meeting without Commander lane |

*Path note (TSSTM v0.2.1 fix): filenames are the numbered room files produced by `init_meeting.sh` (`01_ROSTER.md` … `04_OUTCOME.md`); earlier revisions of this table cited unnumbered names.*

---

## 3. Same-time loop

```text
1. Bootstrap roster + branches
2. Isolate: each seat commits to own branch (blind)
3. Exchange: append MESSAGES.md; pull often
4. LETTER: TO: seat in header; carrier or git
5. Merge: LEAD synthesizes on merge branch / OUTCOME.md
6. Commander seal → close meeting → optional PR to skills main
```

---

## 4. DESK ↔ FIX visibility

- DESK **may read** FIX/RADIATION state for context  
- DESK **may not** commit to FIX-owned branches unless Commander opens a lane  
- Note in MEETING.md: `FIX_READ: allowed | FORBIDDEN_WRITE`

---

## 5. Conflict handling

- Prefer append-only meeting files  
- Seat code conflicts → fix on seat branch, not by editing another seat’s branch  
- LEAD resolves product conflicts in OUTCOME / merge branch  

---

**End branch team protocol.**
