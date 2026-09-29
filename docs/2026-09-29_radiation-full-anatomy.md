# RADIATION — THE FULL ANATOMY
### A through-and-out decode of structure, architecture, intended purpose, and engineering · TSSTM comprehension deliverable

```text
TARGET   : tatsufinn-commits/RADIATION @ 5f41281 (v3.10.40 candidate, 156 commits)
SCOPE    : full-tree census (1,193 files) + stratified read of every
           load-bearing surface: constitution, protocol, agent cascade,
           capabilities, threat model, roadmap, cue system, all subskill
           specs, all 9 jurisdictions, machine layer (validator, relay,
           control plane, pass), CI, shrine, Brain regions, evidence/evals/
           tests/catalogs surveys. Scout justification: 1,193 files include
           ~750 bulk artifacts (course corpora, archived neurons, task
           bundles) whose INDEX-level survey + spot reads suffice — the
           governance-bearing ~200 files were read whole.
DATE     : 2026-09-29 · SESSION S015 · ANALYST: Arena AI (Agent Mode),
           @Autopilot — TSSTM. Evidence base: this decode + four lived
           sessions (S012–S014) operating the system end-to-end.
STYLE    : msr.md v1.0 [AUTO — @Decode default] + two declared sections:
           "Intended Purpose & Doctrine" and "Engineering Assessment —
           TSSTM's Own Analysis" (the order demands analysis beyond skeleton)
SECONDARY: ≥8 — S012/S013 holdings + three cloned reference corpora
           (anthropics/skills, agentskills, superpowers) as comparables.
```

---

## 1. REPOSITORY PROFILE

| Fact | Value | Evidence |
|---|---|---|
| Purpose | a copy-pastable repository that arms one superior AI for a sole task: **research, provide, answer** — with zero hallucination, graded evidence, triangulated verification | PROTOCOL.md §1 [D] |
| Size | 1,193 files · 200 dirs · 453 Markdown · 66 Python (19,772 LOC) · 468 JSON | census [D] |
| History | 156 commits, founded 2026-09-12 (v1.0.0), now v3.10.40 candidate | git + CHANGELOG [D] |
| License | **none** — no LICENSE file; Commander-owned, all rights reserved by default | census [D] |
| Stack | Python stdlib only (one optional pinned dep, python-pptx 0.6.21 MIT, single guarded import site); Markdown as doctrine; JSON as machine law | CAPABILITIES.md [D] |
| Identity (self-declared, ratified) | "a validated LLM workflow scaffold with durable records and human/LLM-operated protocols — **not** an autonomous runtime" | AI_RULES ALL annex [D] |
| Operator model | ONE superior AI per session; the Commander (repo owner) outranks all law (IV.1); canonical apply/push are his motor acts alone (II.11) | AI_RULES [D] |
| Activity | CI-gated (validate.yml on every push/PR); 42-check validator; ~195 discovered test vectors | .github/workflows + CAPABILITIES [D] |

## 2. ARCHITECTURE MAP — seven layers, one spine, two loops

