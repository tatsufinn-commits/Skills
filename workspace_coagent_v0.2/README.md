# Co-Agent extension: Workspace & GitHub (v0.2)

**Not a separate skill.** Extends `@coagent` with parallel branches, meeting room, magic-word fields, and GitHub binding.

## Contents

| Path | Role |
|------|------|
| `extension/COAGENT_EXTENSION_WORKSPACE.md` | Overview |
| `extension/MAGIC_WORDS_COAGENT.md` | Updated console |
| `extension/BRANCH_TEAM_PROTOCOL.md` | Parallel branches / worktrees |
| `GROUND_RULES.md` | Planes & non-negotiables |
| `MEETING_PROTOCOL.md` | Formatted meeting rules |
| `github/GITHUB_WORKSPACE.md` | Repo binding |
| `templates/00_–04_*.md` | Numbered room files |
| `scripts/init_meeting.sh` | Create room |
| `scripts/append_turn.py` | Append headed turn |

## Magic words (arrival)

```text
@[MODE] | STYLE: [AUTO] | TOPIC: [task]
| Co-Agent: yes | N: 2 | Workspace: yes
| Workspace-Repo: owner/skills | Meeting: 2026-09-29-pilot
| Configuration State: truth-stress
```

## Parallel team

Each seat: `coagent/<Meeting>/LEAD` or `…/A1-<codename>` — same time, isolated trees.

## Put this on

`skills` repo (recommended), not FIX-owned RADIATION main.
