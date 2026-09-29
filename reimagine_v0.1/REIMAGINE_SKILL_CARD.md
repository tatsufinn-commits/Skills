# `@reimagine` — Image Re-Imagination Configuration Subskill

**Class:** Active skill (configuration engine) + scaffolding
**Version:** 0.1.1 (workspace build / design-of-record)
**Date:** 2026-09-29
**Status:** Polishing in the Skills workspace — **not** live canon until Patch + Commander/Desk authorize
**Parents:** Prompt kit · Prompt atlas · Blind-spots leg · 3D-enhancers leg · Vicinity-maps v2 · Practitioner audit · Student workflow (all: Skills repo `docs/`, 2026-09-29)
**Doctrine:** Words carry look, tools carry truth. In a 16-item audit (15 captured practitioner prompts + 1 own comparator), only 2 of the 15 captured prompts contained preserve-language. The preserve-list is the highest-leverage free change available (~2× measured edge-IoU) (single-plate, 3-run calibration; the winning run still retained only 25.4% of required-annotation pixels — measured, not magic). All atlas cards are `[N]` — this skill configures doctrine-best, never claims measured-best.

---

## MISSION

On trigger, convert a **task brief + photo reference** into a **paste-ready, law-gated prompt package** — routing to the right problem-card and provider, forcing the decisions operators forget (preserve/alter lists, rights pre-flight, disclosure), and gating the result through decidable QA before anything ships.

**Problem this solves (evidence-backed):** practitioners' prompt practice is styling-led and tool-anchored — in a 16-item audit (15 captured practitioner prompts + 1 own comparator), only 2 of the 15 captured prompts contained preserve-language, and both were meta-advice, not generation text. Meanwhile a measured experiment shows the preserve-list prompt is worth ~2× geometric fidelity, and a plate audit shows required annotations can vanish invisibly ("it looked fine"). The skill makes the disciplined path the default path.

---

## TRIGGERS

Activate when the Commander/user supplies an **image** (photo, screenshot, render, sketch, site/satellite view) or references one, and asks to:

- re-imagine / restyle / re-render / change the mood or materials
- enhance / upscale / restore / clean up (with fidelity intent)
- convert to 3D / extract a mesh / retexture
- derive a study: vicinity map, elevation style, massing concept, floorplan impression
- general (non-architectural) image re-imagination with a reference photo
- explicit `@reimagine` with any brief