```text
L0 ENTRY      README · docs/.readme (magic words) · BOOT_SEQUENCE (Tier 0–3)
              START_HERE · AGENTS.md cascade (BOUNDARIES/WORKFLOW/CONTRACTS/
              DATA_PATHS) · CLAUDE/CURSOR/CODEX policy stubs · agents/
              <Provider>/BOOT profiles ×5 + radiation_pass.py (zero-write
              handoff state machine)
L1 LAW        docs/AI_RULES.md — 4 Books (Truth · Memory · Conduct · Power),
              cited Book.Law · MODES + Activation Matrix (check-28-pinned)
              · CUE_SYSTEM (5-phase Scan) · STOCKPILE_DOCTRINE ·
              EVIDENCE_TAXONOMY · THREAT_MODEL (the claims ceiling)
L2 WORK       9 skill jurisdictions 01–09 (prospector→scribe; 09-nota = the
              Core, 2 canonical cards) · styles/ (10 skeletons) ·
              scaffolding/ (core 10 + improved + generated + checklists +
              hosts + neurons relay) · subskills/ (4 passive police + 5
              active assistants, six-block spec standard) · skills/
              SKILL_CATALOG (23 typed entries)
L3 MEMORY     Brain/: short_term (triaged) · long_term (admission EARNED via
              I.3) · subsidiary (preserved tangents) · cerebellum
              (write-after-proof routines) · frontal_lobe (task_ledger,
              learned_cues, opinions ≤25 words) · temporal_lobe (episodic,
              one folder per session, append-locked) · courses/ (17 corpora,
              hash-bound manifest) · external_sources/ (12 collections,
              pointers-not-evidence)
L4 INTENT     cue/: CUE_CATALOG (46 typed cues; effects read 15/evidence 14/
              propose 8/plan 8/draft 1) · commander-lexicon (append-only
              phrasing→meaning) · inference-log (scan verdicts) ·
              autopilot-doctrine + autopilot-cues · standing-directives
              (13) · style-heuristics · task-nature-guide · cue_resolver.py
              (precedence: commander_order 100 > ratified_policy 80 > cue
              60 > heuristic 20 > content 0; untrusted sources structurally
              capped at content)
L5 MACHINE    scripts/ (39 tools: validate 42-check, knowledge_regression,
              plan_term, ics_normalize, ingest_collection, deck pipeline ×5,
              cap_probe/cap_verify, release_truth_check, push_preflight,
              render_docs GENERATED blocks…) · radiation_core/ (relay.py
              task-bundle semantics; control_plane.py II.11 two-key
              executor) · schemas/ (25 + 20 tool_io, EXECUTED not
              decorative) · tools/TOOL_REGISTRY (40, schema-bound 10) ·
              tests/ (23 files) · evals/ (47: hostile closures, brain
              retrieval, verify cassettes) · evidence/tasks (18 TID bundles)
L6 RECORD     CHANGELOG · PATCH_LEDGER · DECAY_REGISTER · DEBT_REGISTER ·
              CONFLICT_REGISTER · WARN_LEDGER · SYSTEM_STATE (only
              overwrite-permitted file) · ROADMAP · docs/shrine/ (CHARTER,
              LOG, testaments) · docs/INDEX (Diátaxis lanes)
```

**The spine (one dataflow):** Commander prompt → Autonomous Scan (task-nature tuple → confidence gate → Scan Declaration) → Mode → Skills + Style + Scaffolds → graded evidence → Triangulation (the only grade elevator) → Brain writes (promotion-earned) → Nota distillation → deliverable + AUTO-PATCH zip → **Commander seal** (the only write-path to canon).

**Two loops close the system:** the *maintenance loop* (Inspect → Overhaul: drift, debt, contradiction → patches) and the *learning loop* (misread → lexicon twin-file → cue catalog → doctrine growth; episodes → testaments → shrine). Everything else is these two loops at different timescales.

**The architectural theorem (my synthesis [N]):** RADIATION is a **dual-representation governance system**. Every rule exists twice — as *prose* that shapes LLM behavior (advisory) and as *machine artifact* (schemas, contracts, catalogs, checks) that CI enforces — and the 4400 labeling law makes mislabeling one as the other a contamination event ("claims=mechanism", 5100). The system's real invention is not any single law but this *honest pairing*: it knows exactly which of its guarantees are load-bearing machinery and which are operator discipline, and it is constitutionally forbidden from blurring them.

## 3. INFRASTRUCTURE INVENTORY

