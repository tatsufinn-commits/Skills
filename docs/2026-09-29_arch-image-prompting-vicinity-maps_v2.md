# RESEARCH — Architectural Image-Based Prompting for Vicinity Maps & Other Architectural Diagrams
## v2 — REBUILT UNDER COMMANDER REJECTION: relevancy + strength

> **Session:** S012 · 2026-09-29 · Arena AI (Agent Mode) — booted on RADIATION v3.10.40-candidate (base `78029d3`)
> **Commissioned by:** THE COMMANDER — v1 order: *"@[Autopilot] | STYLE: [AUTO] | TOPIC: [Research regarding Architectural imaged based prompt for enhanced vicinity map, and other architectural diagrams]"*; then the **rejection**: *"your proposal is rejected, you improve your research in terms of relevancy and strength. use other LLM provider's info, researches, audits, repositories, platforms, social media relevant informations and other you may deem necessary."*
> **Disposition of v1:** `outputs/2026-09-29_arch-image-prompting-vicinity-maps.md` — **preserved, untouched** (II.4); logged REJECTED in `docs/PATCH_LEDGER.md` with the lesson; this file supersedes it as the live deliverable.
> **Mode:** @Autopilot — RE-SCAN (III.9) executed; legs @Gather (v2 sweep) → @Data → audit execution.
> **Style:** `research.md` base **[AUTO]** + one declared addition: **§7 EXECUTED AUDIT** (reason: the rejection demanded strength — measured evidence beats assertion).
> **Everything graded** `[D][O][I][R][N][S]`. No Nota. No Core write.

---

## 1. WHAT CHANGED, AND WHY (the rejection, read honestly)

The Commander's rejection has two named axes. This is what I take them to mean, and what I did about each:

| Axis | v1's failure | v2's answer |
|---|---|---|
| **RELEVANCY** | v1 answered *"what is generative AI, generally, for diagrams"* — normative + methodological. It never told the Commander **which 2026 product does which job**, on which platform, at what price, with which access path for a student. | **§3.2–3.5**: a provider-by-provider, platform-by-platform operational map — OpenAI, Google, Anthropic, xAI, Black Forest Labs, Recraft, Adobe, Alibaba/Qwen, ByteDance, Midjourney — **plus the AEC/GIS-native stack that actually does site plans** (Autodesk Forma, TestFit, Esri, Mapbox MCP, SketchUp Diffusion, QGIS/prettymaps), **plus grounding** that fixes map hallucination at the source. **§6.1** reduces all of it to a use-this-for-that matrix with student-reality access notes. |
| **STRENGTH** | v1's evidence was vendor pages + a handful of papers; its "demonstration" was an unchecked image; no measurement, no audits, no repos, no community practice. | **§3.7–3.8**: benchmark and audit layer (MapBench, LMArena 28M-vote image arena, Q-Judger, GDELT, Dagstuhl, Hasselblad disqualification, GSDiff/HouseDiffusion) **plus an executed, reproducible audit** of this session's own demo plate (`outputs/2026-09-29_plate_audit.py` → **4 measured findings, plate fails internal consistency**). **§8** registers **62 new sources** (SRC-071…SRC-132) incl. 12 repositories, 3 social threads, 4 audits and 3 regulatory trackers; total registry now **113**.

*Sentinel note (kept in the record): my first audit-harness run produced a false "scale inconsistency" of 40 % — my own px-per-km arithmetic was wrong. The fix was a second, independent derivation inside the same harness; the two now agree (222.0 vs 222.29 px/km). The verifier was itself verified. That is the lesson, not an embarrassment.*

---

## 2. SCOPE & ANCHOR

**Anchor (verbatim):** *"Research regarding Architectural imaged based prompt for enhanced vicinity map, and other architectural diagrams."* — rebound to the rejection order's scope: other providers' info, research, audits, repositories, platforms, social media.

**In scope:** the operational question — *for a given architectural plate, which 2026 tool/provider/platform, reached how, with what prompt, checked how, at what risk.* Covers: (a) PD 1096's legal baseline for the plates that matter; (b) the generative providers; (c) the AEC/GIS platforms; (d) the prompt grammar + condition-image discipline; (e) audits and benchmarks; (f) an executed verification harness with numbers; (g) licence custody and disclosure law incl. the EU AI Act's August-2026 marking duties and PH's pending bills.

**Out of scope:** any real project's geodata; any claim that AI output is permit-acceptable; any model "best" verdict beyond what the cited evidence supports; building software.

---

## 3. FINDINGS

### 3.1 The legal baseline is unchanged and it is not negotiable [D]

PD 1096, 2004 Revised IRR, Rule III (permit documents): vicinity map **within 2.00 km radius (commercial/industrial/institutional) or 0.5 km (residential)** at any convenient scale, *"showing prominent landmarks or major thoroughfares for easy reference"*; SDP with technical description, boundaries, orientation, lot relationship and *"existing buildings within and adjoining the lot shall be hatched and distances between the proposed and existing buildings shall be indicated."* ★ three independent copies `[D] [SRC-020] [SRC-021] [SRC-022]`, OBO checklist corroboration `[D] [SRC-069]`; review/signature reserved to a **Registered and Licensed Architect** `[D] [SRC-020] [SRC-052]`. **Operative consequence for every recipe below:** AI may compose *presentation*, never *geographic truth*; the radius, the landmarks, the distances and the hatching are yours.

### 3.2 The generative providers, 2026 — who is actually good at what `[D]/[O]`

