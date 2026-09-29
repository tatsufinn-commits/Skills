# Magic words — Co-Agent + Workspace (extension)

**Public grammar:** no `ARM:` field (host arming stays private).

---

## Full console (Co-Agent arrival)

```text
@[MODE] | STYLE: [style|AUTO] | TOPIC: [task]
| Co-Agent: yes
| N: 1|2|3|4
| Challengers: [optional short list]
| Configuration State: truth-stress|council|adversarial
| Scenario: [id or none]
| Workspace: yes
| Workspace-Repo: [github.com/org/skills or owner/repo]
| Meeting: [MEETING_ID]
```

| Field | Default | Notes |
|-------|---------|--------|
| `Co-Agent` | no | Must be **yes** to arm |
| `N` | 1 | Seats under LEAD (max 4) |
| `Configuration State` | truth-stress | If Co-Agent yes and omitted |
| `Workspace` | no | **yes** → git-carrier + meeting room |
| `Workspace-Repo` | standing order / skills repo | Where branches + workspace live |
| `Meeting` | auto from date+topic slug | Folder under `workspace/meetings/` |

---

## Minimal arrival

```text
@Autopilot | STYLE: [AUTO] | TOPIC: [task]
| Co-Agent: yes | N: 2 | Workspace: yes | Meeting: 2026-09-29-pilot
```

---

## Autopilot resolution (unspecified fields)

| Omitted | Resolution |
|---------|------------|
| Co-Agent | **no** (do not invent) |
| Workspace | **no** if Co-Agent no; if Co-Agent yes may default **yes** only under standing order |
| N | 1 |
| Meeting | LEAD proposes id; Commander confirms if unset |
| Challengers | ASK or standing default — do not invent providers |

---

## Branch naming (when Workspace: yes)

```text
coagent/<MEETING_ID>/LEAD
coagent/<MEETING_ID>/A1-<codename>
coagent/<MEETING_ID>/A2-<codename>
…
```

Optional integration branch:

```text
coagent/<MEETING_ID>/merge
```

LEAD opens PR from `merge` (or stacks seat PRs) for Commander seal — **not** direct push to RADIATION `main` under FIX.

---

**End magic words.**
