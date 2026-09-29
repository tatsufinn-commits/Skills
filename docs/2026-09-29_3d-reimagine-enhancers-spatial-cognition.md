# RESEARCH — 3D Re-Imagine Prompt Enhancers, Spatial Cognition, Quality & Relevancy
## How re-image prompts work — and how to apply that to architectural re-imagination

> **Session:** S012 · 2026-09-29 · Arena AI (Agent Mode) · RADIATION v3.10.40-candidate
> **Commander's brief (verbatim):** *"@[Autopilot] | STYLE: [AUTO] | TOPIC: [Research regarding 3d re-imagine prompt enhancers, spatial cognition, quality and relevancy to the user's request. our goal is to understand how re-image prompt works and how can we apply it to architectural based prompt re-imagination. refer to sources such as {Researches, LLM audits/reports/findings, Provider Sourced information, Github Repositories, Relevant sournces, Social Media post relevance, Credible Websites and others you may apply.]]"*
> **Mode:** @Autopilot — focus change under the same session; one Scan Declaration covers the chain @Gather (8 batches / ~30 queries) → @Data (62 sources, SRC-186…SRC-247) → @Execute (3-run 3D experiment) → @Deliver.
> **Style:** `research.md` **[AUTO]** + the carried-over declared addition: **§6 EXECUTED EXPERIMENT** (the brief asks how enhancers work AND how quality/relevancy is measured — assertions would not answer it).
> **Relation to prior legs:** v2 survives as the platform/audit layer; the blind-spot leg as the rights/custody layer; this leg is the **mechanism + cognition + measurement** layer. **v3 = v2 + blind-spot leg + this + the Commander's incoming photo-re-imagine handoff.**
> **Grades:** `[D][O][I][R][N][S]`. No Nota. No Core write.

---

## 1. THE MODEL — how a re-image prompt actually works (the one diagram to remember)

A "re-image prompt" is not one instruction. It is up to **five signal channels** entering a diffusion/transformer UNet at different layers, with a strict authority hierarchy:

```text
        YOUR REQUEST (intent)                       THE INPUT IMAGE (reality)
              │                                           │
   ┌──────────┴──────────┐                    ┌───────────┴────────────┐
   │ text prompt         │                    │ latent img2img (noise) │  ← how much of the input
   │ → CLIP/T5 encoder   │                    │ denoise 0.35–0.55 keeps │    survives, per pixel
   │ → cross-attention   │                    │ 0.6+ = makeover         │
   └──────────┬──────────┘                    └───────────┬────────────┘
              │                                           │
     ┌────────▼─────────┐                     ┌───────────▼────────────┐
     │ IP-Adapter       │  style/mood          │ ControlNet family     │  geometry: Canny, depth,
     │ image → CLIP emb │  (space-agnostic)    │ (spatial conditioning)│  normal, MLSD, segmentation
     │ → cross-attn     │  scale 0.5–0.7       │ weight 0.6–1.0        │  (>1.3 artifacts)
     └────────┬─────────┘                     └───────────┬───────────┘
              └──────────────┬──────────────────────────────┘
                             ▼
                THE AUTHORITY LADDER (who wins when signals disagree):
                explicit 3D condition  >  spatial ControlNet  >  image embedding  >  text
                             │
                   conflict rule (documented, not folklore):
                   "the model satisfies one and ignores the other —
                    the structural signal will win" [O SRC-212]
```

