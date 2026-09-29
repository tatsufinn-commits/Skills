# Atlas Router — 34 problem-indexed cards `[N]`

**Source:** Skills repo `docs/2026-09-29_reimagination-prompt-atlas.md` (S014 design track). **Every card is `[N]` — untested at runtime.** A cited complaint explains why a card exists; it is not evidence the card solves it.

## Usage rules (from the atlas, binding)

1. Choose a **problem**, not a provider. Replace bracketed fields with real observations; never guess.
2. Distinguish the five inputs: **geometry/source** · **style reference** · **texture reference** · **mask/selection** · **output specification**. If the tool's UI lacks an input, omit that claim or change tools.
3. Setup-line operations are **not** words to paste. Text goes in a **text-capable** field or serves as a human brief.
4. Adjectives ("exact," "unchanged," "photoreal") do **not** lock pixels, geometry, dimensions, identity or unseen surfaces.
5. Keep an untouched original; record version, settings, source view, and what was actually accepted.
6. Stop decision from the card's **Check** line: if an invariant is non-negotiable and drifts, reject → redo in an authoritative CAD/photo/mesh editor or attach better measured inputs.

## Card index

**A — Architecture (12): preserve a design while changing its portrayal.** Text-capable image-to-image editor with the named permitted images attached; A10 also needs actual separate views. For text-to-image tools: replace "source view" with an explicitly imagined design, drop all fidelity claims.

| ID | Problem |
|---|---|
| A01 | Rough massing / model screenshot → exterior concept |
| A02 | Refinish only a facade region |
| A03 | Same geometry, new daylight / weather mood |
| A04 | Interior palette/furnishing refresh without redesign |
| A05 | Insert one object without replacing the room |
| A06 | Remove temporary clutter from a building photograph |
| A07 | Context/site atmosphere, not a survey |
| A08 | Elevation / diagram *style* without invented dimensions |
| A09 | Early-stage physical-model / sketch look |
| A10 | Two existing views of the same building, coordinated look |
| A11 | Change the building's *design*, with a stated change boundary |
| A12 | Floorplan → perspective *impression* (not automatic BIM) |

**P — Photo/enhancement (10): correction is not factual recovery.**

| ID | Problem |
|---|---|
| P01 | Remove one distraction rather than redesign the photograph |
| P02 | Refill a small damaged area or paint blemish |
| P03 | Expand a photograph for a poster crop |
| P04 | Match the color of a retouched patch to the source |
| P05 | Low-light denoise that keeps fine texture |
| P06 | Old portrait restoration with an identity ceiling |
| P07 | Tiny screenshot, logo or text: enhance legibility, do not hallucinate facts |
| P08 | A genuinely promptable Gigapixel image description |
| P09 | Fabric/skin smoothing or sharp halo triage |
| P10 | Intentional creative reinterpretation with honest labeling |

**D — 3D (10): decide first whether you need a picture, an editable asset, or a printable object.**

| ID | Problem |
|---|---|
| D01 | Words → simple 3D product-study object |
| D02 | Single product photo → speculative 3D prop |
| D03 | Real multi-view photos → one object mesh |
| D04 | Retexture a supplied mesh without asking for a new object |
| D05 | Low-poly game prop with a target budget |
| D06 | Object missing or wrong from rear view |
| D07 | 3D print concept: visible texture is not printable relief |
| D08 | Change one feature on an *existing* 3D asset |
| D09 | Furniture kit, not a one-shot "build my whole room" mesh |
| D10 | Decorative surface versus actual modeled carving |

**T — Audit/refine (2): not automatic measurement.**

| ID | Problem |
|---|---|
| T01 | Source/output difference log for an image or mesh |
| T02 | After a failed generation, revise *one variable* |

## Fast selector (condensed from the atlas)

| Future problem | Start with | Required distinction |
|---|---|---|
| Sketch/model → exterior mood without moving openings | A01, A03 | Source view ≠ geometric guarantee |
| Facade finish, interior furnishing, insert one object | A02, A04, A05 | Region/selection vs whole-view rewrite |
| Context/site, elevation, floorplan, camera angles | A07, A08, A10, A12 | Speculative image vs geospatial/CAD truth |
| Remove an object, extend a photo, fix a seam | P01–P03 | Blank fill/Remove/selection and edge QA |
| Denoise, restore face, rescue tiny text or fabric | P05–P09 | Conservative settings vs new invented detail |
| Invent a mesh from words/front photo/multiple views | D01–D03 | Text input vs one input image vs actual multi-image input |
| Change mesh look, game asset, print object | D04–D07, D10 | UV/topology/scale; geometry vs color map |
| Debug why any prompt failed | T01, T02 | Diagnose operation and observed delta before adding adjectives |

## Paste-field router — recheck the live UI before using

| Workflow | Where text goes, if at all | Non-text input/setting and major limit |
|---|---|---|
| SketchUp AI Render | Current prompt field, if enabled (D01–D03) | Model view, style preset, Paint/Erase mask where available. Do NOT assume geometry-respect sliders exist. |
| Photoshop Generative Fill | Selection → prompt or **blank** → model/variations | Selection + layers (+ separate Remove op); selected ≠ non-selected proved unchanged. |
| Midjourney | Generate/Editor text in the relevant version | Style Reference changes aesthetic, does not copy a building; Edit Model is separate; confirm version/parameter syntax. No universal exact-preserve flag. |
| FLUX.2 layout guidance | Instructions in the guide's editing workflow | Uploaded reference image(s); not an automatically available native ControlNet field; no pixel-perfect guarantee. |
| Topaz Gigapixel Redefine | *Image description* on documented realistic-Subtle or creative configs — phrase as **description, not directive** | Creativity/texture settings; Face Recovery disabled in Redefine creative. |
| Topaz Face Recovery / Lightroom Enhance | **No natural-language prompt in these controls** | Select faces / model / mode / strength. A text prompt elsewhere is not their setting. |
| Meshy | Text describes geometry (text-to-3D) or retexture; `texture_prompt` is **texture-only**, not a geometry slot; upload source images separately | D07 accepts 1–4 separately supplied geometry views — generated views are not evidence of a real back. No deprecated `negative_prompt`. |
| TRELLIS.2 / Hunyuan3D-2.1 / Tripo | Check their own current upstream UI/README/tips | A request or failure report on one project does not create another's input route. |

## Card anatomy (how to read any card)

`Setup` = operation outside the paste text · paste text = the copyable brief · `Check/fallback` = performed on the *result*, not assumed · `Basis` = research-report D/R/O codes + `[N]` on the text itself.