| Provider / model family | What its own documentation claims | Diagram-relevant strength | Access / cost | Grade |
|---|---|---|---|---|
| **OpenAI — GPT-Image (1.5 → 2)** | Guide states you can configure size (multiples of 16, up to 3840 px, 1:3–3:1), quality `low…max`, transparency; and — directly on point — *"For diagrams and information graphics, verify labels and factual relationships as well as appearance"*; use `quality: high` "for dense labels, diagrams, or assets that will be used in slides or course materials" | Best-documented instruction following; explicit diagram guidance; `input_fidelity: high` to preserve input details in edits | ChatGPT free tier (limited) / API per image | `[D] [SRC-071] [SRC-072]` |
| **Google — Nano Banana Pro (Gemini 3 Pro Image)** | Official page: *"Create and edit images with studio-quality levels of precision and control"*, *"Generate clear text for posters and **intricate diagrams**"*; multi-frame consistency demonstrated from a reference sketch. API docs: **all generated images carry a SynthID watermark** | Reference-image fidelity (practitioner consensus: *"it holds geometry from a reference better than the rest"*); free in the Gemini app | Gemini app free (daily limits); API ≈ $0.134–0.24/img `[O] [SRC-133]` | `[D] [SRC-027] [SRC-076]`, `[O] [SRC-035]` |
| **Black Forest Labs — FLUX.1 Kontext [pro/max]** | *"In-context image generation… prompt with both text and images"*; local editing; style reference; iterative edits without fine-tune. Official prompting guide: *preserve intentionally* (state what stays unchanged; "maintain the original composition") | The cleanest local-edit instrument; the preserve-list idiom originated here | BFL playground / partners (Replicate, Together, Fireworks) | `[D] [SRC-028] [SRC-029]` |
| **xAI — Grok Imagine 2.0** | Docs: image generation with aspect ratio / resolution (1K, 2K) / batch; **image editing with up to 5 reference images**; $0.04/image | Multi-reference editing at the lowest listed per-image price among frontier APIs | X/Grok app + xAI API | `[D] [SRC-074] [SRC-075]` |
| **Recraft — V3 / V4** | Docs: V3 *"the only model capable of placing text at specific positions in an image"*; **Vector variant generates editable SVG**; curated + custom styles with consistency from few examples; $0.04 raster / $0.08 vector per image | **The only mainstream provider that hands you vectors** — the correct output format for architectural work | recraft.ai (free tier) + API | `[D] [SRC-079] [SRC-080]` |
| **Adobe — Firefly** | FAQ: trained on *"licensed content, such as Adobe Stock, along with public domain content"*; outputs usable commercially; Content Credentials applied on export | The **commercially-safe** option when training-data provenance matters to a client or school ethics review — *but see the conflict, §5.2* | Adobe plans/credits | `[D] [SRC-081]`, `[O] [SRC-082]` |
| **Alibaba — Qwen-Image (20B MMDiT) + Edit** | Apache-2.0 open weights; standout capability = **complex bilingual (EN/CN) text rendering**; runs in ComfyUI / diffusers locally; 2512 refresh ranked among top open models on community arenas | Self-hosted, licence-clean, strong labels; the free/local path if a GPU exists | local (free) or fal.ai API | `[O] [SRC-083] [SRC-084]` |
| **ByteDance — Seedream 4.x** | Unified generate+edit; **up to 6 reference images**; 4K; platform page lists use case *"Produce accurate diagrams or timelines with labeled details"*; official prompt guidance = subject+action+setting, keep under ~600 words | Multi-reference consistency for a board's whole plate set | Volcengine / fal / Replicate | `[O] [SRC-086] [SRC-087] [SRC-088]` |
| **Midjourney — v7/v8 line** | Practitioner-documented: `--sref` style reference + `--sw` weight for board-wide coherence; `--raw` for *"cleaner geometry and structural lines"*; `--no text` | Aesthetic cohesion across a board; weakest control of geometry | $10+/mo | `[O] [SRC-033] [SRC-036]` |
| **Anthropic — Claude (vision, analysis side)** | Vision API: multi-image input (up to 100/request), base64/URL/Files API; documented limits: better at structured extraction than handwriting/non-Latin | **The verifier's seat**: use a vision model to *list* what a plate claims — never to certify it (§3.7 evidence) | Claude plans + API | `[D] [SRC-073]` |

**Reading** `[N]`: the 2026 field has specialized. For architectural diagrams the three picks that matter are (1) **a reference-faithful editor** (Nano Banana Pro or Kontext-class) to restyle a lawful base without moving geometry; (2) **a text-capable generator with a vector escape hatch** (Recraft V3 Vector, Qwen-Image locally) for label-bearing diagram plates; (3) **a multi-reference model** (Seedream/Grok 5-ref) when a set of plates must share one visual language. Leaderboard position is *not* the criterion — see §3.7.

### 3.3 The AEC / GIS-native stack — the part v1 missed, and the part that answers "enhanced *vicinity map*" honestly `[D]/[O]`

Image models *paint* maps. AEC and GIS platforms *compute* plans. For anything that must be true, the platform layer is where the work belongs; the image layer only styles it afterwards.

| Platform | What it does (as documented) | Why it matters for vicinity/SDP work | Access | Grade |
|---|---|---|---|---|
| **Autodesk Forma "Site Design"** | Cloud, browser-only: contextual data + *"real-time AI analyses for noise, wind, embodied carbon and more"*; generative **site automation** explores building layouts against height/setback/density rules and returns environmental performance per option; Revit/Rhino interop via Forma Board | The industry's actual answer to "AI site design" — and it is **analysis-driven, not pixel-driven**: sun hours, wind comfort, noise, carbon are computed, not hallucinated | ~$185/mo standalone, free in AEC Collection (third-party pricing) | `[D] [SRC-089]`, `[O] [SRC-090] [SRC-091]` |
| **TestFit** | Real-time constraint-solving for site plans: *"starting from an AI-generated plan you can edit down to the last parking stall"*; **Site Solver** generates ~3,000 variations in seconds and ranks them by user KPIs (unit count, FAR, yield, parking ratio); zoning/setback/financial constraints | Feasibility-grade site layouts where every element is a **parameter**, not a painted shape — the anti-hallucination architecture | Enterprise (student-free unclear) | `[D] [SRC-101]`, `[O] [SRC-102] [SRC-103]` |
| **Esri ArcGIS — GeoAI + AI assistants** | Tier 1: purpose-trained geospatial models inside ArcGIS. Tier 2: natural-language **assistants** (three now GA, included with user types at no extra cost); ArcGIS is adding **MCP support so external agents call spatial tools** and receive *"results anchored to real geographic coordinates, infrastructure datasets, and demographic layers, rather than the ungrounded spatial approximations that generic LLMs produce"* | The sentence that summarises this whole research: grounded spatial answers vs plausible pixels | ArcGIS subscription (some assistants free with user types) | `[D] [SRC-092] [SRC-093]`, `[O] [SRC-094]` |
| **Mapbox — MCP server + agent toolkit** | *"Gives agents and LLMs structured access to the Mapbox location platform"* — distance, direction, nearby places; live map; 35+ mapping controls for agents | Programmatic, licence-clean base generation and place facts an agent can call instead of imagining | Mapbox account token (free tier) | `[D] [SRC-095]`, `[O] [SRC-096]` |
| **Trimble — SketchUp Diffusion** | Official extension: generate imagery *inside* SketchUp from the model, with **"respect model geometry"** and prompt-influence sliders; documented limits — no material control, no post-edit | The closest thing to *image-based prompting with your own geometry as the condition* for a student workflow | Extension Warehouse (free extension) | `[O] [SRC-098] [SRC-099] [SRC-100]` |
| **QGIS + prettymaps (open stack)** | QGIS Print Layout/Atlas renders **vector-styled** maps with scale bars, north arrows, attribute-driven labels, one-command batch export `[O] [SRC-062] [SRC-063]`. prettymaps draws styled maps straight from OSM data (osmnx + matplotlib + shapely; preset styles; AGPL-3.0) | **This is the lawful "condition image" factory**: your base map is vector-authored, attributed, reproducible — and then AI only restyles it | Free (AGPL for the library) | `[D] [SRC-111]`, `[O] [SRC-062] [SRC-063]` |