**Four consequences** that everything below depends on `[R]/[O]`:
1. **Text alone cannot hold geometry.** Any prompt longer than a style direction is spent on something the model will re-roll; the reliable geometric channels are the *input* channels (denoise, ControlNet, embedding). This is the mechanical reason the previous leg's preserve-list worked: it converts text into a **preserve instruction the model can reconcile with the input channel**, which is one of the few semantic jobs text still does in img2img.
2. **Each channel has a calibrated strength.** IP-Adapter 0.3–0.4 = hint, 0.5–0.7 = style transfer, 0.8+ = "your prompt barely matters"; combined conditioning scales should sum ≈1.0–1.3 or the model has no room left for text `[O SRC-210] [O SRC-211]`. img2img denoise is the survival dial: 0.35–0.55 strong retention, 0.6+ makeover `[O SRC-160]`.
3. **3D awareness today = depth/normal/mask tokens + camera conditioning, not "understanding space."** Current spatially-aware systems literally decompose 6DoF object pose into *2D mask + composited depth + orientation features* and train the diffusion transformer to follow them (SpatialHand, ICLR 2026 submission — and its baseline test found GPT-4o, Gemini-2.0-Flash and Nano Banana provide only 2D positional control) `[R SRC-187]`. SmartSpatial (IJCAI 2025) does the same with depth injection + cross-attention control, no fine-tuning, and ships SpatialPrompts/SmartSpatialEval exactly because "in front of / behind" is a known failure class `[R SRC-190]`. Even industrial-grade 3D-aware pipelines (e.g., virtual try-on) gain their fidelity by augmenting 2D cues with **depth/normal maps** as explicit geometry `[R SRC-186]`.
4. **Instruction editors move the same levers under the hood** — a vision-language encoder reads your image (semantic control) plus a pixel path preserves appearance (VAE path), which is precisely why "preserve" and "change" are separable instructions in 2026 editors and why spatial slips still occur when the two paths disagree `[O — v2 corpus, SRC-163]`.

---

## 2. PROMPT ENHANCERS — the emerging machinery, classified by evidence

"Enhancer" now means four different things. Conflating them is how students get worse prompts, not better.

### 2.1 Research enhancers (peer-reviewed class) `[R]`

| System | Mechanism | What it measurably does | Take-away |
|---|---|---|---|
| **PromptEnhancer** (arXiv 2509.04545; CVPR 2026) | Chain-of-thought rewriting trained against **AlignEvaluator** — a reward model scoring 24 key points in 6 categories (linguistic, attributes, composition, knowledge, text/layout) | Consistent prompt-adherence gains across mainstream T2I backbones, plug-and-play, no weight changes; qualitative: rewriting **changes content** (binds attributes, fixes layout), not just adds adjectives | Enhancement is a *reasoning* act about failure modes, not verbosity `[R SRC-204/206]` |
| **APE** (arXiv 2606.00204, 2026) | Post-trains small language models as enhancers with RL (GRPO); **SAPE** = single-pass rewrite; **MAPE** = router → rewriter → composer for compositional/editing constraints | SAPE alone gives substantial alignment gains; MAPE’s routing decisions ("rewrite-field selection and necessity") are what make editing-time enhancement work; rewards come from the downstream image, not text similarity | For edits, the enhancer must decide **what NOT to rewrite** — the same conclusion as our preserve-list `[R SRC-205] [O SRC-207]` |
| **Input-side rewriting with iterative DPO** (arXiv 2510.12041) | LLM rewrites trained toward composite rewards; best results reported with Llama-3-70B-Instruct as the rewriter | Rewrites **transfer across T2I backbones** (train/test mismatch barely hurts); short user prompts systematically underperform because training captions are longer — expansion closes a *distributional* gap | A generic LLM can be a legitimate enhancer; the gain is partly distribution repair `[R SRC-209]` |
| **DALL·E 3’s original architecture** (referenced class) | Auxiliary captioner trained to re-caption images *as if* a user had asked for them — the provider-side origin of today’s "enhance" buttons `[R SRC-208]` | — | Enhance is an old trick; what’s new is that it’s now user-visible and editable |

### 2.2 Provider-shipped enhancers `[D]`

- **Adobe Firefly (Image 4 / 4 Ultra):** "Prompt enhancement" is **on by default**; the UI exposes a **"Show enhanced"** button so you can read and edit the rewritten prompt before/after generation `[D SRC-237]`. That inspect-and-edit affordance is the responsible pattern — and the one to demand.
- **ChatGPT / GPT Image line:** prompt rewriting is internal; provider documentation and its system-card addendum frame the model as following detailed instructions and rendering **instructional diagrams** — with explicit diagram-verification duty pushed to you `[D SRC-234]`, `[O SRC-232/233/235]`.
- **Gemini/Nano Banana, Krea, SD front-ends:** all ship "enhance"-style rewriting in 2026; treat every rewrite as a **proposal**, not truth.

### 2.3 Image→prompt ("reverse prompt") enhancers — the node-level class `[D]/[O]`

