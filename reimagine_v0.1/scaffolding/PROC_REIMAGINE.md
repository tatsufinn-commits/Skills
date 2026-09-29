# PROC_REIMAGINE — the seven-stage configuration procedure

**Default action: `configure`.** Each stage names its input, output, and failure route. Stages may not be skipped; a stage with nothing to say writes "N/A — reason" rather than silence.

## Stage 1 — INTAKE (scaffolding/INTAKE_FORM.md)

Collect the **six-field brief** (kit grammar): (1) SOURCE & rights · (2) VIEW & source-of-truth · (3) LOCKED · (4) ALLOWED CHANGE · (5) REFERENCE ROLES · (6) AUDIENCE & evidence status. Plus context flags: school/competition, deadline, provider access.

**Dual-mode photo reading — both modes first-class:**
- *Vision mode:* the operator examines the attached photo directly; still confirm rights verbally.
- *Questionnaire mode (this operator's default — it has no vision):* walk the INTAKE_FORM questionnaire — photo type, what it shows, ownership, quality/provenance (screenshot? original export? resolution guess), and the user's own listing of features that must survive.

**Gate 0 — eligibility (G1):** `own / licensed / cleared` → proceed. `internet-untraced / unknown` → STOP: offer the lawful alternatives (describe aesthetic in own words · make own reference · request permission · substitute verifiable licensed item). Record the eligibility verdict in the worksheet — `PHOTO_SOURCE` key.

## Stage 2 — CLASSIFY

Three axes:
- **Task family:** A (architecture portrayal change) · P (photo correction/enhancement) · D (3D transaction — first decide picture / editable asset / printable object) · T (audit/revise an existing attempt).
- **Custody standing:** from Gate 0 + CMI check (G2) + no-FoP style-authority check (G5 rungs).
- **Fidelity requirement:** which features are LOCKED (measured constraints from documents) vs visual cues; which band the output must reach (fidelity-dial decision bands).

## Stage 3 — ROUTE (references/atlas-router.md + provider-matrix.md)

- Pick the **problem card** (never the provider first). State the required distinction from the fast selector.
- Pick the provider whose **non-text input carries the invariant**; check the paste-field router for where text even goes (some workflows have NO prompt field — then the deliverable is settings, not words).
- **Decay check:** provider facts past 2026-12-28 → re-scout before routing; note the recheck in the rationale.

## Stage 4 — CONFIGURE (references/fidelity-dial.md + signal-channels.md)

- Fill the master-prompt grammar from the kit: base description · style-only separation · keep-list · one bounded reinterpretation · viewpoint lock · unknowns-as-unknown · concept-status line.
- **FORCE the preserve/alter lists** — 13/15 real prompts omit preserve-language; this skill never does when a reference photo exists. Include the **projection/view invariant**.
- Signal-channel setup per the matrix (geometry in the tool; words for look). If the tool has no geometry channel, say so and hold expectations accordingly.
- Disclosure line (G4) if school/competition/public audience.

## Stage 5 — GATE (scaffolding/QA_GATE.md)

Run the decidable QA lines. Rules: `PASS / FAIL / UNVERIFIED` with actual evidence; **"cannot tell from photo" = UNVERIFIED, never PASS**. On drift of a non-negotiable invariant: **reject → redo in an authoritative CAD/photo/mesh editor** (or attach better measured inputs). Re-prompting adjectives at a drifted output is forbidden. Programmatic pre-check: `python3 evals/grader.py <worksheet>`.

## Stage 6 — EMIT (scaffolding/CONFIG_WORKSHEET.md)

One worksheet per run: paste text + preserve/alter lists + tool settings + QA results + disclosure + rationale + risk flags (e.g. "provider facts near decay," "no geometry channel available — fidelity risk"). The worksheet is the deliverable the user acts on.

## Stage 7 — LOG

Append to the iteration log: date · input (id, not contents) · tool + version · prompt/card id · measured numbers or **"not measured"** · verdict. Never log secrets or unreleased client material. Future: receipt loop via `@stockpile`/`@admit` (ADMIT | QUARANTINE | REJECT | DECAY-PROPOSE) — **pending that package's intake audit; do not integrate before it.**

## Failure routes (summary)

- Rights unknown → stop at Gate 0 (lawful alternatives).
- Watermark/CMI removal request → refuse + explain (G2).
- Living-architect named style → reformulate to lawful rung (G5 style authority).
- Drifted invariant → authoritative-editor redo, not adjective re-prompting.
- Another angle needed → back to the model / 3D reconstruction; never img2img "rotate."
- Provider past decay → re-scout before routing.