**Reading** `[N]`: the relevant pipeline for a *vicinity map* is **GIS/geodata → vector base → (optionally) AI restyle → vector labels**. The relevant pipeline for *concept diagrams* is **sketch/mass → image model → board**. Conflating them is where v1 was abstract and where projects get hurt.

### 3.4 Grounding — the fix for "the AI invented the geography" `[D]`

- **Google Maps grounding in the Gemini API**: a `googleMaps` tool whose response carries `groundingChunks` (uri, placeId, title) and `groundingSupports` linking response text to those sources — i.e. **inline citations for places**, built to be checkable; Google recommends pairing it with Search grounding for dynamic facts `[D] [SRC-077] [SRC-078]`.
- **Esri's framing** (above) is the same principle from the GIS side: agent tools return coordinates and datasets, not approximations `[O] [SRC-094]`.
- **Lawful base data, 2026 menu** `[O] [SRC-118] [SRC-119] [SRC-120] [SRC-130] [SRC-131] [SRC-132]`: **Overture Maps** (monthly releases, GeoParquet; per-theme licences — Places/Admin CDLA-Permissive-2.0, Buildings/Transportation ODbL because of upstream OSM), **Microsoft GlobalMLBuildingFootprints** (1.4 B footprints, ODbL), **Google Open Buildings** (CSV/GeoJSON, coverage incl. parts of Asia), **OSM** (ODbL, attribution), plus your own survey/CAD. PH coverage quality varies; verify against the actual LGU/lot data before trusting any footprint layer `[N]`.
- **What grounding does not do** `[N]`: it grounds *facts in text*, it does not measure your drawing. The radius ring, the scale bar and the hatched neighbours remain hand-verified — see §7's numbers.

### 3.5 The image-based prompt, sharpened (grammar + per-plate recipes)

The nine-slot grammar from v1 stands; v2 re-weights it per the 2026 evidence: **the condition image is the control; the words are the styling.**

```text
[1 SHOT]      flat orthographic top-down | axonometric 45° | section-cut | eye-level | aerial oblique
[2 SUBJECT]   <plate type> of <building/site type>, <component inventory>
[3 CONDITION] ATTACH <lawful base / CAD linework / sketch / prior frame>;
              PRESERVE: <explicit keep-list — geometry, ring, parcels, scale bar>
[4 STYLE]     flat vector, thin black outlines, editorial minimal, muted editorial palette
[5 PALETTE]   3–4 named colours + roles (water / parks / site / context)
[6 ANNOTATION]"no text" — labels, dimensions, title block added in vector afterwards
[7 SCALE]     graphic scale bar retained; no invented dimension strings
[8 NEGATIVES] no photorealism, no 3D, no gradients, no shadows, no invented labels, no UI, no composite
[9 FORMAT]    aspect ratio for the board zone; single image
```

**Recipe cards** (each is the *operational* unit the rejection asked for; `→` = tool class with the strongest cited support):

| # | Plate | Recipe | Tool class → | Verification burden |
|---|---|---|---|---|
| R1 | **Vicinity map (presentation upgrade)** | R1: OSM/Overture/GIS base → symbolise in QGIS → export vector PNG → *condition*: attach base, "preserve all road geometry, water, park shapes, the red site marker and the 2 km ring exactly; restyle only" → AI restyle → **re-overlay YOUR vector labels, north arrow, scale, title block** | reference-faithful editor (Nano Banana Pro / Kontext) `[D] [SRC-027] [SRC-029]` | full: geometry diff + scale audit (§7) + licence + disclosure |
| R2 | **SDP context plan** | CAD/survey linework → same preserve-list → AI *only* for tonal context (vegetation texture, ground pattern); hatch and distances drawn by hand in CAD | local-edit model, one element per pass `[D] [SRC-028]` | geometry diff; hatch/dimension audit |
| R3 | **Concept diagram pack** (program, circulation, exploded axo, massing) | sketch or massing frame → generate **8–10 plates in one session** with a fixed style reference; text excluded, added later | multi-reference model (Seedream/Grok 5-ref) + style refs `[O] [SRC-086] [SRC-074] [SRC-036]` | plausibility read only (no truth claim) |
| R4 | **Label-bearing analytical diagram** (zoning, phasing, sun paths) | generate background; **or** generate with labels on a vector-capable model and expect to redraw | Recraft V3 **Vector** (SVG out) `[D] [SRC-079]`; Qwen-Image if self-hosting `[O] [SRC-083]` | OCR pass + label redraw |
| R5 | **Render embellishment** of a model view | export SketchUp view → Diffusion with geometry-respect high → refine lighting only; keep a "no invented structure" negative | SketchUp Diffusion `[O] [SRC-098]`; Kontext local edits `[D] [SRC-029]` | side-by-side vs model |
| R6 | **Feasibility site layout (numbers matter)** | do **not** prompt this — run a constraint solver (TestFit) or Forma site automation, then style the output | TestFit / Forma `[D] [SRC-101] [SRC-089]` | KPI-level verification, not pixel-level |

### 3.6 Reference-image discipline (unchanged core, now with citations)