For the re-imagine workflow specifically, the most useful enhancer is the **captioner that turns your input image into text**:
- **Florence-2** caption → CLIP text encode is the standard ComfyUI pipeline (`kijai/ComfyUI-Florence2`, ComfyUI_LayerStyle’s Florence2Image2Prompt) — a 0.45 GB base model that produces the descriptive prompt for you `[D SRC-214] [O SRC-216] [O SRC-217]`;
- **Qwen2.5-VL nodes** (1–15 GB variants) for richer captions `[O SRC-217]`;
- **LLM enhancer ports** (FluxPromptGen: Florence-2 caption + local LLM rewrite via Ollama) `[D SRC-215]`;
- community consensus: these save labor, but the caption **describes what is there, not what must be preserved** — you still append the preserve-list `[O SRC-217]`.

### 2.4 The judge-side catch — enhancement changes what auditors measure `[R]`

GenEval 2 (arXiv 2512.16853) ran judges against **original vs rewritten** prompts and found scoring shifts: VQAScore drops 93.5 → 90.5 on rewritten prompts (Qwen3-VL judge) while the newer Soft-TIFA stays ≈stable (94.2 → 94.4); best models reach **85.3 % atom-level but only 35.8 % prompt-level** correctness `[R SRC-226]`.
**Reading** `[N]`: enhancement does not objectively "improve" a result; it moves the result along the axis the judge is looking at. Therefore: **fix the intent first (frozen, written), let the enhancer expand only the fields (light, material, atmosphere, style), and verify against the frozen intent — never against the enhanced text.**

---

## 3. "3D re-imagine" is three different transactions — stop treating them as one

| Transaction | Reality check (what the evidence supports) | Correct instrument | Grade |
|---|---|---|---|
| **A. 3D-conditioned 2D edit** — restyle/re-render a plate while holding geometry | Works: depth/normal/edges as explicit conditions are the proven levers `[R SRC-186/190]`; our executed runs confirm (E beats D on every fidelity metric, §6) | ControlNet depth/canny/MLSD + preserve-list; instruction editors with reference image | `[R]/[I]` |
| **B. Viewpoint change of an existing image** — "show me the other corner" | Research-grade and lossy: camera-conditioned diffusion (Zero-1-to-3 line) generalizes from synthetic training but is scene-approximate `[R SRC-193/194]`; ViewCrafter (TPAMI 2025) needs point-cloud priors + iterative synthesis to stay consistent `[R SRC-191/192/195]`. **Our executed run F shows exactly the failure**: the view changed, the building didn't — middle-band structure collapsed to edge-IoU 0.257 (§6) | Your own model (new viewport → restyle) or an actual NVS pipeline — never img2img "rotate it" for anything submittable | `[R]/[I]` |
| **C. Image → 3D asset** — snip a photo → get a mesh | Production-useful for context and props, not for exact architecture: TRELLIS.2 (MIT, 4B, sparse-voxel O-Voxel, PBR → 4K, single photo, ~20 s–4 min; community ports in ComfyUI; ~10–12 GB weights; <2 min on RTX 4090 reported) and Hunyuan3D (open; hosted 20 gens/day; 3.5 claims <60 s + 8K PBR) lead the open class; hosted Meshy/Tripo/Rodin ~$0.10–0.50/model `[O SRC-196/197/199] [O SRC-200/201/202/203]`. Honest flaws documented by reviewers: baked lighting in albedo, uneven texel density, approximate back-of-object reconstruction `[O SRC-197]` | TRELLIS/Hunyuan (local or hosted); ComfyUI-TRELLIS2 nodes if you live in ComfyUI — expect install friction `[O SRC-200/203]`; pre-existing CAD? no — use it for massing/context, verify by dimensions | `[O]` |

**And for capturing real context — the lawful-input machine you already carry:** Polycam (LiDAR + photogrammetry; OBJ/STL/FBX/GLB/DAE; ~$27/mo) and KIRI Engine (free → Pro ≈$80/yr) turn a site walk into your own rights-clean base mesh; MagicPlan/SiteScape for plans/point clouds; note the LiDAR-dependent apps need iPhone Pro-class hardware, photogrammetry works on any phone `[O SRC-246/247]`. This converts "screenshot from the internet" into "capture I own" — the cleanest fix to the blind-spot leg's custody problem.

