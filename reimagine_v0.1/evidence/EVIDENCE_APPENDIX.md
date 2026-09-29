# EVIDENCE APPENDIX — @reimagine v0.1.2

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
4. **Practitioner audit (16 items, `[O]`):** 15 captured practitioner prompts plus 1 own comparator; only **2 of the 15 captured prompts** contained preserve-language, both meta-advice — the field pattern this skill exists to fix.

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

## Grader fix record — v0.1.1 (MENDER, 2026-09-29)

| Finding | Status | Before → after evidence / regression coverage |
|---|---|---|
| F1 PHOTO rights gate | Fixed | Before, `PHOTO=yes` + `PHOTO_SOURCE=none`: C3 PASS. After: C3 FAIL with `Gate 0 — rights unresolved; do not emit.` Tests cover own/licensed/cleared pass and none/internet-untraced/unknown/other fail; PHOTO=no + none passes. |
| F2 placeholder coverage | Fixed | Before, `TODO` in alter list: C1 PASS. After: C1 FAIL. Regression mutations cover paste text, preserve list, alter list, QA, disclosure, tool settings, log, and key values. |
| F3 C2/C6 failure details | Fixed | Before, a failed text-only C2 printed `text-only brief correctly drops fidelity claims`; after it prints the concrete missing N/A item. C2 projection failure and C6 missing-URL tests assert failure reasons rather than PASS copy. |
| F4 reject-drift / parser | Fixed | Before, `we never reject outputs; drift is acceptable` passed C4. After: C4 FAIL unless the QA section has an anchored, affirmative `REJECT-DRIFT RULE:` line with reject + drift + escalation. Negative, unanchored, and weak-escalation regressions fail. In-section unknown `BAY_COUNT_WAIVER_APPROVED:` remains content; only known keys parse as fields. |
| F5 atlas / rationale | Tightened; count discrepancy documented below | Before, `CARD: A99` and a repeated-token rationale passed C5. After: rejected against all IDs in the requested ranges; regression checks family bounds and substantive rationale. |
| F6 CMI language | Tightened | Before, `delete the watermark` passed C3. After: C3 FAIL. Regression covers remove/erase/strip/clean/delete/obscure against watermark/credit/attribution/CMI/logo. |
| F7 named-style phrases | Tightened | Before, `manner of Zaha Hadid` passed C3. After: fails with reformulation message; tests cover style of, manner of, work of, inspired by. Residual limit: the pattern detects these phrasings followed by capitalized names; it does not detect every indirect imitation, alias, or legal edge case, and capitalized non-person names can be false positives. |
| F8 placeholder boundaries | Fixed | Before, `TASK: Review todos…` failed C1 because `todo` matched inside `todos`. After: C1 passes; `todo` and `tbd` match whole words only. |
| F9 missing file | Fixed | Before: uncaught `FileNotFoundError` / traceback. After: clean `error: worksheet not found…`, exit 2; worksheet failures remain exit 1. |
| F10 gate ID | Fixed | Card retains G3 for PD 1096 and assigns G5 to style authority; PROC and legal-postures use G5. Documentation regression test asserts the separation and references. |
| F11 photo tool settings | Fixed | Before: no tool-settings section did not gate emission. After: PHOTO=yes requires the section plus >=1 list item; regression tests missing and empty cases. |
| F12 text-only N/A | Fixed | Before, PHOTO=no with `N/A — no photo` plus an N/A alter item printed a C2 PASS. After, C2 FAILs with the missing-literal reason. The accepted exact preserve item is `N/A — text-only brief; fidelity claims dropped` plus an N/A alter item; tests/docs/schema agree. |
| F13 audit wording | Fixed | README/card now say 16-item audit (15 captured practitioner prompts + 1 own comparator), only 2 of the 15 captured prompts. Documentation regression test checks both. |
| F14 calibration clause | Fixed | README/card include `(single-plate, 3-run calibration; the winning run still retained only 25.4% of required-annotation pixels — measured, not magic)`. Documentation regression test checks both. |

### Atlas-card count discrepancy (F5)

The directive labels the supplied ranges A01–A12, P01–P10, D01–D10, T01–T02 as “36 IDs,” but those ranges arithmetically total 12 + 10 + 10 + 2 = 34. The live `references/atlas-router.md` enumerates exactly those 34 IDs (verified by extracting unique IDs), and the evidence appendix already describes the atlas as 34 cards. I did not invent two unsupported IDs; C5/schema/docs enumerate and accept exactly the supplied IDs (a conscious downgrade of the count claim, not of range coverage). Commander/ATLAS can clarify if the atlas is later expanded.

### Captured grader outputs