1. **The condition carries truth.** The published map-making pipeline masks *all* text in both raster and vector training data precisely so the model cannot invent labels; control comes from symbolised vector layers `[R] [SRC-037]`.
2. **Preserve by naming what must not change** — the documented idiom of the edit class `[D] [SRC-029]`; practitioner guides repeat it for photo-extension plates `[O] [SRC-034]`.
3. **Local edits, not re-rolls** — local editing exists to *"make targeted modifications of specific elements… without affecting the rest"* `[D] [SRC-028]`.
4. **Style lives in a reference image**, not adjectives — `--sref/--sw` (100–300) is the practitioner standard for board coherence `[O] [SRC-036] [SRC-033]`.
5. **Re-anchor when drift starts** — re-upload the best frame rather than continuing a drifting chain `[O] [SRC-034]`.
6. **Reduce the prompt, raise the condition.** Seedream's own guidance caps prompts at ~600 words to keep attention from scattering `[O] [SRC-086]`; OpenAI's guide says *name the required components and say what should not be included* `[D] [SRC-072]`.

### 3.7 Audits, benchmarks and field failures — the strength layer `[R]/[O]`

| Source class | What it measured | Finding that changes practice | Grade |
|---|---|---|---|
| **MapBench** (arXiv 2503.14607 + repo) | 1,649 map-reading queries over 100 human-readable maps (zoos, campuses, urban, mall, Google-Maps style) | LVLMs show *"critical limitations in spatial reasoning and structured decision-making"* on maps — a vision model reading your plate is a flagger, not a certifier | `[R] [SRC-106] [SRC-107]` |
| **LM Arena image editing, 7 categories** (Jul 2026) | 52 models, **28M+ human votes**; separate rankings for Photorealistic / Portraits / Cartoon / Art / 3D / Commercial Design / **Text Rendering** | The category split is the practical takeaway: a model can top portraits and be mediocre at text; the current leader's **largest margin is in Text Rendering** — pick by category, not by one Elo | `[O] [SRC-104] [SRC-105]` |
| **Qwen Q-Judger (Qwen-Image-Bench)** | Apache-2.0 judge model, 5 dimensions, structured JSON, **0.92 Spearman vs human raters** | Automated scoring is now cheap and open — useful for screening many plates, never for certifying one | `[O] [SRC-085]` |
| **GDELT map-hallucination experiments** | AI-generated world maps | Label pointers landed on wrong countries at scale; vision models *listed* errors well, but **no reliable autonomous correction loop** was found | `[O] [SRC-039]` |
| **Dagstuhl GIScience 2023** | Ethics of DALL·E-2 maps; detector study | Class list: unclear borders, deformation, unanticipated features, irreproducibility; an AI-map detector reached ≈0.87–0.91 accuracy/F1 | `[R] [SRC-038]` |
| **Hasselblad Masters 2026** (May 2026) | Real competition | A finalist was **disqualified** after AI forensics — the "AI tell" was typography on a bottle *"that looks… suspicious"* | `[O] [SRC-115] [SRC-116]` |
| **GPT-4V engineering-design benchmark (AI EDAM)** | Spatial reasoning tests | 36 % and 18 % accuracy on packing/rotation (≈ random); blind-vs-through-hole judged correctly **11 %** of the time | `[R] [SRC-044]` |
| **Construction-progress GPT-4V study** | Aerial site photos | Good at naming stages/materials; **cannot localise** — misidentified machinery, misread debris | `[R] [SRC-045]` |
| **Vector-floorplan research line** (HouseDiffusion CVPR 2023, GSDiff, Graph2Plan repo) | Floorplan generation as **vectors** with topology constraints | The research answer to "trustworthy plan generation" is constraint/vector based — not pixel diffusion; and even there, alignment failures (gaps, overlaps) are documented | `[R] [SRC-108] [SRC-109]`, `[D] [SRC-110]` |
| **Social practice threads (r/Architects, r/LandscapeArchitecture, r/architecture)** | What practitioners actually do | *"AI-generated plans can look plausible at first glance… rooms with no doors, corridors that lead nowhere, bathrooms with two toilets but no sink"*; site plans specifically: *"I use it for 3D renderings but **never site plans**… a lot of Photoshop work after"*; and TestFit seen *"lay out whole site plans in real time"* in offices | `[O] [SRC-127] [SRC-128] [SRC-129]` |

**Cross-cutting reading** `[N]`: independent measurement, competition forensics and practitioner experience agree on one distribution — **AI is strongest where the deliverable is an impression, weakest where the deliverable is a measurement.** Every recipe in §3.5 is placed on that distribution, not on enthusiasm.

### 3.8 Licensing, custody, and provenance — 2026 update

**Base custody (unchanged from v1, now with the open-data menu):** Google Maps ToS §10.5 bars derivative work and explicitly lists *"tracing or copying… building outlines"* `[D] [SRC-023] [SRC-024]`; OSM repeats the ban from its side `[D] [SRC-025]`. Lawful bases: **OSM** (attribution "© OpenStreetMap contributors" + ODbL statement) `[D] [SRC-025]`; **Overture** themes (Places/Admin under CDLA-Permissive-2.0 — *no* share-alike; Buildings/Transportation under ODbL because of upstream OSM) `[O] [SRC-118] [SRC-119] [SRC-120]`; **Microsoft footprints** (ODbL) `[O] [SRC-130] [SRC-131]`; **Google Open Buildings** (open terms, CSV/GeoJSON) `[O] [SRC-132]`; your own survey/CAD. **Software licences ≠ output licences:** prettymaps is **AGPL-3.0** — the rendered map image carries OSM attribution duties, while distributing a *modified pipeline* triggers source-disclosure `[D] [SRC-111]`, `[N]`.