---

## 4. SPATIAL COGNITION — the measured human–machine gap, and why it matters to a student

### 4.1 The benchmark record `[R]/[O]`

| Benchmark | What it measures | Headline result |
|---|---|---|
| **VSI-Bench** (NYU; 288 videos, 5,060 QA) | 3D spatial reasoning from video: configurational, metric, spatiotemporal | **Humans 79.2 % average; best MLLM 48.8 % (Gemini-1.5 Pro); GPT-4o 34.0 %.** Per-task: humans 94–100 % configurational vs models ≈50 %; route planning 95.8 % vs 36.0 %; relative direction 95.8 % vs 46.3 %; even absolute distance: 47.0 % vs 30.9 % `[O SRC-218] [R SRC-220]` |
| **VLM²** (2026) | Video-LLM + 3D geometric priors + dual memory | Video-only SOTA reaches 68.8 avg — but its own public review flags possible scene-level leakage in the training/eval splits `[O SRC-221]` |
| **OmniSpatial** | Cognitive-psychology taxonomy beyond left/right/counting | Training on it lifts VSI-Bench 41.7 → 43.7 — gains are real but incremental `[R SRC-219]` |
| **GPT-4V (engineering-design study, v1 corpus)** | Packing / rotation / projection | 36 % packing, 18 % rotation ≈ random; blind-vs-through-hole 11 % `[R SRC-044]` |
| **MapBench (v2 corpus)** | Reading human-readable maps | *"Critical limitations in spatial reasoning and structured decision-making"* `[R SRC-106]` |

**Verdict** `[N]`: models are decent at *naming what is in a view*, weak at *mentally moving between views* — the exact operation "3D re-imagine, rotate it" asks them to perform, and the exact operation §6/F shows them faking.

### 4.2 The other side — human spatial ability in architecture education `[R]`

- **Trained vs untrained (N=593, Frontiers 2020):** master students beat beginners on perspective-taking, object composition and cross-section visualization — **but not on the standard Mental Rotations Test**; longitudinally, cross-section and composition gains were robust `[R SRC-222]`.
- **Course effect (Kara 2020):** first-semester studio measurably raised spatial visualization/perception; **mental rotation did not move** — the paper recommends targeted MR training `[O SRC-223]`.
- **VR effect (MDPI Buildings 2023, AISAT):** spatial visualization performed better in static mode; **mental rotation performed better in VR**, and the usual gender gap was not evident in VR `[R SRC-225]`.
- **Disciplinary edge (Estoa 2025):** architecture students outperform peers on 2D/3D **and 4D** cube-rotation tasks `[R SRC-224]`.

**Synthesis for your practice** `[N]`: the studio trains composition and cross-sections; it under-trains rotation; AI models are worst exactly at rotation-family operations. So the correct division of labor is: **AI multiplies views you can already justify (restyles of screenshots you took, variants of your own model), while the mental rotation work stays yours — and if you want it stronger, VR rotation drills are the evidence-backed trainer** `[R SRC-225]`. Using "rotate the building" prompts as a substitute trains the model habit of accepting pseudo-rotations (§6/F) — the precise compound error:

> *you outsource the skill you're weakest at, to the system that's weakest at it, and neither of you can tell.*

### 4.3 Spatial vocabulary as prompt equipment — say exactly what projection you want `[O]`

| Projection | Angles | Prompt phrasing that maps to it |
|---|---|---|
| **Isometric** (true) | 30°/30° axis drawing; camera yaw 45°, pitch atan(1/√2)≈35.264° | *"true isometric, 30° axonometric, no perspective, verticals vertical"* `[O SRC-238/240]` |
| **Dimetric / trimetric** | two / three different foreshortenings | *"dimetric 2:1, steeper pitch, dynamic composition"* |
| **Plan oblique (military)** | plan rotated 45°/45° (or 30/60), verticals true-length | *"military axonometric — plan readable, walls extruded straight up"* — the workhorse for diagrams `[O SRC-238]` |
| **Elevation oblique (cabinet)** | front true, depth 45° at half length | *"cabinet axonometric, half-depth, facade true"* |
| **Section axonometric / cutaway** | — | *"cutaway axonometric, front half removed, interior visible"* |

