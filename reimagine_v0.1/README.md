# @reimagine — Image Re-Imagination Configuration Skill

**Version:** 0.1.2 · **Date:** 2026-09-29 · **Author:** TSSTM (Arena AI Agent Mode), Commander-commissioned
**Status:** WORKSPACE BUILD — lives in the Skills repo for polishing; **NOT live canon until Patch + Commander/Desk authorize.**

## What this is

A configuration skill for image re-imagination work: given a **task brief + photo reference**, it runs a seven-stage pipeline (intake → classify → route → configure → gate → emit → log) and produces a **paste-ready, law-gated prompt package** — not just a prettier prompt. Built for the Commander's context (Mapúa architecture student, PH law, PD 1096 plates) and general enough for any image re-imagination task with a reference photo.

**Core finding it is built on:** in a 16-item audit (15 captured practitioner prompts + 1 own comparator), only **2 of the 15 captured prompts** contained preserve-language — while a measured experiment showed a preserve-list prompt roughly **doubled geometric fidelity** (edge-IoU 0.485 → 0.898, SSIM 0.867 → 0.967) (single-plate, 3-run calibration; the winning run still retained only 25.4% of required-annotation pixels — measured, not magic). Forcing explicit preserve/alter lists is the single highest-leverage change available. That is this skill's heart.

## Tree

```
reimagine_v0.1/
  README.md                       ← you are here
  REIMAGINE_SKILL_CARD.md         the skill itself (triggers, pipeline, gates)
  references/                     loaded per-stage, keeps the card lean
    atlas-router.md               34 problem-indexed cards + paste-field router
    provider-matrix.md            task → tool routing (decay-dated)
    legal-postures.md             rights, CMI, PD 1096, school disclosure
    fidelity-dial.md              preserve/alter protocol + measured thresholds
    signal-channels.md            5-channel model + authority ladder
  scaffolding/
    PROC_REIMAGINE.md             the seven-stage procedure
    INTAKE_FORM.md                dual-mode brief (vision / questionnaire)
    CONFIG_WORKSHEET.md           the emit template + machine grammar
    QA_GATE.md                    decidable gate + reject-drift rule
  schemas/
    intake.schema.json            required intake fields
    worksheet.schema.json         worksheet field contract
  evals/
    VECTORS.md                    3 acceptance vectors + rubric
    grader.py                     programmatic grader (C1–C6 core + conditional F11), stdlib only
    test_grader.py                28 tests — run exactly: python3 -W error::ResourceWarning evals/test_grader.py
    examples/vector2_with_skill.md   GREEN exemplar (graded PASS)
    examples/vector2_baseline.md     RED exemplar — the documented no-skill failure
  evidence/
    EVIDENCE_APPENDIX.md          provenance, [N] boundaries, decay dates
```

## Run the evals

```bash
python3 -W error::ResourceWarning evals/test_grader.py  # 28 tests
python3 evals/grader.py evals/examples/vector2_with_skill.md    # → PASS, exit 0
python3 evals/grader.py evals/examples/vector2_baseline.md      # → FAIL, exit 1
```

Stdlib only. No network, no subprocess, no secrets. The grader checks the **configuration** (completeness, explicitness, law, QA decidability, traceability, disclosure) — image quality itself stays `[N]` until a runtime measurement tranche exists (see EVIDENCE_APPENDIX).

## Honesty declaration

Every prompt card in the atlas is `[N]` — untested at runtime by the corpus that authored it. This skill configures **doctrine-best, law-gated** packages and says so; it never claims measured-best. Three corpus experiments are measured (fidelity, plate audit, enhancer runs) and are cited where they apply.