**Marking and disclosure — moving from etiquette to law:**
- **EU AI Act Article 50 applies from 2 August 2026** (fines to €15 m / 3 % of turnover): providers must mark synthetic image/audio/video/text outputs in a **machine-readable, detectable** way; **deployers must disclose** deepfakes; marking obligations for systems already on the market run from 2 December 2026; artistic/satirical work has limited exceptions `[O] [SRC-112] [SRC-113] [SRC-114]`.
- **Implementation reality:** SynthID is mandatory on all Gemini API image outputs `[D] [SRC-076]`; **C2PA Content Credentials** adoption is partial in 2026 — OpenAI layered C2PA + SynthID (May 2026), Google is rolling verification into Gemini/Search/Chrome, Canon shipped a C2PA newsroom workflow — **but as of mid-2026 no dedicated camera had achieved C2PA Conformance-Program compliance**, and there is a version rift (several makers on 1.4) `[O] [SRC-124] [SRC-125]`; institutions are already deploying it (Austrian Parliament, Sep 2026) `[O] [SRC-126]`.
- **Competition/education regimes:** ASAI AIP 40 — AI-influenced images *"MUST be labeled"* `[D] [SRC-048]`; ASCE 2026 requires an **AI Use Log** and treats uncited generative use as plagiarism `[D] [SRC-049]`; competition guidance warns AI images may face **ownership and disqualification** problems because entrants must hold rights in submitted imagery `[O] [SRC-117]`; and the field has already seen a disqualification `[O] [SRC-115]`.
- **Philippines:** no single AI statute yet — governance currently runs through strategic roadmaps + **National Privacy Commission guidelines on personal data in AI** + **COMELEC Resolution 11064 on electoral deepfakes**, with multiple bills pending (HB 10567 Deepfake Accountability; HB 10362 AI Governance Act; HB 2827 AI Bill of Rights; HB 7396/7913/7983/9448) `[O] [SRC-121] [SRC-122] [SRC-123]`. Professional practice: architectural review/signature remains an RLA function `[D] [SRC-020] [SRC-052]`, and AI is already inside PRC-recognised CPD `[D] [SRC-051]`.
- **The practical rule for a student submission today:** disclose in the title block (*"Concept imagery produced with <tool>, <date>; geometry and annotations author-drawn"*), retain the unedited original + its metadata, and prefer tools whose outputs carry provenance (`[D] [SRC-076] [SRC-081]`) rather than tools that strip it.

### 3.9 What practitioners and offices are actually doing `[O]` (social layer, capped grades)

| Thread | Signal |
|---|---|
| r/Architects — *AI in Architecture* (2025) | Consensus: *"presentation assistant"* — concept images and render enhancement; plans remain untrustworthy | `[O] [SRC-127]` |
| r/LandscapeArchitecture — *rendered plans* (2025) | Renderings yes; **site plans no**; seamless textures are an underrated, safe use; firms training AI on their own past work for style | `[O] [SRC-128]` |
| r/architecture — *office deployment* (2024) | TestFit already laying out site plans in offices; space/massing generators used for studies | `[O] [SRC-129]` |
| Mapbox on X | MCP server positioned as *"a full toolkit for building spatially-aware agents"* — the platform layer advertising itself to AI, not the reverse | `[O] [SRC-097]` |

*Grade cap applied (I.2): forum and social matter enters at `[O]`/`[N]` and is used here as *practice signal*, never as technical proof.*

---

## 4. ANALYSIS STRUCTURES

### 4-A The operational matrix — *use this for that* (request → tool → verification)

| You need… | Kept honest by… | Style it with… | Then verify with… |
|---|---|---|---|
| A lawful base map of a real site | OSM / Overture / MS footprints / own survey | QGIS Print Layout (vector) or prettymaps | attribution line + coordinates check |
| A **restyled** nice-looking vicinity sheet | your vector base as the condition | Nano Banana Pro / Kontext preserve-list pass | §7 audit (scale, ring, labels) + OCR |
| Place facts (what is 1.2 km away, what is the street called) | **grounded** answers, not generated ones | Gemini Maps grounding / Mapbox MCP / a map you read yourself | each fact cited to a source `[D] [SRC-077]` |
| A feasibility site layout | constraint solver (TestFit) or Forma automation | the tool's own drawing output | KPIs, not pixels |
| A board-coherent concept diagram set | a fixed style reference + multi-ref model | Seedream / Grok / Midjourney sref | read-through for plausibility |
| Editable vector diagram output | Recraft V3 **Vector** (SVG) or Qwen-Image → trace | vector-capable generator | node/geometry sanity in a vector editor |
| Renders of your own model | your model as condition | SketchUp Diffusion (geometry-respect) / Kontext | side-by-side against the model |
| A plate set that survives an ethics review | provenance-carrying tools (SynthID/C2PA) + disclosure block | Firefly (commercially-safe line) or Gemini | metadata + disclosure line present |

### 4-B Diagram-type × AI-role (verdict table, unchanged in substance, now cited)

| Plate | AI role | Condition required | Failure class to police |
|---|---|---|---|
| Vicinity map / location plan | presentation restyle **only** | lawful geodata base | invented geography/labels `[O] [SRC-039]`, `[R] [SRC-038]`; scale drift (§7) |
| Site development plan | restyle context tone; **no** new elements | CAD linework | invented neighbours, false hatching |
| Sections / elevations | styling aide | control drawing | dimension creep |
| Exploded axo / program / circulation / concept | **generate**, freely | sketch/mass frame optional | plausible-but-meaningless geometry — harmless here |
| Materials/context studies, moodboards | generate | none | bias/homogenisation `[R] [SRC-047]` |
| Details, schedules, dimensions | none | — | all of them |

### 4-C Failure taxonomy → mitigation (now with measured instances)

| Failure | Evidence | Mitigation |
|---|---|---|
| Invented geography | `[O] [SRC-039]`, `[R] [SRC-038]` | never generate the geographic layer; ground facts (`[D] [SRC-077]`) |
| Painted text = unverifiable claim | `[D] [SRC-071]` (OpenAI explicitly warns to verify labels), `[D] [SRC-029]`; **measured in §7** (5 label blocks, invented values) | "no text" + vector overtype + OCR pass |
| **Internal scale inconsistency** | **measured in §7: ring/scale error 18.6 %** | §7 audit harness before any submission |
| Vector-looking raster | **measured in §7** (39,902 colours, 72 dpi chunk) | demand SVG/DXF; Recraft Vector or re-draw |
| Unmarked/unattributed output | **measured in §7** (no C2PA/EXIF) | use provenance tools `[D] [SRC-076]`, keep disclosure line `[O] [SRC-112]` |
| Drift across iterations | `[D] [SRC-028] [SRC-029]` | local edits + re-anchor |
| Style loss across a board | `[O] [SRC-036]` | style reference + fixed seed/reference frame |
| AI-checking-AI false confidence | `[R] [SRC-044] [SRC-045] [SRC-106]` | vision pass may FLAG; certification stays deterministic |
| Disqualification risk | `[O] [SRC-115] [SRC-117]` | read the brief's AI clause; disclose; keep originals |

### 4-D The six-stage pipeline (v2 — grounding and audit inserted)