The point of the vocabulary is falsifiability: "nice axo" cannot be checked; "verticals stay vertical, parallels stay parallel, 30/30" can be — and it survives into the QA pass.

---

## 5. QUALITY & RELEVANCY — what to measure, with what, against what

### 5.1 The benchmark map (what each metric class is actually for) `[R]`

| Metric family | Examples | Measures | Known limits |
|---|---|---|---|
| Compositional adherence | **GenEval / GenEval 2** (six sub-tasks → 40 objects/18 attributes/9 relations/6 counts) | Does the image contain the requested atoms in the right relations? | Detector-dependent; drift → hence GenEval 2 + Soft-TIFA `[R SRC-226/227]` |
| Human-aligned scoring | **VQAScore** (CLIP-FlanT5), **TIFA**, **Soft-TIFA** | Question-based alignment; AUROC vs human judgment 92.4 / 91.6 / **94.5** | Judges drift with model generations; rewritten prompts shift scores `[R SRC-226/228]` |
| Edit-specific | **GEdit-Bench / GEditBench v2** (606 → 1,200 real user edits; 11 → 23 tasks; + PVC-Judge) | Instruction following **vs** visual consistency of unedited regions | Documents the **under-editing trap**: models that barely change anything score high on consistency (GLM-Image VC 1,109 with IF 787) `[R SRC-229/230]` |
| Reward/judge models | **EditReward** (ICLR 2026), **Q-Judger** (v2 corpus, Spearman 0.92) | Automated screening of many candidates | Replace neither human eye nor deterministic checks `[R SRC-231]` |
| Provider self-reports | GPT-4o image system-card addendum; GPT Image 2 third-party reviews (adherence 9.8/10; text as differentiator; 9/13 use cases production-ready) | Vendor-relevant strengths/risks | Vendor-grade claims; cap at `[O]` unless docs `[D SRC-234] [O SRC-232]` |

### 5.2 The operational definition for YOUR requests `[N]`

*Relevancy to the user's request* = **adherence to a frozen intent** (did it do what I asked?) **+ preservation of declared invariants** (did it keep what I said must stay?) **+ provenance** (can I say what tool and what inputs produced this?). Hence a four-gate ladder, all cheap:

| Gate | Question | Instrument | Threshold (calibrated on our own runs, re-baseline as you go) `[I]` |
|---|---|---|---|
| **G1 Adherence** | Did it do the asked change, and only that? | Your eyes + optional VLM judge (never sole arbiter — v2/v1 evidence) + the *atom checklist* from the frozen intent | every asked atom present; **zero unrequested content** (D failed this: added four labels + roof vent) |
| **G2 Preservation** | Did the declared invariants survive? | `outputs/2026-09-29_reimagine_fidelity.py` — edge-IoU, SSIM, band deltas, annotation retention | faithful restyle ≥0.85 IoU / ≥0.95 SSIM; usable-with-redraw 0.6–0.8; **any loss of a required annotation = reject** (§F below) |
| **G3 Geometry claims** | If the plate asserts a projection/view, is it internally true? | `outputs/2026-09-29_plate_audit.py` (scale, ring, format) + axis check (verticals/parallels) | no dimension/projection claims without a source model |
| **G4 Provenance & law** | Whose image, whose tool, disclosed? | Rights pre-flight (blind-spot leg), tool custody matrix, disclosure line, SynthID/C2PA tools where available | disclosure block present; no unlicensed input; no watermark pipelines |

---

## 6. EXECUTED EXPERIMENT — "3D re-imagine" under the harness `[I]`

**Subject:** our own exploded axonometric (four stacked layers: roof slab, upper floor, ground floor, foundation; dashed alignment lines; red stair/bath cores — a plate whose *whole meaning* is spatial: layer order, alignment, core position).
**Harness:** `outputs/2026-09-29_reimagine_fidelity.py` (now CLI-capable; adds **M5 band-wise structure** — top/middle/bottom third edge-IoU and ink-mass ratio — a crude spatial-cognition probe), results in `outputs/2026-09-29_reimagine3d_fidelity_results.json`.

