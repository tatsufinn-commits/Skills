# CONFIG_WORKSHEET — the emit template

One worksheet per run (Stage 6). This template **is** the machine contract consumed by `evals/grader.py` (see schemas/worksheet.schema.json): `KEY: value` lines are parsed position-agnostically; `## Section` headers open sections; preserve/alter/QA items are `- ` list lines; QA boxes are `- [ ]`. Replace every `⟨…⟩` before emitting — no placeholders survive to a PASS.

```markdown
# @reimagine — Configuration Worksheet ⟨run id / date⟩

## Brief
TASK: ⟨one sentence: what is being re-imagined and why⟩
CARD: ⟨A|P|D|T⟩⟨00⟩            ← from references/atlas-router.md
PROVIDER: ⟨tool + model/version as confirmed in the live UI⟩
PHOTO: ⟨yes|no⟩
PHOTO_SOURCE: ⟨own|licensed|cleared|internet-untraced|none⟩
SCHOOL: ⟨yes|no⟩               ← any coursework/competition context
STYLE_AUTHORITY: ⟨rung + wording — movement/palette language, own precedent, or public-domain master; never a named living architect⟩
AUDIENCE: ⟨internal mood study|client concept|public|approval package⟩
DEADLINE: ⟨date or -⟩

## Paste text
```text
⟨The paste-ready prompt. Master grammar: base description → style-only separation →
keep-list → ONE bounded reinterpretation → viewpoint lock → unknowns-as-unknown →
concept-status line. Every bracket replaced with a KNOWN input; unknown claims removed,
not guessed. Goes only where the paste-field router says text goes at all.⟩
```

## Preserve list
- ⟨projection/view invariant first: e.g. "east elevation, eye-level, same camera and framing"⟩
- ⟨concrete observable feature: bay/window/door counts and positions⟩
- ⟨… footprint edges, roof profile, entrance, circulation, legal annotations⟩

## Alter list
- ⟨the ONE bounded change from intake field 4⟩

## Tool settings
- ⟨inputs attached and their roles (A geometry/base · B style-only · C mask)⟩
- ⟨channel setup: e.g. ControlNet depth 0.7–0.8 / img2img 0.35–0.55 / IP-Adapter 0.5–0.7⟩
- ⟨versions, seed if exposed, what was actually accepted⟩

## QA gate
- [ ] ⟨decidable check: overlay source and output at identical crop; verify ⟨invariant 1⟩⟩
- [ ] ⟨decidable check: count ⟨bays/openings⟩ against the original; any change = FAIL⟩
- [ ] ⟨decidable check: inspect non-selected regions for drift⟩
- [ ] ⟨decidable check: confirm no unrequested content (people, logos, labels, new elements)⟩
- [ ] ⟨decidable check: dimensions/site conditions validated in original documents, not pixels⟩
- [ ] ⟨decidable check: caption + attribution placed outside the generative pass⟩
REJECT-DRIFT RULE: on drift of any LOCKED invariant — reject, redo in an authoritative CAD/photo/mesh editor or attach better measured inputs; never re-prompt adjectives at a drifted output.

## Disclosure            ← required when SCHOOL: yes
⟨Caption (presentation sheet): "AI-assisted concept visualization based on my [dated]
model view; material/light reimagined; building dimensions and site context must be
checked against the original drawings."⟩
⟨Reproducible attribution if any third-party reference used: source, access date
(YYYY-MM-DD), URL, prompt description.⟩

## Rationale
RATIONALE: ⟨why this card / provider / channel setup — the decision trail, incl. decay
status of provider facts and any risk flags (no geometry channel available, base-quality
limits, [N] card status)⟩

## Log
- ⟨date · input id · tool + version · card id · measured numbers or "not measured" · verdict⟩
```

**Emission rules:** placeholders → not emittable (Stage 5 blocks). PHOTO: no → preserve/alter lists become "N/A — text-only brief; fidelity claims dropped" (grader expects exactly that line in each section). PHOTO_SOURCE: internet-untraced → the worksheet may not be emitted at all (Gate 0).