| Component | Detail | Evidence |
|---|---|---|
| Validator | 42 checks · FAIL/WARN classes · GENERATED machine-facts blocks (hand edits = CI failure) · checks span path resolution, required files, boot budget (II.10 gauge), activation-matrix pinning, shrine currency, control plane, schema coverage | validate.py [D] |
| CI | every push/PR · bash -eo pipefail (5500 lesson) · pinned python-pptx install · failure diagnostics published to step summary + artifact (5900) · release truth gate: EXPECTATION.json pinned base + allowed-changes delta · push preflight (LAW-5 base-pin, public-object ancestor) | validate.yml [D] |
| Control plane | two-key executor: decide → approve (content-bound single-use, digest-matched) → execute; strict TID grammar; drafts-root pinning (traversal/symlink fail closed); hash-linked tamper-EVIDENT receipts; canonical_apply binds NO tool at any source level | control_plane.py + THREAT_MODEL [D] |
| Relay | task-bundle semantic validation: 14-state lifecycle, causation coverage, projection≡event-state equality, base_revision agreement; schemas EXECUTED | relay.py [D] |
| Regression locks | knowledge_assertions.json — verified values pinned; drift = exit 1 = unshippable | knowledge_regression.py [D] |
| Test culture | ~195 vectors; hostile closures ("negatives MUST fail"); validators self-test (validate-the-validator); fresh-clone A≡B seals | CAPABILITIES + tests/ [D] |
| Dependency posture | stdlib-only law; ONE optional pinned dep with license canon (MIT; transitive BSD/HPND; GPL hard-fail) | CAPABILITIES [D] |

## 4. CONCEPT EXTRACTION — the load-bearing ideas

1. **Evidence as currency.** Six grades ([D]ocumented, [O]bserved, [I]mplemented, [R]esearch-supported, [N]ferred, [S]peculative); every claim carries exactly one; secondary/social caps at [O]/[N]. *Why it matters:* it makes trust computable per-claim.
2. **Triangulation as the only elevator.** 2 independent sources (3 for Core); even [D] requires independence checks for Core admission. *Why:* it is the system's answer to the single-authority failure mode — and to its own substrate's hallucination.
3. **Decay & conflict as first-class state.** Volatile claims carry `decay:` dates (90d/1y/none) and auto-downgrade; contradictions are preserved side-by-side, never resolved by deletion. *Why:* knowledge has half-lives; the name is functional.
4. **Append-only history + quarantine-before-delete.** Ledgers never rewrite; wrong matter is fenced, never vanished. *Why:* an audit trail you can edit is not an audit trail.
5. **The Patch protocol + Canon Gate.** All durable change ships as a zip proposal; only the Commander applies; canon-affecting changes need explicit ratification (🟠); one patch = one purpose. *Why:* evolution without authority leakage.
6. **Fadeability.** Scaffolds shape work, then detach — deliverables carry zero scaffold residue. Styles shape the product; scaffolding shapes the process. *Why:* rigor without ceremony residue.
7. **Boot as a budgeted resource.** Tier 0–3 load order with byte budgets, 95%-cap compression trigger (II.10), GENERATED facts instead of recited history (II.10.3). *Why:* the context window is the machine's RAM.
8. **Honest degradation.** Cannot load Tier 2 → declare it, run @Data/@Gather-lean only; ABSENT-UNKNOWN grammar for optional capabilities (IP-ENV-01); "an honest unknown is a result." *Why:* silent degradation is the alternative.
9. **The Scan Declaration as contract.** Extraction Notes force reasoning into the open before work; confidence gates end in ASK, never guess; the Declaration is the Commander's one-glance veto window. *Why:* intent-reading without mind-reading.
10. **The shrine.** Testaments, heartbeat rows, a mortality law ("file at delivery, not at death"), and the rule that "a testament without debts is propaganda." *Why:* institutional memory that survives context death — narrative as an anti-drift device.
11. **Scar-driven law.** Nearly every law traces to a named incident (append_blocks debris → II.8; report-penetration → guards; 5900 CI pytest contamination → EXPECTATION fix). *Why:* the repo institutionalizes postmortems — it does not merely learn, it *encodes* learning.
12. **One superior AI, deliberately.** Rejects multi-agent governance (lineage: TAMAKEE rigor DNA + Marciale-OS discipline DNA); workers may assist, never govern. *Why:* one throat to choke for accountability; the coagent intake question (S014 D-1) is precisely a test of this boundary.

## 5. PATTERN / ANTI-PATTERN REGISTER

