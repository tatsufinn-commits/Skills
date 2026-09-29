# RESEARCH — Re-Imagine Blind Spots: Screenshots, Custody, Capability, and a Measured Fidelity Gate
## S012 scope-expansion leg — answer to: *"is there something I haven't noticed that we need to address?"*

> **Session:** S012 · 2026-09-29 · Arena AI (Agent Mode) · RADIATION v3.10.40-candidate
> **Commander's revealed workflow (verbatim, 2026-09-29):** *"I am an architecture student and I use AI to reimagine what I create or what I screenshot/snippet from the internet, and I need better re-imagining capabilities for it to happen… is their something I havent noticed that we need to address? if yes can you research regarding it? same directives as earlier."*
> **Disposition:** v2 remains the live deliverable (HELD pending the other agent's photo-re-imagine research). This leg is **additive** — it maps the scope blind spots the workflow exposes and researches them under the same directives (@Autopilot, STYLE AUTO → `research.md` base + one declared addition: **§6 EXECUTED FIDELITY EXPERIMENT**). When the incoming handoff arrives, **v3 = v2 + this leg + the handoff**, merged with conflict rows.
> **Grades:** `[D][O][I][R][N][S]` as always. No Nota. No Core write.

---

## 1. ANSWER FIRST — the eight things you haven't flagged

| # | Blind spot | Why it bites | Where answered |
|---|---|---|---|
| **1** | **"Screenshot from the internet" is not a neutral input.** An img2img remix of a human-made image is a *derivative work* question, and 2026 courts look at the **visual output** ("total concept and feel"), not the process; liability is **strict** — intent is irrelevant | A pretty re-imagine can be an infringing derivative; "I only used it as a reference" is not a defence if the output is substantially similar | §3 |
| **2** | **You are in the Philippines: no freedom of panorama.** Photographs/renders that substantially reproduce a copyrighted building or artwork — commercial or distributed use without permission — can infringe; the current exceptions are thin | Snippets of buildings/monuments you didn't notice were copyrighted; posting re-imagines of them publicly compounds it | §3 |
| **3** | **Watermarks are not cosmetic — they are CMI.** Removing a watermark (or using a tool pipeline designed to) can violate DMCA §1202-class protections even when you never publish — statutory damages $2,500–25,000 per violation in the US, with equivalents elsewhere | A "clean up this stock screenshot" prompt is a legal act, not a filter | §3 |
| **4** | **School and competition rules are now the sharper threat than copyright.** 2026 policies split into disclosure / process-only / prohibited postures (Cornell AAP: no AI-generated imagery; CCS: one AI piece max, no AI finals); competitions require **original concept + process statement**, and non-disclosure — not use — is the disqualifying act | You could lose a portfolio slot or a competition for *how* you used AI, not *that* you used it | §4 |
| **5** | **Your uploads are someone's training data — possibly not yours to give.** Consumer tiers of major tools train by default (OpenAI Free/Plus/Pro: opt-out required; Midjourney: images public by default + Midjourney keeps a training licence; Leonardo free: public + Leonardo owns the output IP). Uploading **someone else's** snippet or your **unreleased** studio work to a consumer cloud tool is a custody leak | Two victims: the image owner (their work is now in a training pool) and you (unreleased work exposed; output rights are tier-dependent) | §5 |
| **6** | **"Better re-imagining" is a parameter stack, not a better model.** The executed experiment below: the same model and a **preserve-list prompt** moved geometry retention (edge-IoU 0.48 → **0.90**), global similarity (SSIM 0.87 → **0.97**) and kept the legally required red radius ring that the naive prompt silently deleted (retention **1.9% → 25.4%**) | Prompt strategy dominates outcome; and the naive output *looked* fine | §6 |
| **7** | **The screenshot path degrades invisibly.** From a 460 px JPEG-quality-35 snippet, the preserve-list run still produced a smooth, clean-looking plate — but drift from the clean source is measurable: SSIM 0.967 (clean path) vs **0.809** (snippet path); edge-IoU 0.898 vs **0.653** | "It looks clean" ≠ "it is faithful"; loss-of-fidelity is invisible without measurement | §6 |
| **8** | **You need a verifier you can run in 2 seconds.** No detector will save you: university guidance in 2026 says AI detectors are not sole evidence — **documentation** is the defence; and reverse image search (TinEye oldest-sort first) is the tool that answers "what is this snippet and whose is it?" | Process discipline (originals, inputs, parameters, fidelity numbers, disclosure line) is the only durable shield | §4, §6, §7 |

**Ranked verdict** `[N]`: blinds 1–3 are the ones you cannot un-ring after a mistake (legal); 4–5 are the ones that can cost you a submission (policy); 6–8 are the ones that make the work actually better (craft). All three classes are now covered below — with the craft class *measured on your own machine*.

---

## 2. What this leg adds to the existing spine

v1 → legal baseline, prompt grammar, custody for map data. v2 → provider/platform matrix, audits, executed map-plate audit. **This leg → the re-imagine layer of an architecture student's actual workflow:** rights triage for snippets, upload custody, the parameters that make img2img obey, a fidelity harness with executed numbers, and the documentation package that satisfies the strictest 2026 school/competition rule without lying about process.

---

## 3. Screenshot rights: the legal layer you were walking past `[O]`

**3.1 Img2img is derivative-work territory.** As of early 2026 the settled positions are: (a) *pure* AI output without meaningful human contribution is not copyrightable (US Supreme Court declined *Thaler v. Perlmutter*, 2 March 2026) — which is why "someone else's AI image" is a strange grey zone; but (b) **taking a human-made image as an img2img input and producing something substantially similar to it is an unauthorized derivative** — courts now look at the **visual output**, and the operative question is whether the result captures the original's "total concept and feel" `[O] [SRC-134] [SRC-135]`. Infringement is **strict liability**: no knowledge or intent required `[O] [SRC-137]`. Copyright Office guidance confirms prompting alone usually does not give you authorship of what the model expresses — so the derivative risk outweighs the ownership you think you're building `[O] [SRC-138]`.

**3.2 Architectural works are protected as such — and you work in that medium.** The 1990 Architectural Works Copyright Protection Act covers "the design of a building as embodied in any tangible medium" — plans, drawings, renderings, **and the building itself**; plaintiffs prove access + substantial similarity; the "total concept and feel" test means *minor changes are no defence*, and innocent infringement is no defence `[O] [SRC-181] [SRC-182]`. Courts keep protection to the author's **expression** (standard features like windows and doors are unprotectable, and mere conceptual inspiration is not actionable `[O] [SRC-183]`) — but the practical line every practitioner guide repeats is blunt: *no amount of changes converts someone else's protected plan into your design* `[O] [SRC-185]`.

**3.3 The Philippines detail that matters: no freedom of panorama.** RA 8293's exceptions do **not** include reproducing images of copyrighted buildings, monuments, or artistic works for commercial/distributed use; §184(d) covers only incidental current-events reporting `[O] [SRC-139] [SRC-141]`; Wikimedia Commons classifies the Philippines as "no FoP" and blocks such uploads `[O] [SRC-140]`; reform bills (HB 2672 in the 19th Congress) have **not** been enacted `[O] [SRC-139]`. Photographic works are protected 50 years from publication `[O] [SRC-140]`. **Translation into your workflow:** a screenshot of a landmark building, a famous interior, or a copyrighted photo of one — re-imagined and *posted, submitted, or published* — is exactly the use the thin PH exception does not cover. Private study is one thing; a public board or competition entry is another `[N]`.

**3.4 Watermarks are CMI, and "cleaning" them is an act with a price tag.** DMCA §1202 makes it illegal to remove or alter copyright management information — watermarks, authorship/licence data — without authorization, **regardless of whether you intended to use the image commercially**; statutory damages commonly cited at $2,500–$25,000 **per violation**, with six-figure settlements attested `[O] [SRC-175] [SRC-176] [SRC-177]`. The correct response to a watermarked snippet is not "generate it away" — it is *find the lawful version or don't use it* `[N]`.

**3.5 Reverse image search is the missing pre-flight step.** Before any snipped image enters a pipeline: **TinEye first** for origin tracing (date-sort to oldest — the earliest indexed copy is closest to the source), **Google Lens/Yandex** for scene identification across different indexes `[O] [SRC-168]`. Research libraries frame it as authenticity hygiene: know and cite the source; if the engines find no source at all — treat it as an AI or unknown-rights image and cap your trust accordingly `[O] [SRC-169]`.

**The triage rule this leg installs** `[N]`:
> **Can't name its owner → don't re-imagine it. Owner named, no licence → re-imagine only for private study, never publish/submit. Licensed (CC/stock/own) → re-imagine freely within the licence. Own work → full freedom, keep the originals.** And never, for any class: remove or pipeline-away a watermark, or reproduce a specific building/photo substantially in a public deliverable without clearance.

---

## 4. School and competition reality, 2026 `[O]`

**4.1 Portfolio/studio policies split into four postures** (August 2026 survey of art/architecture programs) `[O] [SRC-142]`:

| Posture | Meaning | Example | What you must do |
|---|---|---|---|
| **Disclosure required** | AI permitted; declaration mandatory; **non-disclosure is the disqualifying act** | CalArts, Parsons, RISD | Log tools + where AI entered the work |
| **Process-only** | AI for research/ideation only; finals must be human-made | College for Creative Studies (AI capped at 1 piece; no AI final images) | Cite prompts/platforms; keep process |
| **Prohibited** | No AI-generated imagery at all | **Cornell AAP (B.Arch)** | Submit only independently produced work |
| **No published policy** | Silence ≠ permission | Most programs | Treat as risk; ask; default to fully independent work |

AP Art & Design (2026–27): limited AI in ideation/process **with attribution**; final work must be the student's own; violations → score cancellation `[O] [SRC-142]`.

**4.2 Universities: the violation is misrepresentation, not tool use.** 2026 guidance is consistent — detectors are **not** sole evidence for misconduct; the operative question is what a submission *claims about its authorship*; adequate disclosure names **tool, purpose, and extent**, effectively as a specific AI-use statement rather than "AI helped" `[O] [SRC-143]`. Policy fragmentation is course-level: the same student can be permitted in one class and sanctioned in the next, so the syllabus/assignment is the binding document `[O] [SRC-143] [SRC-144]`. (2026 survey: 24% of students admit submitting AI-generated work without disclosure — the cohort the rules are sharpened for `[O] [SRC-146]`.)

**4.3 Competitions are converging on a documentation package** — and the pattern is worth internalising now:
- **ASAI Architecture in Perspective 40 (2026):** AI-influenced images **MUST be labeled**; the submitter **affirms** the work is their original creation and does not duplicate anyone else's copyrighted material; ASAI may demand **proof of originality**; failure to comply → disqualification `[D] [SRC-149]`.
- **Student contest amendment (MLGW 2025–26):** entries must begin from **your own original sketch**, which must be **submitted alongside** the final; AI is permitted only *after* the original concept exists, for enhancement; a **process statement** (tools, how used, how you refined it) is mandatory and judged; AI-generating the concept itself → disqualification under originality `[D] [SRC-150]`.
- **Team competitions (Ideace/others):** reference and third-party tool attribution required; process documentation recommended; plagiarism scrutiny explicit `[O] [SRC-151]`.
- Cross-cutting: 2026 competition guidance already warns AI images may lack full rights (v2 `SRC-117`), and the field has a live disqualification precedent (Hasselblad, v2 `SRC-115`).

**The package that satisfies all of the above at once** `[N]`:
> ① original concept artefact (your sketch/model/photo of it), ② the AI inputs (what image went in, whose is it, what licence), ③ the tool + parameters log (prompt, model, date), ④ the fidelity numbers (§6 harness), ⑤ a one-line **disclosure block** on the board ("Concept imagery produced with <tool>; geometry and annotations author-drawn; ≤n labelled AI-assisted assets"), ⑥ keep everything — version history is the defence the detector-policy guidance tells you to bring `[O] [SRC-143]`.

---

## 5. Custody: whose work is safe in which tool `[O]`

**5.1 The upload-rights matrix** (from vendor docs/T&C analyses; tier-dependent — verify at use):

| Tool | Does it train on your uploads? | Is your upload/output private? | Ownership / rights of output | Grade |
|---|---|---|---|---|
| **OpenAI — ChatGPT consumer (Free/Plus/Pro)** | **Yes by default; opt-out in Settings → Data Controls** (`Improve the model for everyone` toggle); files ~30 days | Conversation/attachments private per account, but trainable unless opted out | You retain output rights per policy; personal-workspace data-sharing default is ON | `[D] [SRC-156] [SRC-157] [SRC-158]` |
| **OpenAI — API / Business / Enterprise** | **No training by default** (policy) | Yes | Commercial use standard | `[D] [SRC-156]` |
| **Midjourney (paid)** | MJ retains a **licence to use images for training/service**; public by default | Public unless **Stealth (Pro/Mega)** | Full ownership on paid tiers; no free tier since 2024; free outputs only CC BY-NC | `[O] [SRC-152] [SRC-153] [SRC-154]` |
| **Adobe Firefly** | Vendor states **no training on Creative Cloud subscriber content**; trained on licensed + public-domain | Yes | "Commercially safe" claim + **Content Credentials on output**; note the General ToU §2.2 still mentions ML analysis of content — Firefly policy is the specific commitment | `[D] [SRC-170]`, `[O] [SRC-171]` |
| **Leonardo.Ai (free tier)** | **Yes (public content used for training)** | **No — free generations are public** | **Leonardo owns free-tier output IP**; paid tiers assign ownership and keep private content out of training | `[O] [SRC-172] [SRC-173]` |
| **Krea (free tier)** | Not on free content per current review; **no commercial rights on free** | Yes — private | Commercial licence requires paid plan | `[O] [SRC-172] [SRC-174]` |
| **Local stack (ComfyUI + Qwen-Image/FLUX/ControlNet)** | Nothing leaves the machine | Full | Apache-2.0 model stack = licence-clean for output use; your custody is total | `[O] [SRC-164]` |

**5.2 The custody rules this leg installs** `[N]`:
1. **Snippets never go into consumer-cloud tools.** If it is someone else's image without a licence, it doesn't get uploaded at all (that is also the derivative-work-safe default). If it must be studied, study it locally or not at all.
2. **Unreleased studio work: local stack or API-no-training only.** Your own renders/models are the assets you cannot rewind once trained-on or leaked (free tiers that publish your uploads: Leonardo free; Midjourney without Stealth).
3. **Free GPU exists:** Colab T4 (15–30 hrs/week), Kaggle (~30 GPU hrs/week; environment ships torch/diffusers/ComfyUI), HuggingFace ZeroGPU (5 min/day), Lightning AI (~15 credits/mo) — enough to run a ComfyUI restore/restyle pipeline without paying or exposing anything `[O] [SRC-178] [SRC-179] [SRC-180]`.

---

## 6. Capability: what "better re-imagining" actually is — and the executed proof `[I]`

**6.1 The parameter stack (the craft layer v1/v2 didn't spell out)** `[O]`:

- **ControlNet conditions for architecture** — the preprocessor is a *choice of truth*: **MLSD** = straight lines/manmade geometry; **Depth** = 3D space; **Canny/Lineart** = exact outlines; **Segmentation** = zones. Practitioner weight tables for architecture: Canny 0.9–1.0 (lock lines), Depth 0.7–0.8 (space), MLSD 0.4–0.6 (geometry error correction) `[O] [SRC-161]`; general guidance: keep weights 0.6–1.0, >1.3 artifacts, 0.4–0.7 loose hint `[O] [SRC-159]`.
- **img2img denoise is the fidelity dial:** 0.35–0.55 = strong structure retention; 0.6+ = bigger makeover `[O] [SRC-160]`.
- **The two-pass method (lock, then style):** pass 1 — high control weight (0.75–0.85), minimal prompt, nail structure; pass 2 — lower weight (0.35–0.5) or end early, enrich style. "Separate *where things go* from *how they look*" `[O] [SRC-160]`.
- **Prepare own-model inputs properly:** clean viewport screenshot ≥1920×1080, annotations off; depth/canny for buildings — scribble/pose models don't understand architecture `[O] [SRC-162]`.
- **Instruction editors (no node graph needed):** Kontext family vs Qwen-Image-Edit — both preserve structure; documented spatial slips exist in both (objects placed where physically impossible); Kontext leads realism/consistency, Qwen Edit led lighting adherence in one head-to-head `[O] [SRC-163]`; community opinion is **split and contradictory** (see §8 conflicts) — resolve by A/B with the harness, not by vibes `[O] [SRC-165]`. FLUX.2 [pro] Edit takes **up to 9 reference images**, supports JSON-structured prompts and HEX colour control — strong for board-wide consistency `[O] [SRC-164]`. Qwen Image 2.0: unified generation+edit, natively 2048², 1,000-token prompts `[O] [SRC-164]`.

**6.2 The executed fidelity experiment** — same task, three runs, measured with `outputs/2026-09-29_reimagine_fidelity.py` (pure PIL+numpy; SSIM with uniform 7×7 windows, edge-IoU with adaptive gradient threshold, all images normalised to 768²):

| Run | Input | Prompt | Edge-IoU vs input | SSIM vs input | Palette Δ (R,G,B) | Red-annotation retention |
|---|---|---|---|---|---|---|
| **A** | clean plate | **naive** ("reimagine as flat vector…") | **0.485** | 0.867 | 1.6 / 1.2 / 12.1 | **1.9%** — the 2 km ring is *gone* |
| **B** | clean plate | **preserve-list** (explicit keep-list) | **0.898** | **0.967** | 2.9 / 6.3 / 14.2 | 25.4% — ring kept (re-rendered) |
| **C** | 460 px JPEG-q35 "screenshot" | preserve-list (same) | 0.642 (vs its input) | 0.771 (vs its input) | 22.8 / 26.1 / 41.0 | ring kept visually |
| C vs **clean source** | — | — | **0.653** | **0.809** | — | 2.0% by class |

**Findings** `[I] [N]`:
1. **The prompt strategy, not the model, produced the improvement:** edge-IoU nearly **doubled** (0.485 → 0.898) and SSIM rose 0.867 → 0.967 solely by adding a preserve-list. This is the single highest-leverage change available to your workflow — free, instant, portable across tools.
2. **The naive output silently deleted the legally required annotation.** Output A is handsome — and missing the 2 km radius ring that PD 1096 review context exists to read. Retention 1.9% vs 25.4%. *The failure mode looks like a design choice.*
3. **The snippet path is measurably lossier even when it looks clean.** From a 460 px JPEG-35 input, C's fidelity to the clean source (SSIM 0.809, IoU 0.653) sits far below the clean path (0.967 / 0.898) — the visible surface is smooth; the drift is in the geometry you'd be submitting.
4. **Metric honesty (kept in the record):** M4 counts *saturated-red pixels*; B and C demonstrate the ring visually but re-rendered its tone/weight, so pixel-class retention understates ring survival (25.4% / visually present). A's 1.9% is corroborated by direct inspection — no circle at all. The metric is a flagger; the report reads the plate.
5. **All three outputs pass the eye test.** Without the harness, A would have shipped. That is the entire argument for the gate.

**6.3 The Re-Imagine Ladder (workflow this leg installs)** `[N]`:
```text
R0 RIGHTS   trace it (TinEye→Lens/Yandex) → classify (own / licensed / unlicensed / unknown)
            → unlicensed or unknown = local analysis only, never publish/submit; no watermark pipelines, ever
R1 PREPARE  own model → clean viewport ≥1920px; snippet → highest-res lawful version, crop, upscale first
R2 ENGINE   restyle-preserving-geometry → instruction editor (Kontext / Nano Banana Pro / Qwen Edit)
            control-heavy rebuild → ControlNet depth/Canny/MLSD two-pass (lock 0.75–0.85 → style 0.35–0.5)
            text-heavy plates → Recraft Vector / Qwen-Image; board coherence → multi-ref (Seedream / FLUX.2 ≤9 refs)
R3 PROMPT   preserve-list ALWAYS (name every keep: geometry, ring, scale bar, labels, proportions)
            + "no text" on map plates; never ask it to fix/copy text
R4 VERIFY   run outputs/2026-09-29_reimagine_fidelity.py (input vs output; +2 s) → compare IoU/SSIM/ring
            redraw annotations as vectors; audit with outputs/2026-09-29_plate_audit.py before submission
R5 CUSTODY  log input provenance + prompt + tool + date; keep originals; disclose on the board
```

**6.4 What to expect from the numbers** `[I]`: treat edge-IoU **≥0.85 and SSIM ≥0.95** vs input as the "faithful restyle" zone (B's zone); **0.6–0.8 IoU** as "usable with redraw" (the snippet path); **<0.6 with missing required annotations** as "not submittable as a document" (A). These are *this harness's* calibration on one plate — re-baseline on your own images; the point is the gate exists and is cheap.

---

## 7. What changes in the protocol (proposed — `[S]` incubation, needs your word)

1. `[S]` **Rights pre-flight becomes a standing step** for any snipped image (R0) — candidates for `learned_cues` if you adopt the phrase "rights pre-flight".
2. `[S]` **Custody rule for unreleased work**: local/API-no-training only; free tiers that publish uploads are out.
3. `[S]` **Fidelity gate** (`reimagine_fidelity.py`) joins `plate_audit.py` as the second verification harness; promotion into `scripts/` still needs the CAPABILITIES ratification path (unchanged from v2 §6).
4. `[S]` **The disclosure package** (concept + inputs + params + numbers + line) as the default board furniture for AI-touched plates.

---

## 8. CONFLICTS & LIMITS

| Conflict | Position A | Position B | Status |
|---|---|---|---|
| Qwen Edit vs Kontext preservation | Reddit practitioners: *"Qwen edit ruins and changes way too much"* / *"Qwen Edit 2509 preserves more details"* (both in one thread) `[O] [SRC-165]` | Head-to-head session: both preserve structure, both have spatial slips; Kontext realism, Qwen lighting `[O] [SRC-163]` | **OPEN** — resolve per-task with the §6 harness; do not pick by reputation |
| AI-image remixing legality | "Pure AI images are public domain (post-*Thaler*), so remix freely" `[O] [SRC-134]` | The img2img derivative risk attaches to the **source** image's human authorship; strict liability `[O] [SRC-135] [SRC-137]` | **RESOLVED as layering** — the risk track is the source, not the output's copyright status |
| Firefly "does not train on customer content" | Adobe Firefly FAQ + business page: explicit commitment `[D] [SRC-170]` | Adobe General ToU §2.2 still permits ML analysis of content; Firefly-specific promises live outside the ToU `[O] [SRC-171]` | **OPEN — preserved** (same shape as v2's training-claim conflict) |

**Limits line** `[N]`: PH statements here rest on RA 8293 + Commons/Wikipedia summaries — not counsel; if a plate is headed for construction, publication, or a paid competition, get a licensed opinion. Fidelity numbers are **one plate, one model session** — they demonstrate the *method and the gate*, not universal thresholds. Prices/quotas/T&C claims are volatile (90-day class). Grades for forum/T&C-analysis sources are capped as marked; vendor claims are vendor claims.

---

## 9. REFERENCES — S012 blind-spot leg (SRC-134 … SRC-185)

**Legal & rights:** SRC-134 Norton Rose Fulbright — AI copyright litigation 2026 (*Thaler* cert denied 2 Mar 2026; Disney v. Midjourney) `[O]` · SRC-135 aiforreal — AI & global copyright Mar 2026 (img2img "substantial similarity" trap; visual output test; prompt not protectable) `[O]` · SRC-136 redescuela — AI copyright guide 2026 (public domain of pure AI output; platform ToS governs sale) `[O]` · SRC-137 recordinglaw — US AI copyright 2026 (§106/§501; strict liability; Copyright Office 2025 report) `[O]` · SRC-138 Wikipedia — AI and copyright (human authorship; disclosure duty) `[O]` · SRC-139 Wikipedia — Copyright law of the Philippines (no FoP; §184(d); HB 2672 attempt; 50-yr photos via §213) `[O]` · SRC-140 Wikimedia Commons — Philippines (FoP: No; licensing consequences) `[O]` · SRC-141 lawphil — RA 10372 (amending §184.1 text) `[D]` · SRC-175 cliptics — watermark-removal legal 2026 (DMCA §1202 CMI; $2,500–25,000/violation) `[O]` · SRC-176 bridgelegal — watermark removal law (CMI, licence breach) `[O]` · SRC-177 synthidremove blog — AI watermark-removal legality (CMI scope; removal is the act) `[O]` (blocklisted-domain check: none) · SRC-181 vondranlegal — architectural works copyright (AWCPA; access + substantial similarity; filtration test) `[O]` · SRC-182 maynardnexsen — 10 things architectural copyrights (1990 Act; total look; innocent infringement no defence) `[O]` · SRC-183 florida-construction-lawyers — *Sieger Suarez* analysis (expression vs idea; standard features) `[O]` · SRC-184 johnchapmanlaw — construction plans copyright (total concept and feel) `[O]` · SRC-185 buildrrv — copyright Q&A ("no number of changes" makes another's plan yours; internet ≠ public domain) `[O]`

**Academic & competitions:** SRC-142 collegeflightpath — art/architecture portfolio AI rules 2026 (four postures; Cornell prohibition; CCS process-only; AP rules) `[O]` · SRC-143 EyeSift — university guidance (detectors not sole evidence; disclosure standard tool/purpose/extent) `[O]` · SRC-144 uona.edu — AI policy (disclosure & citation; no copyrighted-material feeding; logged environments) `[O]` · SRC-145 NYU Steinhardt — academic-integrity framing for syllabi `[O]` · SRC-146 eCampusNews — Coursera report (24% undisclosed; governance gaps) `[O]` · SRC-149 ASAI — AIP 40 T&C 2026 (AI must be labeled; originality affirmation; proof on request; disqualification) `[D]` · SRC-150 MLGW — art-contest AI amendment (original concept + process statement mandatory; post-concept AI only) `[D]` · SRC-151 Ideace — student competition T&C (reference crediting; process documentation; plagiarism scrutiny) `[O]`

**Custody / platform terms:** SRC-152 terms.law — Midjourney commercial policy 2026 (tier table; free tier CC BY-NC; MJ training licence) `[O]` · SRC-153 pxlpeak — Midjourney pricing 2026 (no free tier since 2024; ~200 images Basic) `[O]` · SRC-154 neolemon — Midjourney commercial use 2026 (public by default; Stealth Pro+; revenue threshold) `[O]` · SRC-156 OpenAI Help — training toggle (business/API excluded; consumer opt-out path) `[D]` · SRC-157 intuitionlabs — ChatGPT plans 2026 (training default by tier) `[O]` · SRC-158 fileuploadgpt — uploads & training (consumer default; ~30-day retention) `[O]` · SRC-170 Adobe (business) — Firefly approach (licensed+PD training; **no training on customer content**; Content Credentials) `[D]` · SRC-171 lightroomqueen thread — Adobe ToU §2.2 nuance vs Firefly-specific policy `[O]` · SRC-172 krea.ai — Leonardo review 2026 (free tier public + Leonardo IP; Krea free private/no commercial; watermark/rights table) `[O]` · SRC-173 terms.law — Leonardo commercial rights 2026 (tier ownership; training policy) `[O]` · SRC-174 toolworthy — Krea review (100 CU/day free; LoRA; commercial on paid) `[O]`

**Capability stack & compute:** SRC-159 Botmonster — ControlNet guide (weights, artifacts >1.3, two-pass, VRAM) `[O]` · SRC-160 sider.ai — ControlNet playbook (denoise 0.35–0.55 retention; two-pass lock/style; MLSD for architecture) `[O]` · SRC-161 comfyui-wiki — multi-ControlNet (architecture weight table Canny/Depth/MLSD) `[O]` · SRC-162 qwe.edu.pl — architectural visualization setup (viewport ≥1920×1080; depth/canny; not scribble/pose) `[O]` · SRC-163 MimicPC — Qwen Edit vs Kontext head-to-head (structure preserved; spatial slips; lighting vs realism) `[O]` · SRC-164 fal.ai — FLUX vs Qwen (families, pricing, FLUX.2 9 refs/JSON/HEX, Qwen 2.0 7B/2K, Apache-2.0 open models) `[O]` · SRC-165 r/StableDiffusion — Kontext vs Qwen restoration thread (positions both ways) `[O]` · SRC-178 alibaba guide — free GPU compute 2026 (Colab/Kaggle/Lightning patterns) `[O]` · SRC-179 aquanode — free GPU credits (Colab/Kaggle ~30 h/wk; ZeroGPU 5 min/day; Lightning credits) `[O]` · SRC-180 pinggy — ComfyUI on Colab (T4 15 GB; tunnel workflow) `[O]`

**Measurement & hygiene:** SRC-166 arXiv 2508.05037 — scene-composition similarity metric paper (SSIM/LPIPS/CLIP behaviour table) `[R]` · SRC-167 paperspace — image-quality metrics review (SSIM/MSSIM/LPIPS definitions) `[O]` · SRC-168 webbytemplate — reverse image search guide (TinEye oldest-sort; Google/Yandex roles) `[O]` · SRC-169 NYU Libraries — finding images / AI authenticity (reverse-search to authenticate; no-source = red flag) `[O]`

*Registry: 133 → **182 rows** after this leg (SRC-134…SRC-185; IDs 147/148/155 intentionally unused). The incoming agent handoff will register from the next free ID at receipt (reception checklist amended accordingly). Composition: 6 primary-type (statute text, organiser T&Cs, vendor docs, arXiv paper) + 43 secondary/analysis/social.*

---

*Sentinel signature: every number in §6 reproduces from `outputs/2026-09-29_reimagine_fidelity.py` + `..._results.json`; every legal/​platform claim traces to §9 with its grade; every `[S]` sits in §7. v2 remains live-but-held; this file is the second leg of the eventual v3 merge.*