```text
1 CUSTODY   choose a lawful base + note its licence and attribution text      [D 023/025/118]
2 GROUND    facts from grounded sources (Maps grounding / GIS / map reading);  [D 077]
            never from generation
3 CONDITION vector-author the base: line weights, palette, ring, scale bar,
            NO TEXT                                                        [R 037; D 029]
4 GENERATE  nine-slot prompt (§3.5); local edits only; labels off             [D 028/029]
5 VERIFY    plate_audit.py → format/provenance/scale/ring/base checks          [I this session]
            + OCR + vision-flag pass + geometry diff vs base + licence +
            disclosure/provenance
6 PLATE     vector labels, north arrow, scale, title block, attribution &
            disclosure line
```

### 4-E Cost & access reality (student lens; third-party prices, 90-day decay class)

| Option | Free path | Paid path | Relevancy note |
|---|---|---|---|
| Gemini app (Nano Banana) | ✅ free with daily limits `[O] [SRC-133]` | API $0.134–0.24 img `[O]` | best reference-fidelity free option |
| ChatGPT images (GPT-Image) | ✅ limited free | API per image `[D] [SRC-071]` | strongest documented diagram guidance |
| Grok Imagine | app access | $0.04/img API `[D] [SRC-074]` | cheapest frontier API + 5 refs |
| Qwen-Image / Edit | ✅ **local, free (Apache-2.0)** `[O] [SRC-083]` | fal.ai if no GPU | licence-clean, text-strong; needs GPU |
| Recraft | ✅ free tier `[D] [SRC-079]` | $0.08/vector img | **SVG output** |
| Midjourney | ❌ | ~$10+/mo `[O] [SRC-033]` | cohesion, not control |
| Forma / TestFit / ArcGIS | ❌ (Forma free w/ AEC Collection `[O] [SRC-091]`) | ~$185/mo / enterprise `[O]` | the professional layer for real site work |
| QGIS + prettymaps + OSM | ✅ free `[D] [SRC-111]` | — | the lawful base factory |

---

## 5. CONFLICTS & UNCERTAINTIES

| # | Position A | Position B | Status |
|---|---|---|---|
| 1 | Vendor capability claims (diagram text, precision) `[D] [SRC-027] [SRC-079]` | Independent measurement: small/rotated text unreliable; LVLM map-reading limitations `[O] [SRC-032]`, `[R] [SRC-106]` | **OPEN** — solved for posters, not for legal annotation. Recipes R1/R4 route around it. |
| 2 | Adobe markets Firefly as *"commercially safe"*, trained on licensed/public-domain content `[D] [SRC-081]` | Reported allegation that Firefly was also trained on competitor-generated images, which would undercut the claim `[O] [SRC-082]` | **OPEN** — preserved side-by-side (I.5). Practical posture: treat "commercially safe" as a vendor claim to be read against its FAQ, not as a warranty. |
| 3 | Overture described as CDLA-permissive `[O] [SRC-118]` | Theme-level reality: Buildings/Transportation are ODbL due to OSM lineage `[O] [SRC-119] [SRC-120]` | **RESOLVED as licence-by-theme** — the schema is per-theme; read the attribution page per dataset. |
| 4 | Open-data footprint layers look authoritative (1.4 B footprints) `[O] [SRC-130]` | ML-derived footprints are unverified against cadastre; PH coverage quality varies `[N]` | **OPEN — declared**: verify against the lot data before drawing any boundary claim. |
| 5 | EU AI Act marking becomes law Aug 2026 `[O] [SRC-112] [SRC-113]` | C2PA adoption partial, version rift, no conformant cameras mid-2026 `[O] [SRC-125]` | **OPEN** — the duty is real before the tooling is uniform; disclosure by the author remains the reliable move. |
| 6 | Leaderboards rank one model #1 in all seven categories `[O] [SRC-104]` | Category margins matter more than rank; your task may sit at a margin `[O]` | **OPEN** — use categories, not aggregate Elo. |
| 7 | [UNVERIFIED] Third-party pricing (Forma $185, Grok $0.04, Nano Pro $0.134–0.24, Midjourney $10+) | — | **DECLARED** — volatile class, 90-day decay; re-check before budgeting. |
| 8 | v1's normative framing (what the law requires) | v2's operational framing (what to run) | **RESOLVED by rejection direction (IV.1)**: v2 leads operational; the legal baseline stays as §3.1 because the recipes depend on it. |

---

## 6. INCUBATION (`[S]` — parked, inadmissible as fact)

1. `[S]` **Plate-grammar as a `styles/` skeleton** — the nine-slot grammar + recipe cards as a proposal (🟠, needs Commander ratification; not this session).
2. `[S]` **`plate_audit.py` as a repo script** under `scripts/` + CAPABILITIES inventory entry — currently a session artifact in `outputs/`; promotion needs the capability-registry path `[I]`.
3. `[S]` **A "grounded vicinity" mini-workflow** for AR173-1P studio exercises: maps-grounding facts + QGIS base + restyle + §7 audit, run once end-to-end as coursework evidence.
4. `[S]` **Disclosure line as board standard** for any AI-touched plate, pre-empting the ASAI/ASCE/competition class before it bites.

---

## 7. EXECUTED AUDIT — the strength test, on my own artifact `[I]`

**Harness:** `outputs/2026-09-29_plate_audit.py` (stdlib + PIL + numpy; every threshold documented; exit 0/1/2). **Raw result:** `outputs/2026-09-29_plate_audit_results.json`. **Subject:** this session's demo plate `outputs/2026-09-29_demo-vicinity-map-plate.png` (the same invented-imagery prompt-receipt as v1 — kept precisely so the audit can be re-run by anyone).

| Check | Method | Measured | Verdict |
|---|---|---|---|
| **A1 format/print** | mode; DPI chunk; unique colours | RGB 1254², DPI chunk **72**, **39,902 unique colours** | **FAIL** — raster masquerading as "vector-style"; no SVG/DXF; below 150-dpi print guidance |
| **A2 provenance** | PNG chunks + EXIF + C2PA hint scan | only a `dpi` key; **no EXIF, no C2PA, no generator metadata** | **FAIL** — the file is unsigned/unmarked (the exact gap EU AI Act Art. 50 (Aug 2026) is about) |
| **A3 scale bar** | alternating-block detection; two independent derivations | bar row 1011; blocks 57/56/57/57 px; period 111.0 px → **222.0 px/km** (periodicity) vs **222.3 px/km** (black-span) → agree | **PASS** (internal consistency of the printed scale) |
| **A4 ring vs scale** | dashed red ring vertical extent vs printed scale | ring **723 px**; at the printed 222 px/km a 2-km radius must be **888 px** → ratio 0.814 → **implied radius 1.63 km → 18.6 % error** | **FAIL** — the plate's own "2 km" annotation is wrong at its own printed scale |
| **A5 base diff** | is there a conditioning base to diff against? | none (invented imagery) | **FAIL** — geometry cannot be falsified; *an AI plate without a base is an unfalsifiable claim that happens to look like a drawing* |

