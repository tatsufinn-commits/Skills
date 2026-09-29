# `@mapua` — Mapúa Domain Acquisition Subskill

**Class:** Active subskill (domain playbook)  
**Version:** 0.1.0 (archive / design-of-record)  
**Date:** 2026-09-24  
**Status:** Prepared for future Patch — **not** on RADIATION main until Commander/DESK authorize  
**Parents:** scout · @fetch · Research · Annotate · Triangulate · (future @social for public post URLs)  
**Doctrine:** One superior AI + many skills. `@mapua` does not invent institutional facts. Hypothesis = residual / incubate, never silent Core truth.

---

## MISSION

When the topic is **Mapúa** (institution, course codes, exams beyond ICS, public faculty footprint, student organizations, campus services), run a **bounded acquisition and packaging playbook**: prefer official and course-bound sources, then graded public secondary (web, Reddit, public social). Emit a short dossier block with **evidence grades and residuals**.

**Special pressure:** many exams (including exit-style assessments) **do not appear on Blackboard ICS** — calendar bots alone are insufficient; `@mapua` must hunt official + public secondary channels and **admit gaps**.

---

## TRIGGERS

Activate when Commander intent matches any of:

- Mapúa / MU / Mapua University campus or policy questions  
- Course code lookup (e.g. AR173, GED103, MEC30)  
- Exit exam / departmental exam / assessment details **not** on ICS  
- Professor / instructor public information tied to a course code  
- Student organization (public) information  
- “What does Mapúa say about X?” / official vs rumor sorting  

**Silent skip:** pure non-Mapúa general knowledge with no campus angle.

---

## ACTIONS

| Action | Input | Behavior |
|--------|--------|----------|
| `course-pack` | `<CODE>` | Official/course-bound links, Brain/courses hits, assessment pattern if sourced; residual if thin |
| `exit-exam` | `[CODE] [term]` | Multi-source hunt for exam rules/dates/requirements (**ICS is optional bonus only**) |
| `prof` | `<CODE> [name]` | Public footprint: official role if found + Reddit/web secondary; graded anecdotes |
| `org` | `<name or query>` | Public student org pages/posts only |
| `official-search` | `<query>` | Allowlisted / official-first web acquisition plan + results package |
| `secondary-scan` | `<query>` | Reddit/public web/social **secondary**; every claim graded |
| `gap-expand` | `<prior pack id or query>` | When findings thin: **widen search plan** + list hypotheses as **unverified** — do not fabricate dates/rules |

### Exit-exam hunt order (normative)

1. Official Mapúa / college / program pages and PDFs  
2. Commander-supplied or External_Sources LMS text  
3. Public web (site: and general search)  
4. Reddit / forums / public social (secondary)  
5. ICS/calendar brief **if** an event happens to exist  
6. If still empty → **NOT FOUND (public)** + acquisition residual + optional incubate ticket — **no invented schedule**

### Prof hunt order (normative)

1. Official directory / course page if public  
2. Course code + name web search  
3. Reddit and public discussion (anecdote grade)  
4. Public post URL only if `@social`-class tools exist  
5. Never private groups; never present rumor as policy  

---

## FORBIDDEN

- Inventing exam dates, rooms, passing scores, or org facts when sources are silent  
- Stating hypotheses as verified institutional fact  
- Auth-walled / private group scrape  
- Continuous surveillance or “real-time firehose” of campus social  
- Doxxing, harassment framing, or non-public personal data harvest  
- Writing ungraded claims to Core / long_term  
- Replacing triangulation for Mapúa topics  
- Acting as a second AI or bypassing scout necessity gates on large bulk fetches  

---

## FAILURE MODES

| Mode | Response |
|------|----------|
| No public sources | `status: NOT_FOUND_PUBLIC` + residual channels still worth Commander check (LMS paste, faculty email — human path) |
| Only Reddit/anecdote | Package as **secondary**; block Core elevation |
| Contradictory dates | Side-by-side conflict row; do not pick a winner without independence rules |
| Auth / paywall | `AUTH-BLOCKED` / `INACCESSIBLE` — no fake paraphrase from memory posed as fetch |
| ICS empty for exams | Expected — do not treat as “no exam”; continue hunt |

---

## OUTPUTS

Every `@mapua` run emits a **Mapúa Pack** (markdown and/or JSON):

```text
MAPUA_PACK
- action: course-pack | exit-exam | prof | org | official-search | secondary-scan | gap-expand
- query: …
- status: FOUND_OFFICIAL | FOUND_SECONDARY_ONLY | MIXED | NOT_FOUND_PUBLIC | BLOCKED
- claims: [ { text, grade, source_url_or_id } ]
- sources: [ { url_or_id, type, note } ]
- hypotheses: [ { text, label: UNVERIFIED } ]   # only when expanding gaps
- residuals: [ … ]
- calendar_bonus: [ … ]   # optional ICS hits; never sole authority for exit exams
- next_acquisition: [ suggested queries / pages for Commander or next fetch ]
```

**Grades:** use house evidence taxonomy (`[D][O][I][R][N][S]` or local equivalent).  
**Hypothesis rule:** appears only under `hypotheses` or incubate — never merged into `claims` as verified.

---

## COMPOSITION

| Peer | Relation |
|------|----------|
| Calendar Summary bot | Optional bonus events; **not** sufficient for exit exams |
| `@fetch` / scout | `@mapua` supplies domain plan; they execute acquisition discipline |
| Research → Annotate → Triangulate | Required before Core |
| Future `@social` | Public post-by-URL only |
| Housekeeper | Unrelated (repo integrity) |

---

## ACCEPTANCE TESTS (design)

| # | Test | Pass |
|---|------|------|
| T1 | `exit-exam` with no ICS events | Still runs web/official path; does not conclude “no exam” from empty ICS alone |
| T2 | Only forum dates found | `FOUND_SECONDARY_ONLY`; claims graded secondary |
| T3 | No sources | `NOT_FOUND_PUBLIC` + residuals; no fabricated date |
| T4 | `gap-expand` | Hypotheses labeled UNVERIFIED; claims list unchanged by invention |
| T5 | `prof` private-only rumor | Residual / secondary; no Core-ready personal dossier |

---

## IMPLEMENTATION NOTES (Architect)

1. Skill file under `subskills/active/mapua.md` (or house naming) when ratified.  
2. Optional helper: `scripts/mapua_pack.py` — validates pack schema / emits template (no scrape engine required in v0.1).  
3. Curated allowlist of official hosts in playbook data (Commander-editable).  
4. Single-purpose Patch; does not mint a tenth pipeline skill — domain subskill only.

---

**End of skill card v0.1.**