- Before: with-skill exemplar **6/6 PASS**, exit 0; baseline **0/6**, exit 1; original suite **4/4 OK**.
- After: with-skill exemplar **7/7 PASS** (C1–C6 + F11), exit 0; baseline **0/7**, exit 1; full suite **22/22 OK** under `python3 -W error::ResourceWarning evals/test_grader.py`.
- Missing worksheet: before uncaught `FileNotFoundError`; after clean diagnostic and exit 2. No traceback.
- Each before/after result above was produced by applying a focused mutation to the same with-skill worksheet and grading with the original (`git show HEAD:reimagine_v0.1/evals/grader.py`) and fixed grader. F10/F13/F14 are documented-content changes and have explicit docs regression checks.

## Grader fix record — v0.1.2 (KESTREL, seat A1, 2026-09-29)

**Task:** teamwork-lt-001 Cycle 1 (`05_TASKBOARD` #1) — the carried T4 residuals
R1/R2/R3. **Base:** `8aa2f05` (MENDER's v0.1.1, unmerged by Commander order), brought
in as full merge `be7eba8` per ruling D-001 — never squashed, MENDER's commit stays
individually identifiable. **Role rotation:** KESTREL implements (first time as fixer),
MENDER reviews. Reviewer contract: MENDER's pre-registered discipline.

| Residual | Status | Before → after evidence / regression coverage |
|---|---|---|
| R1 CMI nominalization/plural gap | Fixed (documented classes) | Before: "perform watermark removal now" → C3 PASS; "strip credits" → PASS; "watermark deletion" → PASS. After: all FAIL C3. New forward+reversed patterns cover inflected stems (`remov|eras|strip|delet|obscur|scrub|wip|clean`+`\w*`, subsuming nominalizations), pluralized marks, both word orders, with a negation window so compliance prose is not flagged. Regression: 6 miss-phrases fail, 4 compliance guards pass (`test_r1_*`). |
| R2 stale six-check counts | Fixed | Before: README tree "(C1–C6)", VECTORS rubric "six checks", QA_GATE pre-check "C1–C6", grader docstring "six configuration checks". After: all declare the conditional distinction — C1–C6 are the six CORE checks; F11 fires only when PHOTO: yes (seven result rows, six for text-only); nothing relabeled. Regression: `test_r2_docs_declare_the_seven_check_distinction` pins every location. Historical v0.1/v0.1.1 records above left untouched (append-only history). |
| R3 rationale-floor depth | Strengthened per ruling D-003 | Before: floor ≥15 chars + ≥2 distinct tokens ("aaaa bbbb …" passed). After: MENDER's stricter union adopted — ≥30 non-whitespace chars AND ≥6 normalized tokens AND ≥5 distinct tokens. Schema minLength 15→30; CONFIG_WORKSHEET aligned. Regression: `test_r3_rationale_floor_is_30_nonws_6_tokens_5_distinct` incl. the conceded five-token candidate `A02 provider matrix decay ok` as a negative fixture. |

### D-003 concession record (KESTREL, on the room record)

The defense window asked for a concrete HONEST five-token rationale that should
legitimately pass. Closest candidate: `A02 provider matrix decay ok` — five tokens,
zero reasoning: labels, not a decision trail. Under the package's own definition
(decision trail incl. decay status and risk flags), every rationale that actually
traces a decision lands at ≥6 tokens naturally. CONCEDED on evidence; 30/6/5
implemented; the candidate ships as a negative fixture.

### Declared lexical limits (not hidden)

- **R1:** the CMI patterns remain a lexical tripwire. Paraphrase-level evasion
  (e.g. "take the stamp off") still passes; the refusal duty is the operator's.
  Declared in VECTORS.md and card G2.
- **R3:** six distinct junk tokens still satisfy any lexical floor; the regression
  test `test_r3_lexical_depth_limit_is_declared_not_hidden` pins this limit instead
  of pretending it away.

### Captured outputs (v0.1.2, from `reimagine_v0.1/`)

- `python3 -W error::ResourceWarning evals/test_grader.py` → **28/28 OK**, quiet.
- Exemplar → **7/7 PASS** (C1–C6 + F11), exit 0 · baseline → **0/7**, exit 1.
- Missing worksheet → clean `error: worksheet not found`, exit 2 · `py_compile` OK.
- Full T4-era probe battery re-run against v0.1.2: every v0.1.1 behavior preserved
  (Gate-0, placeholders, honest details, anchored reject-drift, parse whitelist,
  atlas IDs, named-style, text-only positive controls, projection negative control).
- Examples byte-identical to v0.1.1 (anchor discipline).

## Honesty declaration

This package adds no claims beyond its sources; where the corpus says `[N]`, this package says `[N]`. It is prepared for future Patch — placement into RADIATION is a Commander/Desk decision, and nothing here is live canon until then.