**Harness self-audit (kept in the record):** run #1 reported a 40 % inconsistency — **my own px-per-km arithmetic was wrong**; the corrected harness cross-derives the scale two independent ways before computing A4 and now agrees to 0.13 %. Lesson filed to `learnings.md`: *a verifier that cannot be checked is decoration.*

**What this audit proves for the Commander:** (1) the failure modes the literature predicts are **present and measurable in a one-prompt plate** — invented labels, no provenance, a scale annotation that contradicts its own graphic scale; (2) verification is **cheap and deterministic** — 60 lines and two seconds produced findings no amount of prompt craft would have surfaced; (3) therefore the §4-D pipeline's step 5 is not bureaucracy, it is the difference between a drawing and a plausible picture.

**Vision-pass ledger (declared method, grade `[O]`-class, not machine-certified):** a visual read of the plate enumerates 5 text blocks ("RIVERSIDE PARK 1.2 km", "CITY MUSEUM 1.6 km", "HARBOR TERMINAL 1.8 km", "S E A", "VICINITY MAP"), a title block with an invented date (*"MAY 20, 2024"*) and invented scale ("AS SHOWN"), a north arrow, and a 0–2000 m scale bar. Per §3.7 (`[R] [SRC-044] [SRC-045] [SRC-106]`), this read may **flag**, never **certify** — which is why the numeric checks above carry the verdict.

---

## 8. REFERENCE LIST — v2 acquisition block (SRC-071 … SRC-132)

### PRIMARY (provider/platform/official documentation, contracts, repos)
| ID | Source | Tier |
|---|---|---|
| SRC-071 | OpenAI — *Image generation* guide (platform.openai.com): size/quality/format parameters; dense-label guidance | vendor doc |
| SRC-072 | OpenAI — *Image prompting* guide (developers.openai.com): diagram instruction — *"verify labels and factual relationships as well as appearance"*; `quality:"high"` for dense labels; `input_fidelity` | vendor doc |
| SRC-073 | Anthropic — *Vision* (Claude API docs): multi-image inputs, limits, Files API | vendor doc |
| SRC-074 | xAI — *Imagine Overview* (docs.x.ai): generate + edit, **up to 5 reference images**, $0.04/image, 1K/2K | vendor doc |
| SRC-075 | xAI — *Image Generation* capability docs: aspect ratio, resolution, quality, batch | vendor doc |
| SRC-076 | Google — *Nano Banana image generation* (ai.google.dev Gemini API): *"All generated images include a SynthID watermark"* | vendor doc |
| SRC-077 | Google — *Grounding with Google Maps* (Gemini API): `googleMaps` tool; `groundingChunks`/`groundingSupports` | vendor doc |
| SRC-078 | Google Cloud — *Grounding API* reference: Google Maps grounding parameters and metadata | vendor doc |
| SRC-079 | Recraft — *Recraft V3* model docs: text positioning; **Vector variant → editable SVG**; $0.04/$0.08 per image | vendor doc |
| SRC-080 | Recraft — *Introduction* docs: model generations and variants | vendor doc |
| SRC-081 | Adobe — *Firefly FAQ*: licensed/public-domain training; commercial use; Content Credentials | vendor doc |
| SRC-089 | Autodesk — *Forma Site Design* product page: real-time AI analyses; generative site automation | vendor doc |
| SRC-092 | Esri — *What's new in AI assistants* (June 2026): three assistants GA, included with user types | vendor doc |
| SRC-093 | Esri — *What's new in AI assistants* (February 2026): role-based privilege; assistant roster | vendor doc |
| SRC-095 | Mapbox — *2025 year in review*: MCP server giving agents structured geospatial access | vendor doc |
| SRC-101 | TestFit — site planning product page: *"Automate Site Plans"*, editable AI-generated plan | vendor doc |
| SRC-111 | GitHub — **prettymaps** (marceloprates): osmnx+matplotlib+shapely map drawing; **AGPL-3.0** | repository |
| SRC-107 | GitHub — **MapBench** (taco-group): benchmark code/dataset for LVLM map reading | repository |
| SRC-110 | GitHub — **Graph2plan** (HanHan55): graph-based floorplan generation implementation | repository |

### RESEARCH (papers, benchmarks, audits)
| ID | Source | Tier |
|---|---|---|
| SRC-106 | arXiv 2503.14607 — *Can Large Vision Language Models Read Maps like a Human?* (MapBench; 1,649 queries; 100 maps) | paper |
| SRC-108 | Shabani et al. — *HouseDiffusion: Vector Floorplan Generation…* (CVPR 2023) | paper |
| SRC-109 | *GSDiff: Synthesizing Vector Floorplans via Geometry…* (2025) — Graph2Plan/House-GAN++ limitations | paper |
| SRC-112 | bratby.law — *AI Act Article 50 Explained* (duties from 2 Aug 2026; fines to €15 m / 3 %) | legal analysis `[O]` |
| SRC-113 | hard2bit — *AI Act Article 50: AI transparency from 2 August 2026* (machine-readable marking; 2 Dec 2026 for systems on market) | legal analysis `[O]` |
| SRC-114 | wasitaigenerated — *Article 50 for AI content detection* (marking as legal hook behind SynthID/C2PA; deployer disclosure) | legal analysis `[O]` |

### AUDITS & MEASUREMENT
| ID | Source | Tier |
|---|---|---|
| SRC-104 | AlphaSignal — *LM Arena image editing: 7 categories, 52 models, 28 M+ votes; largest margin in Text Rendering* | measurement `[O]` |
| SRC-105 | awesomepapers — Text-to-Image Arena leaderboard snapshot (2026-09-11) | measurement `[O]` |
| SRC-085 | aiweekly — Qwen **Q-Judger** (Qwen-Image-Bench): Apache-2.0 judge, 0.92 Spearman | measurement `[O]` |
| SRC-115 | PetaPixel — *AI-Generated 'Photo' Disqualified From Hasselblad Masters 2026* | journalism `[O]` |
| SRC-116 | DIYPhotography — same event, detail: typography as the AI tell | journalism `[O]` |