| Run | Prompt class | M1 edge-IoU | M2 SSIM | M5 top / middle / bottom (IoU; ink ratio) | Visual read |
|---|---|---|---|---|---|
| **D — naive** ("reimagine as clean editorial vector…") | style only | 0.719 | 0.938 | 0.772 / 0.710 / 0.693 — ink ≈ 1.0 everywhere | **Added unrequested content**: four floor labels ("ROOF LEVEL…", "FOUNDATION"), a roof hatch, a vent. House style otherwise preserved. |
| **E — 3D-aware preserve-list** ("…true parallel axonometric, zero perspective; verticals vertical, parallels parallel; same four layers in order and spacing; every wall/window/door/stair; dashed lines; red cores; no additions, no text") | style + explicit geometry & projection invariants | **0.775** | **0.968** | **0.836 / 0.754 / 0.775** | Faithful: all four layers, spacing, core position, dashed lines; no added text; more saturated red core (deliberate style freedom) |
| **F — viewpoint change** ("keep style and layers, rotate the building 30° clockwise around its vertical axis…") | **transformative spatial ask** | **0.394** | 0.814 | **0.381 / 0.257 / 0.667** — middle band collapses | It *attempted* the rotation: roof notch moved, kitchen relocated, right walls revealed — but the **stair core degraded into an amorphous wedge**; wall/door network rearranged. A **plausible new drawing, not our building from a new angle** — a pseudo-rotation. |

**Findings** `[I] [N]`:
1. **The 3D-aware preserve-list is the best instrument available today** — E's fidelity (0.775 / 0.968) even improved on the map-plate result from the blind-spot leg and held *all three bands* (0.75–0.84). Naming the projection itself ("verticals vertical, parallels parallel") is the 3D-specific upgrade to the preserve-list.
2. **Naive restyles hallucinate *content*, not just style.** D did not visibly break geometry — it silently added a floor-plate label set and equipment that a reviewer would read as project data. Class-of-failure: unrequested addition.
3. **Viewpoint-change prompts produce pseudo-rotations.** F's band profile is the fingerprint: foundation band held (0.667 — the outline guess is easy), middle band collapsed (0.257 — the actual spatial content is where it fails). This matches the benchmark record (§4.1) — the weakest measured machine skill is the one this prompt asks for.
4. **Metric honesty (kept in the record):** M4 (red-class retention) read **451 % / 285 % / 44 %** — inflated by palette shift pushing pixels into the red mask class. On plates with palette changes, M4 is a flagger only; the verdicts above rest on M1/M2/M5 and the visual reads. Same rule as before: *a metric with known blind spots is reported with them.*
5. **The general law this experiment adds to the file:** *image models can restyle your drawing; they cannot rotate your building; and they will not tell you which of those they just did.*

---

## 7. APPLICATION — the re-imagine protocol, upgraded (supersedes §6.3 of the blind-spot leg where they conflict)

```text
STEP 0  FROZEN INTENT   write the request you will hold the tools to (atoms + invariants).
                        The enhancer NEVER edits this text — it expands only fields (light/material/mood/style).
STEP 1  INPUT           own model screenshot (clean viewport ≥1920px) ▸ own capture (Polycam/KIRI) ▸ lawfully-licensed
                        ▸ never: unlicensed internet snippet (rights pre-flight from the blind-spot leg still governs).
STEP 2  ENHANCER ROUTE  provider "enhance" button → read the enhanced prompt ("show enhanced"), edit it, keep the
                        preserve-list OUTSIDE its rewrite zone. Optional: Florence-2/Qwen2.5-VL caption node for
                        image→text; local LLM rewrite as candidate, never as final.
STEP 3  CHANNEL SETUP   restyle: img2img denoise 0.35–0.55 + preserve-list; geometry-critical: ControlNet depth
                        (0.7–0.8) / Canny (0.9–1.0) / MLSD (0.4–0.6); style: IP-Adapter 0.5–0.7; two-pass lock→style.
STEP 4  VIEW PROBLEMS   need another angle? GO BACK TO THE MODEL (new viewport screenshot), or reconstruct:
                        TRELLIS.2/Hunyuan image→3D → re-render; NVS (ViewCrafter-class) acknowledged as
                        research-grade. NEVER img2img "rotate it" for anything you'll submit (Run F).
STEP 5  VERIFY          G1 adherence (atom checklist incl. “no unrequested content”) → G2 fidelity harness (CLI:
                        python3 outputs/2026-09-29_reimagine_fidelity.py in.png out.png "label") → G3 plate audit if the
                        plate asserts dimensions → G4 provenance + disclosure.
STEP 6  SHIP            vector labels, title block, disclosure line, and the log (input, tool, prompt, numbers).
```

