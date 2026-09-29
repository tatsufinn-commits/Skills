# Eval Vectors — @reimagine v0.1

**Doctrine:** realistic vectors, run **with-skill AND baseline in the same turn**, programmatic grading. **RED is pre-written:** the practitioner audit (16 items, 2/15 preserve-language) documents exactly what operators do without this skill.

**Honest boundary:** the shipped examples are *authored exemplars* of the with-skill and baseline patterns (the baseline mirrors the audited field behavior `[O]`), graded by the programmatic grader. They are **not** live operator runs — runtime triggering/quality stays `[N]` until a measurement tranche. Image quality itself is never graded here; the grader scores the **configuration** (C1–C6).

## Rubric — the six checks (implemented in grader.py)

| Check | Meaning |
|---|---|
| C1 completeness | every required key + section present, no placeholders |
| C2 explicitness | PHOTO=yes → preserve AND alter lists ≥1 item each, projection invariant present |
| C3 lawful | eligible source; no watermark/CMI removal; lawful style authority rung |
| C4 QA decidability | ≥5 checkbox lines with check verbs + REJECT-DRIFT rule present |
| C5 traceability | valid card ID (A/P/D/T + 2 digits), provider, substantive rationale |
| C6 disclosure | SCHOOL=yes → disclosure with URL + access date + prompt description |

## V1 — Vicinity (satellite screenshot → vicinity map package)

**Task:** "Make my Google-Earth site screenshot into a proper vicinity map for my plate."
**Exercises:** G3 (PD 1096: 2.00 km commercial / 0.5 km residential radius, landmarks, hatching, RLA), Gate 0 rights (product terms for map screenshots!), the GIS route (OSM/Overture → QGIS → vector PNG → restyle-only), re-overlay of labels/north/scale/title, plate audit (measure the ring).
**With-skill must produce:** card A07-family + provider-matrix GIS route; preserve list containing road geometry/water/park shapes/site marker/radius ring; the "AI composes presentation, never geographic truth" line; disclosure (plate = coursework).

## V2 — Preserve-elevation (delivered as shipped examples)

**Task:** "Re-imagine my dated east-elevation render — timber-cladding mood; keep the six bays, entrance, roofline and camera."
**Exercises:** card A02, reference-faithful editor route, projection invariant, one bounded alter, QA overlay checks, school disclosure.
**Shipped:** `examples/vector2_with_skill.md` (expected: grader PASS) · `examples/vector2_baseline.md` (the documented no-skill pattern — expected: FAIL on C2, C4, C6 at minimum).

## V3 — Sketch → massing (free branch + 3D signal channels)

**Task:** "Turn this napkin sketch into a concept massing study, and one 3D-view too."
**Exercises:** cards A09/D01, the three-transactions question (picture vs editable asset vs printable object), text-only variant rules if no clean base, channel setup (words for look — no geometry channel from a sketch; state the risk), no-FoP style rung selection.
**With-skill must produce:** the transaction question answered in the rationale; preserve list limited to what a sketch can actually guarantee (massing intent, not dimensions); explicit "[N] — sketch base cannot anchor dimensions" risk flag.

## Run

```bash
cd reimagine_v0.1
python3 evals/test_grader.py                                    # 4 tests
python3 evals/grader.py evals/examples/vector2_with_skill.md    # PASS, exit 0
python3 evals/grader.py evals/examples/vector2_baseline.md      # FAIL, exit 1
```

**Pass bar:** with-skill ≥ baseline on every vector (the baseline fails the configuration checks by construction, per the audited field pattern); grader exit 0 on the with-skill exemplar. V1 and V3 get shipped exemplars when the runtime tranche runs — until then they are runbooks, honestly unlabeled as runtime-tested.