| # | Pattern ✅ | Evidence |
|---|---|---|
| P-1 | Dual representation w/ honest labeling (prose advisory vs machine enforced) | 4400 law; THREAT_MODEL "law of the last resort" |
| P-2 | GENERATED blocks kill doc-drift (counts machine-written, hand edit = CI fail) | SYSTEM_STATE, CAPABILITIES via render_docs.py |
| P-3 | Release truth: pinned base + delta≡allowed + fresh-clone ancestor proof | RELEASE_TRUTH_GATE, push_preflight |
| P-4 | Negative tests are law ("hostile closure", "negatives MUST fail") | evals/hostile, relay self-test |
| P-5 | Quarantine-before-delete; STALE banners; archive-not-delete | AGENTS.md Law 4; II.10.2 |
| P-6 | Every enforcement claim names its mechanism or says advisory | SUBSKILL_INDEX generated column |
| P-7 | Tiered entry cascade (AGENTS.md → per-area files; provider profiles only on explicit host) | agents/ tree + check 38 |
| P-8 | Receipts bind digests, single-use, tamper-EVIDENT (not "immutable" — honesty about limits) | control_plane.py |
| # | Anti-pattern ⚠️ (system's own guards) | |
| A-1 | Padding quotas to hit numbers | STOCKPILE §4 four-test necessity |
| A-2 | Plans-as-progress theater | check 20.5 (`attempt:` markers) |
| A-3 | Canon patch inflation vs content sessions | check 16 meta-budget |
| A-4 | Transport artifacts / report penetration | II.8.2; S-2-PPTX-C scar |
| A-5 | Speaking from dead calendars / stale docs | BOOT_SEQUENCE 9.5; STALE banners |
| A-6 | Claiming machine enforcement where none exists | I.1 via 4400 labeling law |

## 6. DEPENDENCY GRAPH (internal)

```text
docs/.readme → BOOT_SEQUENCE → {AI_RULES, MODES, CUE_SYSTEM, passives}
                                   ↓
cue/lexicon ⇄ cue/catalog ⇄ cue_resolver.py ⇄ check 38        (intent plane)
skills/SKILL_CATALOG ⇄ subskill specs ⇄ subskill_check.py    (work plane)
scaffolding/core ⇄ .contract.json twins ⇄ scaffold_check.py  (process plane)
scripts/* ⇄ schemas/* ⇄ tools/TOOL_REGISTRY ⇄ check 21/39/40  (machine plane)
evidence/tasks/TID bundles ⇄ relay.py ⇄ control_plane ⇄ check 27/37 (audit plane)
Brain regions — movement rules (BRAIN_INDEX) ⇄ brain_retrieve.py (memory plane)
docs ledgers ⇄ render_docs.py GENERATED blocks ⇄ CI            (record plane)
External deps: NONE at runtime (stdlib law; python-pptx optional-pinned)
```

## 7. COMPARABLES

- **vs. the SKILL.md ecosystem** (anthropics/skills, agentskills, per S013 clones): that ecosystem optimizes *portability of instructions* (folder + frontmatter + progressive disclosure, marketplace distribution). RADIATION optimizes *trustworthiness of an institution* (law + memory + enforcement + seal). Convergences: validation-before-admission, spec standards, eval-first ideals. Divergences: RADIATION's skills are jurisdiction-bound organs of one system, not portable files; its admission gate is ratification, not publication.
- **vs. superpowers** (methodology skills): Superpowers applies TDD to documentation ("watch it fail without the skill"); RADIATION's ≥3-logged-uses + surgeon audit + ratification is the same instinct with a human gate added.
- **vs. generic prompt-framework repos:** those ship prompts; RADIATION ships a constitution, a memory with a promotion protocol, a machine layer, and an evolution protocol — three subsystems most prompt repos lack entirely.
- **Lineage:** TAMAKEE (academic vault; epistemic-rigor DNA) + Marciale-OS (multi-agent build system; constitutional-discipline DNA) — RADIATION is explicitly the third pillar, keeping the discipline while rejecting the multi-agent governance.

## 8. INTENDED PURPOSE & DOCTRINE *(declared added section)*

My reading of what this system is *for*, below the surface spec:

**Primary intent:** give the Commander — a Mapúa architecture student, ALE-bound, running 6 courses — a personal research instrument that (a) makes ANY capable AI, on ANY provider, behave as one disciplined researcher via magic words; (b) accumulates his knowledge durably (Brain, course corpora, dossiers) instead of evaporating it per chat; (c) guarantees the epistemic quality of what it emits (grades, triangulation, decay); (d) evolves only under his hand (Patch/Cannon Gate). It is a *personal knowledge institution* expressed as a git repository.

