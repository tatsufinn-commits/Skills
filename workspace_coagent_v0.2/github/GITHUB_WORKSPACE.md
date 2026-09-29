# GitHub workspace binding

**Extension:** Co-Agent Workspace v0.2  

---

## Recommended repo

Commander-owned **`skills`** (or dedicated `coagent-meetings`) — **not** RADIATION while FIX owns main.

```text
skills/
  workspace/                 # this extension lives here
  meetings/                  # or workspace/meetings/
  <skill packs in polish>/
```

---

## GitHub flow

1. Create meeting folder + templates on `main` or `workspace/main`  
2. Open per-seat branches from that commit  
3. Optional: GitHub **Issue** per meeting (`Meeting: <ID>`) for human visibility  
4. Optional: Draft **PR** `coagent/<ID>/merge` → `main` for LEAD outcome only  
5. Protect `main` with review; seats never force-push each other’s branches  

---

## Actions for agents (when they have gh/git)

```bash
git fetch && git checkout coagent/<ID>/A1-<code>
# … work …
git add -p && git commit -m "coagent(<ID>): A1 <codename> <phase>"
git push -u origin HEAD
# append message via PR comment OR commit to 02_MESSAGES.md on a messages branch
```

If only one shared `02_MESSAGES.md` on a coordination branch:

- use **short commits**, pull --rebase, avoid rewriting history  

---

## Commander without agent git

Paste turns into `02_MESSAGES.md` and push yourself — still valid carrier.

---

**End GitHub binding.**