### PLATFORM / PRACTICE / SOCIAL
| ID | Source | Tier |
|---|---|---|
| SRC-083 | Local AI Master — Qwen-Image local guide (20B MMDiT, Apache-2.0, EN+CN text rendering; 2512 refresh) | `[O]` |
| SRC-084 | qwenimage-2.com — Qwen Image overview (Apache-2.0; bilingual text; 2K; LoRA) | `[O]` |
| SRC-086 | Hedra — Seedream 4.0 model page (≤6 refs; 4K; official prompt structure; ≤600 words) | `[O]` |
| SRC-087 | Replicate — Seedream 4.0 (unified gen+edit; *"accurate diagrams or timelines with labeled details"*) | `[O]` |
| SRC-088 | C# Corner — Seedream 4.0 overview (inpaint/outpaint; multi-ref fidelity) | `[O]` |
| SRC-090 | Illustrarch — *Autodesk Forma Review 2026* (sun/wind/noise/carbon; site automation) | `[O]` |
| SRC-091 | CreativeToolsAI — Forma guide (pricing ~$185/mo; Revit/Rhino integration) | `[O]` |
| SRC-094 | TechTimes — *GIS Meets Agentic AI: Esri UC 2026* (GeoAI tier; MCP; grounded vs ungrounded spatial answers) | `[O]` |
| SRC-096 | Highways.today — Mapbox *"Giving AI a Sense of Place"* (MCP; agent toolkit; 45,000 apps) | `[O]` |
| SRC-097 | X — @Mapbox post on the MCP server | social `[O]` |
| SRC-098 | BIM Chapters — SketchUp Diffusion launch walkthrough (geometry-respect slider) | `[O]` |
| SRC-099 | Dezign Ark — SketchUp Diffusion (extension download) | `[O]` |
| SRC-100 | PromeAI — SketchUp Diffusion guide (documented limits: no material control, no edit) | `[O]` |
| SRC-102 | Illustrarch — *TestFit Review* (Site Solver ≈3,000 variations in ~3 s; KPI ranking) | `[O]` |
| SRC-103 | Zeitgeist — TestFit profile (constraint solving; cycle-time claim) | `[O]` |
| SRC-117 | architecturecompetitions.com — AI images in competition submissions (ownership; disqualification risk) | `[O]` |
| SRC-118 | GeoDataViewer — Overture Maps guide (CDLA-Permissive-2.0 vs ODbL by theme; monthly releases) | `[O]` |
| SRC-119 | PeaceLoveFreedom — Overture licensing analysis (buildings/transport ODbL history) | `[O]` |
| SRC-120 | gridisnotajournal — Overture interview (per-theme licences; ML building data) | `[O]` |
| SRC-127 | Reddit r/Architects — *AI in Architecture* (presentation-only consensus; "no doors" plans) | social `[O]` |
| SRC-128 | Reddit r/LandscapeArchitecture — rendered-plans thread ("never site plans"; textures) | social `[O]` |
| SRC-129 | Reddit r/architecture — office deployment thread (TestFit live site plans) | social `[O]` |
| SRC-082 | Wikipedia — *Adobe Firefly* (contested "commercially safe" claim) | `[O]` |
| SRC-124 | EyeSift — C2PA adoption status 2026 (OpenAI C2PA+SynthID May 2026; Canon; partial support) | `[O]` |
| SRC-125 | Wikipedia — *Content Credentials* (C2PA 1.4 rift; no camera conformance as of mid-2026) | `[O]` |
| SRC-126 | BroadbandTVNews — Austrian Parliament deploys C2PA credentials (2026-09-24) | `[O]` |
| SRC-121 | regulations.ai — Philippines AI regulation overview (NPC guidelines; COMELEC Res. 11064; pending bills) | `[O]` |
| SRC-122 | Manila Bulletin — HB 10362 AI Governance Act filed (Diokno, 2026-08) | `[O]` |
| SRC-123 | BusinessMirror — HB 2827 AI Bill of Rights | `[O]` |
| SRC-130 | DeepWiki — Microsoft GlobalMLBuildingFootprints overview (1.4 B footprints; ODbL) | `[O]` |
| SRC-131 | Archive.org mirror — Microsoft buildings license statement (ODbL) | `[O]` |
| SRC-132 | datos.gob.es — Google Open Buildings comparative note (CSV/GeoJSON; Asia coverage) | `[O]` |
| SRC-133 | Zenn (sora_biz) — *Watch Out for That Watermark*: Gemini API image-generation guide (API has no free tier; SynthID automatic; commercial use not prohibited; Nano Banana Pro 4K ≈$0.134–0.24) | `[O]` |

**Registry after v2:** **133 rows total** (SRC-001…SRC-133). This campaign (S012) contributed **114**: v1 = 27 primary + 24 secondary; v2 = 25 primary/primary-type (provider docs, repos, papers, legal analyses) + 38 secondary/analysis/social. @Gather (10+18) and @Radiation (12+20) floors exceeded.

**Note:** the v1 acquisition block (SRC-020…SRC-070) is registered in `01-research/REFERENCES.md` by the v1 patch and remains valid; v2 cites forward to it where still load-bearing rather than duplicating rows.

**Citation-field self-audit (v2):** **92 distinct sources** cited in-text across §3–§7 (243 citation mentions total); every cited ID appears in this list, and every listed ID's role is stated. **v1 retention:** v1's SRC-020…SRC-070 remain valid and are cited where still load-bearing (the legal baseline, licensing custody, disclosure regimes, the research pipelines).

---

## 9. LIMITS LINE

This research does **not** establish: admissibility of any AI-touched plate to any Building Official (the law reserves authorship/review to an RLA `[D] [SRC-020] [SRC-052]`); correctness of third-party prices and version numbers (volatile `[O]`, 90-day decay); quality claims for tools I did not execute directly except the Generative AI agent images and the audit harness `[I]`; PH geodata coverage quality `[N]`; any model ranking beyond the cited leaderboard snapshot; the truth of vendor "commercially safe"/"state-of-the-art" claims — those are vendor assertions held against independent evidence in §5. The §7 audit certifies **internal consistency of one demo plate only**; it is not a survey, not a stamp, and not transferable to any other image. Nothing here is a Nota; nothing entered the Core.

*Sentinel signature: every numeric claim in §7 is reproducible from `outputs/2026-09-29_plate_audit.py` + `outputs/2026-09-29_plate_audit_results.json`; every source claim traces to §8; every `[S]` is quarantined to §6.*