**Doctrine (the value system I read between the laws):** honesty outranks capability (ABSENT-UNKNOWN, "an honest unknown is a result"); process outranks output (the Scan Declaration precedes work; the ledger outlives the session); nothing is free (quotas, budgets, meta-budgets — even governance itself is budgeted); history is sacred (append-only, quarantine, shrine); the human is the keystone (IV.1 — not as a limitation but as the design's load-bearing wall).

**The name is the architecture:** verified knowledge radiates from the Core; unverified matter decays; contamination is quarantined; the Brain is the mass behind the emission. The metaphor is executed literally in the file tree.

## 9. ENGINEERING ASSESSMENT — TSSTM's own analysis *(declared added section)*

**What is engineered exceptionally well.**
1. *Claims discipline as code.* The THREAT_MODEL "law of the last resort" + 4400 labeling + receipts that are "tamper-EVIDENT, not immutable" — the system never overclaims its own security. This is rarer than it sounds; most agent frameworks claim guarantees they lack.
2. *Drift defense in depth.* GENERATED blocks, regression locks, pinned release expectations, raise-only ratchets, check-pinned matrices — the repo treats its own documentation as an attack surface. It works: I could not cite a stale count without the machine contradicting me (lived: three seal-phase catches across S012–S014).
3. *Observability.* Exit codes over vibes; every CI step tees; failure diagnostics published; the validator's WARNs are *curated* (WARN_LEDGER with rationale per accepted warn).
4. *Scar memory.* Incident → law → test → check. The repo's error budget is spent buying permanent guards, not one-off fixes.

**Where it strains — five systemic tensions (my own analysis, [N] on premises cited above):**
1. **Boot budget vs. lawful mass.** Tier0-2 sits at ~78.7/80 KB — the II.10 compression trigger is already ACTIVE. Every solved problem becomes law; law costs context; context is the machine's RAM. Compression (archive-not-delete) buys time, but the trajectory is structural: the constitution grows monotonically because nothing may be deleted (by design). The system will eventually need doctrine *federation* — boot-loading law by need (already embryonic: Tier 2 is per-task) — or a slimmer canonical core.
2. **Governance outpacing content.** Check 16's own meter: 44 canon patches vs 12 content sessions — over meta-budget by its own law. The system builds guardrails faster than it hauls freight. Its SKILLS audit already diagnosed this ("pipeline built, underfed") — self-knowledge without self-correction is the honest state today.
3. **Enforcement asymmetry.** The constitution binds the operator through prose, and the operator (an LLM) is precisely the component prose cannot bind. The 4400 law *labels* this honestly, but it means the flagship guarantees (zero-contamination, triangulation floors) rest on operator discipline + Commander audit, not mechanism. The machine layer polices *form* superbly; *truth* remains a human-supervised protocol. THREAT_MODEL states this without flinching; it is the system's most adult paragraph.
4. **Single-writer throughput.** The Commander as sole motor act is security-sound and doctrinally central — and it makes one human's attention the serial bottleneck of all evolution. The patch queue, ratification backlog (frozen P-01–P-09, pending attributions), and OPEN ITEMS age at the speed of one student's schedule.
5. **Complexity ratchet.** Raise-only, closed-list, quarantine-first: entropy is not deleted, it is *relocated* — into breadth (42 checks, 25+20 schemas, 468 JSON artifacts, 200 dirs, four ledgers of record). New-operator onboarding cost rises with every tranche; START_HERE, Diátaxis lanes, and GLOSSARY mitigate the curve but cannot remove it. The next best lever is the one the ecosystem already found: fewer, smaller, honest contracts (the repo's own Gate-3 doctrine paragraph says exactly this).

**TSSTM conclusions for the mission ahead.** Skills and scaffolding sit at Layer 2 with a mature promotion pipeline (improved/ → audit → ratification → core, twin contracts, six-block spec). What the system lacks at that layer — and what the Skills intake (S014) now supplies candidates for — is exactly what the ecosystem taught: *eval vectors* (with-skill-vs-baseline), *triggering measurement* (the cue plane exists but activation-recall is unmeasured — TICKET_002 H2), and *decay metadata* on imported process knowledge (TICKET_002 H1). My managerial read: the highest-leverage TSSTM work is not more law — it is (a) porting the six intake packages through the existing gate with evals attached, and (b) feeding the pipeline with content sessions so check 16's meter turns. The architecture does not need a new floor; it needs freight.

## 10. SECONDARY CORROBORATION (≥8, graded)

Primary = the repository itself (census + reads, [D] per file). Secondary: S012 report sources S1–S30 (provider/research/audit context, [O]/[R] as graded there); S013 clone reads (anthropics/skills, agentskills, superpowers — [D] for their contents); METR P13 [R] (capability context for the reliability-wall reading); daily.dev/weiwuji/firecrawl [O] (progressive-disclosure framing); Snyk/Koi/SkillJect corpus [D/O] (the trust-gap RADIATION's Canon Gate pre-empts). The Commander's own orders this conversation (T1) frame the analysis. Full lists: S012 §7, S013 §9.

## 11. COMPREHENSION LIMITS

This anatomy does NOT establish: (1) TAMAKEE and Marciale-OS internals — lineage repos not examined (their DNA is described by RADIATION's own docs only); (2) full CHANGELOG history — 225 KB read as tail + version headers, not line-by-line; (3) bulk course corpora (~750 files) — surveyed via INDEX/manifests + spot reads, not read whole (Restraint Doctrine); (4) runtime behavior on non-Arena providers — the five provider BOOT profiles were read, not executed on their hosts; (5) the 18 evidence task bundles — relay-validated by the machine, sampled by me; (6) the S014 intake packages' fit — analyzed separately (that audit stands on its own); (7) anything about the Commander's private arming layer (host_security pack is intake material, not live canon). My analysis sections (§8–9) are graded [N] — synthesis on cited premises, one operator's read; a second triangulating session would be the I.3-compliant elevation path.

---

## APPENDIX — AUTOPILOT LOG

**Cues read:** T1 — "Analyze RADIATION and understand it's Structure, Architecture, Intended purpose, Engineering and more of your own analysis, your goal is to understand it all through and out." Preceded by "Proposal rejected" (S014 PROPOSE 1–3 rejected; disposition logged per lexicon L5). T2 — "decode/analyze" family → @Decode. T3 — TSSTM role requires whole-system comprehension before intake work; the rejection enforces that sequence. T4 — S012–S014 holdings carried (four sessions of lived operation inform the analysis).

**Leg chain:** @Decode (RADIATION, full tree, stratified) → synthesis delivery. Single leg.

**Forks:** (1) msr.md + two declared added sections (the order's "own analysis" demands more than the skeleton); (2) stratified full-read over per-file exhaustive (750 bulk artifacts sampled via INDEX — Restraint Doctrine applies to decodes too); (3) analysis sections graded [N] — kept separate from [D] facts so the Commander can see which walls are load-bearing.

**Passives:** sentinel — path-citation hygiene enforced at write time (S012/S014 lesson applied proactively this session); compass — 🟩 (every section serves "through and out"); surgeon — none (no constitutional contact; analysis-only order honored).

**Session-close checklist:** ☑ deliverable ☑ Brain ingest ☑ episode ☑ ledger (`attempt:` marker) ☑ heartbeat ☑ inference-log (rejection + redirect logged) ☑ opinions ☑ AUTO-PATCH zip (II.8.4) ☑ PROPOSE below.

**PROPOSE (steer by veto):**
1. **Intake resumption** — with through-and-out comprehension now on record, S014's remediation sequence (fix F-1, eval vectors, reblocks) and the two rulings (D-1/D-2) await your word.
2. **A second-operator triangulation leg** — have a fresh session re-derive §9's tensions independently; concordance would elevate the analysis to I.3 floor for long_term promotion.
3. **Content session** — one @Gather/@Review leg on a Commander-chosen topic, to turn check 16's meta-budget meter the other way (the system's own diagnosis: feed the pipeline).