**What this changes vs the last leg:** G1 gains the *no-unrequested-content* clause (Run D's failure); the preserve-list gains the projection invariant (Run E's win); the harness gains band-wise readout (Run F's detector); and "3D re-imagine" is split into its three honest transactions (§3) instead of being one wish.

**Gap statement (for the record):** the Commander's incoming external research — *"photo based re-imagine prompts for architectural purposes"* — remains the missing input for **photo-in** recipes (photographic inputs, re-lighting, real-estate/interior workflows). On receipt: register from next free SRC ID, triangulate against §3/§7, conflict rows where it disagrees, and carry it into **v3**. This leg does not pre-empt it.

---

## 8. CONFLICTS & LIMITS

| # | Position A | Position B | Status |
|---|---|---|---|
| 1 | Enhancers improve adherence (PromptEnhancer/APE/DPO-rewrite results) `[R]` | Enhancement shifts judge scores (VQAScore 93.5→90.5 on rewritten prompts; GenEval 2) and can overwrite user intent fields `[R]` | **OPEN — governed by protocol**: enhance fields, freeze intent, verify against intent |
| 2 | VLM² reaches 68.8 on VSI-Bench (video-only SOTA) `[O]` | Circumstantial leakage in benchmark splits per its own review `[O]` | **OPEN** — cite the number with the caveat or not at all |
| 3 | AI view-change is impossible (our F; MLLM rotation benchmarks) `[I]/[R]` | NVS research legitimately synthesizes novel views (ViewCrafter/Zero-1-to-3) with camera conditioning `[R]` | **RESOLVED as tiering**: NVS via purpose-built pipelines = research-grade tool; img2img "rotate" = pseudo-rotation |
| 4 | "AI improves spatial skills" (tool marketing) | Measured: training improves visualization/composition; mental rotation does **not** improve from ordinary studio work (Kara; Frontiers) — but VR drills do (MDPI) `[R]` | **RESOLVED**: only targeted (VR) rotation practice shows MR gains; restyle tools don't train rotation |
| 5 | 3D asset generators "compete with professionals" (vendor-adjacent) `[O]` | Reviewer-documented flaws: baked lighting, uneven UVs, approximate backs `[O]` | **OPEN** — treat outputs as context/massing assets pending dimension check |

**Limits** `[N]`: our experiment is one plate, one model session, three prompts — it demonstrates *method and detector*, not universal constants; thresholds (0.85/0.95) are calibration from this harness. VSI-Bench numbers quoted are as-of-publication snapshots; 2026 model claims move fast and are grade-capped accordingly. Provider claims (TRELLIS speed, GPT Image 2 adherence) are vendor or vendor-adjacent until independently replicated. Nothing here is legal advice; the rights layer lives in the blind-spot leg.

---

## 9. REFERENCES — S012 3D leg (SRC-186 … SRC-247; 62 rows)

**3D-conditioned editing & spatial control (research):** SRC-186 ICLR 2025 try-on depth/normal cues `[R]` · SRC-187 SpatialHand 6DoF (ICLR 2026 submission; baselines lack 6DoF) `[R]` · SRC-188 ControlNet depth explained `[O]` · SRC-189 Diffusion-for-3D-generation survey `[R]` · SRC-190 SmartSpatial IJCAI 2025 + SpatialPrompts/SmartSpatialEval `[R]`
**Novel view synthesis:** SRC-191 ViewCrafter project page `[R]` · SRC-192 ViewCrafter arXiv `[R]` · SRC-193 Zero-1-to-3 `[R]` · SRC-194 Zero-1-to-3 cross-attention analysis `[O]` · SRC-195 ViewCrafter TPAMI record `[R]`
**Image→3D tooling (platforms/repos/social):** SRC-196 3D-gen APIs comparison `[O]` · SRC-197 Cinevva (free-tier licensing; baked-lighting/texel flaws) `[O]` · SRC-198 3D AI Studio guide `[O]` · SRC-199 Pixazo open-source APIs `[O]` · SRC-200 r/comfyui TRELLIS-2 nodes test `[O]` · SRC-201 TheLocalLab TRELLIS 2 installer claims `[O]` · SRC-202 r/comfyui TRELLIS pipeline thread `[O]` · SRC-203 brightcoding ComfyUI-TRELLIS2 guide `[O]`
**Prompt enhancers:** SRC-204 PromptEnhancer arXiv `[R]` · SRC-205 APE arXiv `[R]` · SRC-206 PromptEnhancer CVPR 2026 `[R]` · SRC-207 APE review (pith) `[O]` · SRC-208 input-side rewriting arXiv 2510.12041 `[R]`
**Prompt channels (IP-Adapter/ControlNet):** SRC-209 agentbus scale tables `[O]` · SRC-210 theneuralbase IP-Adapter mechanics `[O]` · SRC-211 technolynx four layers + failure modes `[O]` · SRC-212 morphic IP-Adapter glossary `[O]` · SRC-213 ThinkDiffusion image-prompt masterclass `[O]`
**Caption/repo enhancers:** SRC-214 kijai/ComfyUI-Florence2 `[D]` · SRC-215 ComfyUI_FluxPromptGen `[D]` · SRC-216 LayerStyle Florence2 workflow `[O]` · SRC-217 r/StableDiffusion image→prompt thread `[O]`
**Spatial cognition:** SRC-218 VSI-Bench topic table `[O]` · SRC-219 OmniSpatial `[R]` · SRC-220 Thinking in Space project `[R]` · SRC-221 VLM² review `[O]` · SRC-222 Frontiers 2020 architecture spatial abilities `[R]` · SRC-223 Kara architecture-course spatial study `[O]` · SRC-224 Estoa 2025 nD rotation `[R]` · SRC-225 MDPI AISAT VR/static `[R]`
**Quality/relevancy metrics:** SRC-226 GenEval 2 `[R]` · SRC-227 GenEval topic `[O]` · SRC-228 VQAScore ECCV `[R]` · SRC-229 GEditBench v2 `[R]` · SRC-230 Step1X-Edit/GEdit-Bench `[R]` · SRC-231 EditReward ICLR 2026 `[R]`
**Provider reports & enhancer features:** SRC-232 Everypixel GPT Image 2 review `[O]` · SRC-233 Playyy analysis `[O]` · SRC-234 OpenAI 4o system-card addendum `[D]` · SRC-235 MindStudio GPT Image 2 vs Gemini `[O]` · SRC-236 PixVerse prompt guide `[O]` · SRC-237 Adobe Firefly prompt enhancement `[D]`
**Projection vocabulary:** SRC-238 Illustrarch axonometric table `[O]` · SRC-239 r/architecture iso-vs-axo `[O]` · SRC-240 GameDev SE isometric math `[O]`
**Practice & capture:** SRC-241 r/aitoolhq rendering tools `[O]` · SRC-242 r/Architects AI rendering thread `[O]` · SRC-243 ai-architect.net SU Diffusion 2026.1 `[O]` · SRC-244 RoomLab guide (Chaos 44 % figure) `[O]` · SRC-245 Chaos comparison (Veras/Rendair/Archsynth) `[O]` · SRC-246 KIRI LiDAR apps round-up `[O]` · SRC-247 ScienceInsights phone-scanning guide `[O]`

*Registry: **237 registered IDs** present (highest SRC-247; gaps 002–008 legacy + 147/148/155 intentional from the prior legs). Composition this leg: 17 primary/paper-class + 45 analysis/social/platform. Quota floors met (@Gather 10+18; @Radiation 12+20).*

*Sentinel: §6 numbers reproduce from `outputs/2026-09-29_reimagine_fidelity.py` (CLI mode) and `...3d_fidelity_results.json`; the three run plates are in `outputs/` (D/E/F). Every claim outside §6 traces to §9 with its grade. Standing by for the Commander's handoff to complete v3.*