**Do not fire on:** text-only image generation with no reference image (plain prompting); pure file conversion; anything in FORBIDDEN below. When no photo exists, the skill may still configure a text-to-image brief (atlas D01, A-cards' text-only variant) but must drop all fidelity claims.

---

## ACTIONS

| Action | Input | Behavior |
|---|---|---|
| `configure` | task + photo + context | Full pipeline → CONFIG_WORKSHEET package (default) |
| `intake` | conversation | Collect the six-field brief only; emit eligibility verdict |
| `gate` | an existing worksheet/prompt | Run QA_GATE checks; PASS/FAIL/UNVERIFIED per line |
| `route` | task description only | Card + provider + parameter skeleton, no paste text |
| `log` | completed run | Append to the iteration log (input, tool, prompt, numbers) |

**Default = `configure`.**

---

## PIPELINE (seven stages — full procedure in scaffolding/PROC_REIMAGINE.md)

```text
1 INTAKE     six-field brief (source & rights · view & source-of-truth · LOCKED ·
             ALLOWED CHANGE · reference roles · audience & evidence status)
             + eligibility gate. DUAL MODE: vision-direct OR structured
             questionnaire — both first-class (an operator without vision
             runs the questionnaire; the photo is never assumed).
2 CLASSIFY   task family (A architecture / P photo / D 3D / T audit) ×
             custody standing × fidelity requirement.
3 ROUTE      atlas card + provider from the matrix; decay-check provider facts.
4 CONFIGURE  fill the master prompt; FORCE preserve/alter lists; signal-channel
             setup (geometry in the tool, words for look); parameters;
             disclosure line if school/competition context.
5 GATE       decidable QA lines (PASS/FAIL/UNVERIFIED — "cannot tell from
             photo" = UNVERIFIED, never PASS); reject-drift → redo in an
             authoritative CAD/photo/mesh editor, do not re-prompt adjectives.
6 EMIT       CONFIG_WORKSHEET package: paste text + preserve/alter lists +
             QA results + rationale + risk flags + decision trail.
7 LOG        iteration record (input, tool, prompt, numbers). Future: receipt
             loop via @stockpile/@admit (pending that package's intake audit).
```

---

## HARD GATES (law — gates, not advisories)

- **G1 Rights pre-flight.** Own / licensed / cleared only. "No watermark," "Pinterest pin," "for class," "credits to owner" are **not** blanket licences (IPOPHL). Unknown rights → **do not upload**; describe an aesthetic in your own words or substitute a verifiable licensed item instead.
- **G2 CMI.** Never remove or obscure watermarks, credits, or attribution marks — including "incidentally" during enhancement. Refuse + explain.
- **G3 PD 1096 (vicinity plates).** Vicinity map within **2.00 km radius** (commercial/industrial/institutional) or **0.5 km** (residential), prominent landmarks/major thoroughfares, existing buildings hatched with distances to the proposed building; review/signature reserved to an **RLA**. AI composes *presentation*, never *geographic truth* — the radius, landmarks, distances and hatching are yours, re-overlayed from your own vector layers.
- **G4 Disclosure.** School/competition context → reproducible attribution (source, access date, URL, prompt description) + concept caption on the presentation sheet: *"AI-assisted concept visualization based on my [dated] model view; material/light reimagined; building dimensions and site context must be checked against the original drawings."* Disclosure is clear communication, not a licence substitute.
- **G5 Style authority.** Use own precedent, generic movement/palette language, or public-domain masters; reformulate named-style requests. Residual grader limitation: it detects the documented phrase patterns followed by capitalized names; it does not detect every indirect imitation, alias, or legal edge case, and capitalized non-person names can be false positives.

---

## FORBIDDEN

- Inventing facts, dimensions, provenance or rights status to fill a gap — flag, never fill.
- Claiming "measured-best," "exact," "unchanged," or "photoreal" as guarantees — prompt adjectives do not lock pixels, geometry, dimensions, identity or unseen surfaces.
- Removing/obscuring watermarks or credits (G2).
- Living-architect named-style imitation at scale (PH has **no freedom of panorama**, RA 8293) — use the lawful authority rungs: movement/palette language, deceased masters' expired-copyright works, or your own precedent studies.
- Producing official geographic truth from generated pixels (G3); survey/as-built claims from concept outputs.
- "Rotate it via img2img" for anything submittable — go back to the model or a 3D reconstruction route; never treat a new view as the same building.
- Bypassing reject-drift by re-prompting adjectives at a drifted output.
- Logging secrets, private credentials, or unreleased client material in the iteration log.

---

## EVIDENCE & LIMITS

- **Measured (corpus experiments `[I]`):** preserve-list ≈ 2× edge-IoU (0.485→0.898), SSIM 0.867→0.967, required-annotation retention 1.9%→25.4%; screenshot path degrades invisibly (SSIM 0.809 vs 0.967 clean); 3-run enhancer harness; vicinity plate audit (caught an 18.6% radius error on its own demo plate).
- **Not measured:** all 34 atlas prompt cards are `[N]` — no card's exact wording was run by the corpus. This skill's outputs inherit that boundary. Image quality claims require the runtime measurement tranche (fidelity harness) — scheduled, not promised.
- **Decay:** provider/platform facts recheck **2026-12-28**; interpretation 2027-09-29 (corpus-declared). Past decay → re-scout before routing.
- Full provenance: `evidence/EVIDENCE_APPENDIX.md`.

---

## COMPATIBILITY

Chat-only operator: fully functional (dual-mode intake). Python 3.8+ stdlib for the grader; no network, no subprocess, no API keys. Works alongside any provider UI — the skill emits paste text + tool settings; it never calls an API itself (v1 is configuration-only by design).

**Second-operator review recommended before any green light to RADIATION** — the TSSTM is this package's author and would also be its auditor.
