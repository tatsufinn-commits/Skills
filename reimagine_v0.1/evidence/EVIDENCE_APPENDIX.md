# EVIDENCE APPENDIX — @reimagine v0.1

**Status:** workspace build (Skills repo) — **not live canon until Patch + Commander/Desk authorize.**
**Author:** TSSTM (Arena AI Agent Mode), S019, 2026-09-29, Commander-commissioned.
**Second-operator review recommended before any green light** — the TSSTM is this package's author and would also be its auditor.

## Provenance — every file's source

| File | Source (Skills repo `docs/`, 2026-09-29 design track) |
|---|---|
| REIMAGINE_SKILL_CARD.md | all seven corpus docs (condensed); triggers = task families; gates = legal postures |
| references/atlas-router.md | reimagination-prompt-atlas (34 cards `[N]`, fast selector, paste-field router — condensed, structure preserved) |
| references/provider-matrix.md | architectura-image-prompt-kit (provider translation notes) + vicinity-maps v2 (GIS route, reference-faithful editors) + 3D-enhancers (channel settings) |
| references/legal-postures.md | reimagine-blindspots (rights/custody, IPOPHL) + vicinity-maps v2 (PD 1096 IRR Rule III, PH governance) + workflow steps 3 & 7 + kit eligibility gate |
| references/fidelity-dial.md | reimagine-blindspots §6 (executed experiment, decision bands, snippet warning) + 3D-enhancers §7 (STEP 0–6 protocol, supersedes the earlier ladder) + kit fields 3–5 |
| references/signal-channels.md | 3D-enhancers §1–§5 (five-channel model, authority ladder, enhancer classes, spatial vocabulary) + practitioner audit (words-carry-look finding) |
| scaffolding/PROC_REIMAGINE.md | S017 build plan × corpus docs (pipeline assembly) |
| scaffolding/INTAKE_FORM.md | prompt-kit six-field brief + workflow steps 2–4 + questionnaire mode (new, dual-mode design) |
| scaffolding/CONFIG_WORKSHEET.md | prompt-kit master-prompt grammar + worksheet machine contract (new) |
| scaffolding/QA_GATE.md | prompt-kit independent QA & publication gate + workflow step 6 |
| schemas/*.json | machine contracts for the above (new) |
| evals/* | rubric C1–C6 (S017 plan) + grader/tests/examples (new code) |

## Measured evidence inherited `[I]` (corpus-executed, not re-run here)

1. **Preserve-list experiment:** edge-IoU 0.485 → **0.898**, SSIM 0.867 → **0.967**, required-annotation retention 1.9% → 25.4% — same model, prompt was the only variable. Decision bands: ≥0.85 IoU + ≥0.95 SSIM = faithful restyle; 0.6–0.8 = usable with redraw; <0.6 or missing annotations = not submittable.
2. **Snippet-path degradation:** 460 px JPEG-35 input measured SSIM 0.809 / IoU 0.653 vs the clean path's 0.967 / 0.898 — fidelity loss invisible without measurement.
3. **Vicinity plate audit:** caught an 18.6% radius error on a demo plate whose own annotation claimed 2 km.
4. **Practitioner audit (16 items, `[O]`):** preserve-language in **2/15** captured prompts, both meta-advice — the field pattern this skill exists to fix.

## Boundaries — declared, not hidden

- **All 34 atlas prompt cards are `[N]`** (corpus-untested at runtime). This package configures doctrine-best, law-gated work; it never claims measured-best. Prompt adjectives do not lock pixels, geometry, dimensions, identity or unseen surfaces.
- **Shipped examples are authored exemplars** (GREEN pattern + the audited no-skill baseline pattern), graded programmatically — **not live operator runs**. Runtime triggering and image quality stay `[N]` until the measurement tranche runs.
- **V1 is configuration-only:** emits paste packages + tool settings; makes no API calls; cannot enforce preservation by itself — the QA gate and the authoritative-editor redo rule carry that duty.
- **No-vision operators:** questionnaire mode is first-class; photo descriptions recorded as `[O] user-described`, never as verified visual fact.
- **Decay:** provider/platform facts recheck **2026-12-28** (corpus-declared); legal interpretation 2027-09-29. Past decay → re-scout before routing.
- **Open input (corpus gap statement):** the Commander's incoming external photo-based re-imagination research is not yet in the drop; on receipt it feeds the v3 corpus and this package's photo-in recipes.
- **stockpile_admit integration** (Stage 7 receipt loop) is deferred pending that package's intake audit — not wired in v0.1.

## Verification performed at build (S019, 2026-09-29)

| Command (from `reimagine_v0.1/`) | Result |
|---|---|
| `python3 -m py_compile evals/grader.py evals/test_grader.py` | OK |
| `python3 evals/test_grader.py` | **4/4 tests OK** (with-skill passes; baseline fails C2/C4/C6; forbidden phrase fails C3; bad card ID fails C5) |
| `python3 evals/grader.py evals/examples/vector2_with_skill.md` | **6/6 checks PASS**, exit 0 |
| `python3 evals/grader.py evals/examples/vector2_baseline.md` | **0/6**, exit 1 (by design) |
| `python3 -W error::ResourceWarning …` re-run | quiet + green (unclosed-file warning fixed at build) |
| Security sweep (`api[_-]?key|secret|token|password|Bearer|sk-…`) | CLEAN — only documentation lines ("no secrets", "never log secrets") |
| Dependency check | Python 3.8+ stdlib only; no network; no subprocess |

## Honesty declaration

This package adds no claims beyond its sources; where the corpus says `[N]`, this package says `[N]`. It is prepared for future Patch — placement into RADIATION is a Commander/Desk decision, and nothing here is live canon until then.
