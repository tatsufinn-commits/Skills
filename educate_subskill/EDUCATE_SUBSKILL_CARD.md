# `@educate` — Horizon Expansion Subskill

**Class:** Active skill (depth mandate) + Horizon scaffolding  
**Version:** 0.1.0 (archive / design-of-record)  
**Date:** 2026-09-27  
**Status:** Prepared for future Patch — **not** on RADIATION main until Commander/DESK authorize  
**Parents:** Research · scout · @fetch · Annotate · Triangulate · CTP (anti-tourism) · (optional Calendar / @mapua when topic is domain-bound)  
**Doctrine:** One superior AI + many skills. `@educate` forces **depth and adjacency**, not coverage theater. Hypotheses stay UNVERIFIED. No invention to fill the horizon.

---

## MISSION

On magic words (“educate yourself on X”, “widen the horizon on X”, “go deep on X”, “everything I need around X”), force a **horizon expansion** around topic X:

- **Activate** latent/parametric knowledge into explicit, graded claims  
- **Acquire** external sources where needed (scout-gated)  
- **Expand** to necessary, relevant, akin, and adjacent material  
- **Integrate** multi-hop links (not isolated fact lists)  
- **Package** a **Horizon Pack** the superior AI and Commander can reuse for the rest of the session (and beyond, if admitted)

**Problem this solves (evidence-backed):** LLMs often have **coverage without depth** — strong surface recall, weak multi-hop integration, under-used internal knowledge, and summaries that leave humans with shallower learning than source-first synthesis. Industry “Deep Research” products exist because default chat under-delivers depth. `@educate` is the **RADIATION-native** depth mandate.

---

## TRIGGERS

Activate when Commander intent matches any of:

- “Educate yourself on …” / “Educate yourself about …”  
- “Widen the horizon on …” / “Expand your horizon on …”  
- “Go deep on …” / “In depth on …”  
- “Everything I need around …” / “All adjacent to …”  
- Explicit `/educate` or `@educate` with a topic  
- (Optional) Standing order: before high-stakes deliverable on unfamiliar X, run `@educate` once  

**Do not** auto-fire on every casual question — only on depth-mandate language or explicit skill call.

---

## ACTIONS

| Action | Input | Behavior |
|--------|--------|----------|
| `horizon` | `<topic>` `[use-case]` | Full Horizon scaffolding (default) |
| `core-only` | `<topic>` | Core fold only (fast floor) |
| `adjacent` | `<topic>` | Adjacent/akin expansion given existing core pack |
| `gap-fill` | `<prior pack>` | Widen only residuals / UNVERIFIED hypotheses |
| `refresh` | `<topic>` | Re-run acquisition for stale or time-sensitive horizon |

**Default = `horizon`.**

---

## FORBIDDEN

- Declaring the horizon “complete” from parametric prose alone with no sources or explicit activation log  
- Inventing adjacent topics or facts to satisfy quotas  
- Infinite crawl (must honor stop criteria)  
- Tourism: high word count, low source residence (CTP applies)  
- Writing ungraded claims to Core / long_term  
- Spawning a second AI / multi-agent swarm as product form (may *compose* with Research skill; does not mint peer agents)  
- Substituting a single summary for the Horizon Pack structure  

---

## FAILURE MODES

| Mode | Response |
|------|----------|
| Topic unbounded | Demand use-case or bound; refuse infinite “everything about X” |
| Sources blocked | BLOCKED / residual; continue with what is graded; no fake fill |
| Only secondary noise | Pack as secondary-heavy; block Core elevation |
| Model “feels done” early | Ignore; check stop criteria checklist only |
| Conflicts | Side-by-side; do not silent-resolve |

---

## OUTPUTS — Horizon Pack

```text
HORIZON_PACK
- schema_version: educate/horizon/0.1
- topic: …
- use_case: …                    # anchors stop criteria
- status: ADEQUATE | PARTIAL | BLOCKED | NOT_STARTED
- folds_completed: [seed, core, necessary, adjacent, integrate, gaps, pack]
- core: [ { claim, grade, source } ]
- necessary: [ { claim, grade, source } ]      # prerequisites to USE topic
- adjacent: [ { topic, relation, claims[] } ]  # akin / near-neighbor
- integrations: [ { link, from, to, note } ]   # multi-hop
- hypotheses: [ { text, label: UNVERIFIED } ]
- residuals: [ … ]
- depth_tags: { D1_count, D2_count, D3_count }  # optional Webb-style
- sources_index: [ … ]
- stop_reason: use_case_met | quota_met | commander_halt | blocked
- next_acquisition: [ … ]
```

---

## COMPOSITION

| Peer | Relation |
|------|----------|
| Research / @Gather | Acquisition engine under scout |
| CTP | Mandatory on extract/generate folds — no volume tourism |
| Triangulate | Before Core admission of horizon claims |
| @mapua | If topic is Mapúa-bound, prefer @mapua playbook *inside* domain folds |
| Calendar Summary | Time-sensitive adjacent only; not a substitute for depth |
| /verdict | May select “run @educate on X” as a path; does not replace horizon folds |

---

## ACCEPTANCE TESTS (design)

| # | Test | Pass |
|---|------|------|
| T1 | Magic phrase + topic | Horizon scaffolding runs; pack emitted |
| T2 | Empty parametric-only “done” | Rejected; sources or explicit activation required |
| T3 | Adjacent quota | ≥ N near-neighbors attempted or residual why not |
| T4 | Multi-hop | ≥1 integration link when core+necessary both non-empty |
| T5 | Hypothesis | UNVERIFIED only; not merged into core claims |
| T6 | Stop | Pack records stop_reason; no infinite loop |
| T7 | CTP smoke | Claims show source residence, not orphan prose |

---

## IMPLEMENTATION NOTES (Architect)

1. Skill file: `subskills/active/educate.md` (or house naming) when ratified.  
2. Scaffolding: `scaffolding/core/proc_horizon-expansion.md` (or generated → improved → core path).  
3. Optional: `scripts/horizon_pack.py` validate template (schema only in v0.1).  
4. Single-purpose Patch; does not replace Research skill.  
5. Evidence appendix travels with design-of-record for DESK/Architect.

---

**End of skill card v0.1.**
