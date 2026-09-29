# PRACTICE — How Architectural Practitioners and Students Actually Use AI, and How They Prompt
## S012 practice leg · social-media-weighted survey of adoption, workflows, prompting habits, and handling

> **Session:** S012 · 2026-09-29 · Arena AI (Agent Mode) · RADIATION v3.10.40-candidate
> **Commander's brief (verbatim):** *"@[Autopilot] | STYLE: [AUTO] | TOPIC: [Research regarding Architectural practioners/students/architect's use of AI and their way (prompt based use) of handling it? refer to sources such as {Researches, LLM audits/reports/findings, Provider Sourced information, Github Repositories, Relevant sournces, Social Media post relevance(rely on this heavily since we are gathering information on people.), reddit, Credible Websites and others you may apply.]]"*
> **Mode:** @Autopilot — focus change, same session; one Scan Declaration covers @Gather (8 batches / ~30 queries, 15+ social/community sources) → @Data (40 rows, SRC-248…) → @Execute (**prompt-practice audit**) → @Deliver.
> **Style:** `research.md` **[AUTO]** + one declared addition carried by convention: **§5 EXECUTED PROMPT-PRACTICE AUDIT** — a structured coding of verbatim practitioner prompts collected during the sweep. The Commander asked how people *handle* prompting; the honest answer requires looking at their actual prompt texts, not at claims about them.
> **Grade discipline:** survey claims `[O]` unless the issuing body's report is primary; social evidence `[O]`-capped and used as *practice signal*, never as technical proof (I.2).
> **v3 note:** this is the **fourth input leg** (v2 + blind-spot + 3D + practice). The Commander's incoming photo-re-imagine handoff still completes the merge.

---

## 1. ANSWER FIRST — the practice picture in ten lines

1. **Practices: yes, but unevenly.** RIBA: **41 % → 59 % → 74 %** of practices using AI on at least some projects (2024→2025→2026); intensive use (most/every project) **6 % → 31 %**; **>90 %** of practices with 50+ staff `[O]`. United States, AIA: only **6 % of individual architects regularly** use it, 53 % experimented, 8 % of firms implemented `[O]`.
2. **Leaders are all-in even where rank-and-file hedge:** 98 % of Design & Make leaders use ≥1 AI tool; 84 % report productivity gains `[D]`.
3. **What they use it for — overwhelmingly the front and back ends of the job, not the middle:** concept imagery (44 %), option variations (35 %), photorealism enhancement (32 %), image-quality passes (26 %) `[O]`; plus specs, code lookups, emails, reports on the text side. **Drafting and design are the last holdouts** — "AI is horrible at designing, especially from scratch" `[O]`.
4. **The emerging standard stack is hybrid:** Midjourney/ChatGPT for the spark → BIM (Revit/SketchUp) for the truth → Enscape/Veras for the faithful render → AI enhancement as the final pass `[O]`.
5. **Their prompt craft is styling-led and parameter-anchored.** Practitioner formulas ("view + building + materials + site + light + mood + parameters" `[O]`; "subject in location, camera type, keep it concise, skip the fluff" `[O]`) spend words on look, and keep consistency with `--sref`/seed locks rather than with preservation clauses `[O]`.
6. **Geometry handling is delegated to tooling, not to words** — ControlNet/MLSD in SD workflows, Veras "Geometry Override 10 %" inside Revit, clean viewport exports — and the field states this explicitly: *"the geometry comes from ControlNet, not the prompt"* `[O]`.
7. **Folk heuristics are sound where they exist:** keep prompts simple; stick to proportions; when it hallucinates, restart instead of building up; check every AI answer against the actual code `[O]`.
8. **The measured gap (this session's audit, §5):** across **15 captured practitioner prompts/recipes, preserve-language appears in 2 — both as meta-advice, neither inside a generation prompt; annotation/text planning 0/15; disclosure/licence handling 0/15**. The field's prompt text carries style, light, and materials; it almost never carries *verification or custody instructions*.
9. **Students are further ahead in usage than in method:** 92.9 % have used GenAI in design work, 78.4 % mostly at ideation; studios report real gains (jury-scored +67.6 % improved outcomes; 95–96 % perceived creativity support with a self-report caveat) but also MJ realism gaps — **70 % of first-pass outputs "different from what they imagined"** `[O] [R]`.
10. **Handling — professionally and socially — is where practice is weakest and the stakes are highest.** AIA's toolkit translates the Code of Ethics into rules (candor 3.301, responsible control 4.102, confidentiality 3.401, copyright 2.101, attribution 5.301) and advises candor over concealment `[D]`; the community reality includes "AI slop" backlash, viral restyle accounts, and client-facing hedging ("I always make sure to hedge to the client that this is a sketch, not a design") `[O]`.

---

## 2. THE ADOPTION NUMBERS (who, how many, how fast) `[O]`

| Source | Sample & date | Headline numbers | Caveats |
|---|---|---|---|
| **AIA** (Journey to Specification) `[O SRC-249/250/251]` | 541 US architects, 2025 | 6 % regular use; 53 % experimented; 8 % firms implemented; 78 % want to learn; 84 % optimistic about complex problems; 90 % concerned (accuracy, privacy); under-50s drive experimentation; tasks: image generation, chatbots, grammar/text analytics | US-only; low-response single survey; single snapshot |
| **RIBA AI Report 2026** `[O SRC-255/258]` | 1,100+ UK/global, Mar–Apr 2026, self-selecting | 74 % of practices use AI on ≥ some projects (41 %→59 %→74 % over three reports); intensive use 6 %→31 %; >90 % for 50+ staff firms; 73 % of users report productivity gain; ROI 57 % positive; 93 % expect ≥moderate impact in 5 years; **only 17 % more optimistic**; **61 % say early-career skill-building gets harder**; 59 % expect sector staff reductions | Self-selecting respondents; authors note "strong signal, not the whole profession" |
| **Autodesk State of Design & Make: AI Pulse 2026** `[D SRC-257]` | 2,500 industry leaders, Jan–Feb 2026 | 98 % use ≥1 AI tool; 84 % report productivity gains; 59 % using/planning agentic AI; 50 % cite legacy-integration as top barrier; 81 % will raise investment | "Leaders", not practitioners; vendor-commissioned |
| **Chaos × Architizer State of ArchViz** `[O SRC-259/260/262/264]` | ~800–1,200 architects/designers, Nov 2024 (3rd edn; 4th edn reported) | 44 % use AI for concept images; 35 % for variations; 32 % photorealism; 26 % image quality; 11 % of firms already using AI in viz workflow; among users, 48 % name concept design as biggest time saving, 40 % image enhancement, ~25 % material/asset generation; ~40 % not using (cost, time, integration, unreliable results) | Trade survey; usage vs intent conflated in some clips |
| **Bluebeam (via Rendervi round-up)** `[O SRC-263]` | early adopters | 46 % reclaimed 500–1,000 hours; 68 % report ≥$50k savings | Secondhand reporting |
| **Students (design-specific)** `[O SRC-266/267/269]` | workshops N=42; studio cohorts N=17+8 faculty; N=18/24 longitudinal; N=25 Turkey; N=85 questionnaire | 92.9 % used GenAI in design work; 78.4 % mainly ideation; 86.6 % report efficiency gains; 65.5 % fear creativity loss; jury: 67.6 % improved outcomes; GenAI studios: 95–96 % perceived positive creativity effect (self-report caveat: instructors surveyed their own students) | Small N, single-institution, demand characteristics |

**Reading the gap** `[N]`: the United States *individual* number (6 %) and the UK/global *practice* number (74 %) describe different questions — "do architects personally use AI regularly at work" vs "is AI used somewhere in the practice". Both are true. For a student entering the field, the operative facts are: **the tooling is already in the pipeline everywhere large, the individual craft is still being invented, and the profession is watching early-career skill formation with concern (61 %)**.

---

## 3. WHAT THEY ACTUALLY DO — the task map `[O]`

| Task | Practice status | Evidence pattern |
|---|---|---|
| **Concept imagery / ideation** | Most common use, front-end | 44 % (Chaos); "it's just a sketching tool"; students: ideation 78.4 % |
| **Option variations** | Common | 35 %; MJ `--chaos` wide sweeps; "variations of design options" |
| **Photorealism / render enhancement** | Common | 32 % enhance photorealism; 26 % image quality; Enscape AI Enhancer, "render enhanced filters over Lumion exports, very convincing for clients" |
| **Model-conditioned renders (the faithful lane)** | Growing, tool-anchored | Veras in Revit/SketchUp ("Geometry Override 10 %"), SketchUp Diffusion, D5/Enscape hybrids; the standard: lock camera, keep geometry on the tool side |
| **Sketches → renders** | Established student + early-career use | SketchUp screenshot + ChatGPT/Veras workflows; SD+ControlNet for the disciplined; MJ "won't do it as you intend" — *"it will take your supplied image and generate a totally new one"* |
| **Site/yield studies** | Real but specific tools | TestFit (v2 leg): "lay out whole site plans in real time" |
| **Documentation: specs, codes, summaries, emails** | Quietly the highest-hours use | ChatGPT→MasterFormat list (4 h→2.5 h); code-section finding; staircase goings/rise calc — *all* with manual check; "always cross-reference for exceptions" |
| **Drafting / drawings / details** | Explicitly rejected | "LLMs don't work with vectors so that's useless"; "floor plans are way too dependent on a crap load of factors" |
| **Client communication** | Careful, hedged | "Hedge to the client that this is a sketch, not a design"; AI as "presentation assistant" |
| **Disclosure** | Inconsistent | AIA guidance says disclose; practice ranges from labeled to none; the community's word for the failure is *"AI slop"* |

**The public quotes that define the culture** `[O]`:
- *"AI is horrible at designing, especially from scratch… Unserious firms and students will put out obvious AI slop that's uninspiring and crappy."*
- *"They can produce nice images. It just will not be of the actual building you designed."*
- *"It's just a sketching tool."*
- *"I do a lot of AI viz and embellishment of basic concept-level renders… It's an effective tool when you don't have a fully fleshed out design yet"* — same thread.
- *"Can't create reproducible images, so I can't 'move the sofa a little to the left' for our clients."*

---

## 4. HOW THEY PROMPT — the observed practice, categorised `[O]`

**4.1 Three prompt cultures in circulation:**

| Culture | Structure observed in the wild | Consistency mechanism | Where it breaks |
|---|---|---|---|
| **Midjourney art-direction culture** | Formula: *[view] + [building+style] + [materials] + [site] + [time/light] + [mood] + [params]* `[O SRC-278]`; or the minimal *"[subject] in [location], [camera type]"* with "none of that cinematic ultra realistic fluff" `[O SRC-272]`; sketch upload → URL → describe → iterate, *"highlight the features / bits that you'd like to see preserved"* `[O SRC-274]` | `--sref` board palette lock, `--oref` building consistency, seed-lock, `--raw` for line character, `--stylize low` `[O SRC-283]` | Cannot hold the actual building; 4× cost/slowness for sref-heavy boards; every image is a re-roll |
| **Stable-Diffusion control culture** | Prompt = materials/light/style only; geometry from ControlNet (Canny for linework, Depth for 3D views, **MLSD for manmade geometry**); start control strength 0.7–0.8, 0.9+ stiff, 0.5–0.6 drifts; delayed-ControlNet trick (start 0.4) for emergence `[O SRC-280/281]` | Control weights, seeds, preprocessor choice, img2img denoise, upscale second pass | Setup burden; the "no-preserve-list" habit — practitioners trust the tool, not the words |
| **Chat/docs culture** | Five-part structure: role, task, format, constraints, tone — for concept narratives, materials rationale, client emails `[O SRC-276]`; ChatGPT→MasterFormat; goings/rise calc; code lookups — always verified `[O SRC-285/286/287]` | Iteration in-thread; "trained" custom GPTs with firm standards; manual verification habit | Hallucinated code/product facts; "more often than not gives wrong answers" for numeric code work |

**4.2 The folk heuristics (what practitioners tell each other):**
1. *"Keep prompts concise — the fluff does nothing."* (Convergent across MJ users and SD users.)
2. *"Ask it to stick to the proportions."* (Approximates a preserve instruction; partial form of what our harness measures.)
3. *"When it fucks up, start a new prompt — don't build up; it hallucinates heavily."* (Practice-version of our "re-anchor, don't chain" rule.)
4. *"The geometry comes from ControlNet, not the prompt."* (The field's own channel model.)
5. *"Lock the seed / lock the sref before you run the board."* (Style and camera continuity.)
6. *"Always check it against the actual code/product data."* (Verification discipline on the text side.)
7. *"Hedge: this is a sketch, not a design."* (Informal disclosure practice.)

**4.3 Where practice and our measured evidence converge/diverge** `[N]`:
- **Converge:** minimal prompts; restart-on-drift; tool-held geometry; seed/sref for consistency; manual verification of code answers; hedging language.
- **Diverge:** (i) no preserve-list inside generation prompts — practitioners stop at "stick to proportions" while our runs show the explicit keep-list is worth ~2× edge-IoU (§ blind-spot + 3D legs); (ii) verification stops at eyeball + "looks fine" — our plate audit shows required annotations can vanish invisibly; (iii) no annotation/text plan in any captured prompt; (iv) disclosure carried verbally in one-to-one hedging rather than as a plate/board artifact.

---

## 5. EXECUTED — THE PROMPT-PRACTICE AUDIT `[I]`

**Artifact:** `outputs/2026-09-29_prompt-practice-audit.py` (+ `..._results.json`). **Method:** structured content coding of **16 verbatim items** — 15 captured from practitioner sources during this leg (Reddit posts, guides, courses, vendor playbooks) + 1 comparator (our own 3D-leg preserve-list prompt). Each item scored for presence of the signal channels the 3D leg's mechanism model identifies, using explicit keyword lists that ship in the script so any reader can re-run and dispute.

| Channel | Items present | % | Comment |
|---|---|---|---|
| Lighting/material vocabulary | 8/15 | 53 % | The true centre of practice prompts |
| Style/mood vocabulary | 5/15 raw → **4 genuine** | ~27 % | 1 coding artifact (see limits); one item (`P2`) explicitly *rejects* "cinematic ultra realistic fluff" — folk wisdom against our own instinct for adjective stacking |
| Camera/view vocabulary | 4/15 | 27 % | Where "3D-ish" language lives ("axon", "hero angles", "lock camera") |
| Geometry conditioning **mentioned** | 4/15 | 27 % | **All tool-level** (ControlNet/MLSD; Veras Geometry Override; hidden-line exports). None requests geometry through prompt text |
| Consistency devices (seed/sref/oref/lock) | 3/15 | 20 % | The MJ/SD parameter culture in action |
| **Preserve-language** | **2/15** | **13 %** | Both are **meta-advice**, not generation text: "stick to the proportions" `[SRC-272]`; "highlight the features you'd like to see preserved" `[SRC-274]` |
| Negative prompts | 1/15 | 7 % | Mostly absent outside SD templates |
| **Annotation / text planning** | **0/15** | **0 %** | Nobody's prompt mentions labels, title blocks, or the vector-overtype workflow |
| **Disclosure / licence / provenance** | **0/15** | **0 %** | The single regex hit was `P7`'s negative-prompt word "watermark" (i.e., *suppress* watermarks) — a coding artifact, disclosed here rather than silently counted |
| **Comparator** (`P16`, ours) | — | — | The only item combining explicit projection terms with a preserve-list; also the only item whose surrounding protocol includes labels-off rules and verification steps |

**Findings** `[I] [N]`:
1. **The field's prompt practice is styling-led and tool-anchored.** Words carry look; tools carry truth. That division of labour is *correct* — and it is why practitioners who never write a preserve-list still get usable renders (their geometry channel is ControlNet/Veras, not text).
2. **But it leaves the preservation layer unnamed.** Where geometry is *not* tool-held (chat-based img2img from a screenshot; MJ restyles), the captured practice falls back on vague proportions-words — the exact configuration where our executed runs measured the biggest silent loss (naive: ring deleted; view-change: pseudo-rotation).
3. **Verification and custody are absent from the prompt artifact entirely** (0/15). Practitioners verify after the fact (as people, in review) — students rarely have that review layer, which is precisely the gap our protocol's G1–G4 gates fill.
4. **Folk wisdom is not the enemy; it is half a protocol.** Audit result + prior runs → the missing half: *name the keep-list, re-verify with numbers, plan annotations as vectors, disclose on the artifact.*

---

## 6. STUDENTS AND STUDIOS — usage, pedagogy, and the detection climate `[O]/[R]`

**6.1 Usage and outcomes (small-N, single-institution studies — grade `[O]` except where journal `[R]`):**
- 92.9 % of surveyed design students had used GenAI in design work; **78.4 % mainly at ideation/concept**; 86.6 % report workflow efficiency; **65.5 % worry GenAI will reduce their independent creative thinking** `[O SRC-269]`.
- Studio integrations measured: jury scores 67.6 % improved with AI tools (42-student workshop cohort); AI most useful pre-design (mean 4.2/5 across 17 master's students + 8 faculty across six design stages) `[R SRC-267]`; longitudinal GenAI-studio cohort: 95 %/96 % perceived positive creativity effect — with the authors' own caveat that instructor-researchers surveying their own class carries demand-characteristics risk `[O SRC-266]`.
- The MJ-reality gap, measured in a studio workshop (N=10): **70 % of first Midjourney outputs were "different from what they imagined"**; 60 % on the second round; yet 70 % were satisfied with the final image — students learn to *reinterpret* outputs rather than to command them `[O SRC-269]`.
- General higher-ed baselines (non-architecture): 86.4 % of 1,265 surveyed students used AI tools; ~54 % for written assignments; university guidance treats documentation as the defense, not detectors `[O SRC-271/287b]` (ties to blind-spot leg).

**6.2 Pedagogy is formalising fast — prompt engineering as coursework:**
- **Zhejiang University core studio (2024–25):** dual module — 20 h AI skills (LLMs, AIGC, LoRA fine-tuning, ComfyUI basics + advanced) + **four staged ethics seminars** (privacy/copyright → accountability → stylistic authorship & cultural bias → model bias), without altering the studio structure `[R SRC-268]`.
- **Three-phase prompt-engineering curriculum (Boden-based):** combinational form generation → exploratory validation → transformative prompt rewriting, in a first-year "Space and Form" course; instructors had to coach groups on "photo-realistic" phrasing when style-transfer prompts produced composites `[R SRC-275]`.
- **Discipline-agnostic AI-literacy course (2026):** tool-agnostic training in prompt construction, **output verification**, bias detection, attribution documentation; observed trajectory: early single-sentence prompts → late role+context+structured-output prompts, with fewer verification errors `[R SRC-279]`.
- Practitioner-facing courses scope AI honestly: *"renders and reasoning, not drawings or code compliance"* `[O SRC-276]`.

**6.3 The detection climate (how students are *handled*, rightly or not):** 2025–26 produced a cluster of false-positive accusation cases across disciplines — thesis accusations resolved by version history and the accused self-running detectors `[O SRC-289/290]`, a professor's own decade-old paper flagged by the same tool `[O SRC-291]`, a Purdue sweep where code-commit-pattern analysis accused ~300 students `[O SRC-292]`, and guidance that detectors are not sole evidence (blind-spot leg `[SRC-143]`). **The transferable student rule is not "never use AI" — it is "keep the process artifact".** For architecture students the equivalents are: the sketch/CAD/model history, the tool logs, the input provenance, the fidelity numbers (§ blind-spot leg), and the disclosure line — a portfolio of *evidence of making*.

**6.4 What students face beyond class:** employment expectations are shifting toward demonstrated AI fluency alongside domain skill `[O SRC-294]`, while the profession debates junior-role erosion (RIBA: 61 % expect early-career skill acquisition to get harder; Reddit: "makes it even tougher for junior staff to progress"); competition and school rules now typically require disclosure or prohibit outright (blind-spot leg, SRC-142/149/150).

---

## 7. PROFESSIONAL HANDLING — what the institutions now tell practitioners `[D]`

**AIA's toolkit is the clearest public artifact of "how to handle it"** `[D SRC-286/287/288]`:
- **Disclosure guidance:** be candid if asked; *"concealing routine, low-risk AI use creates more risk than disclosing it"*; disclose AI-generated visualizations and AI-assisted analysis; anchor = **Code of Ethics Rule 3.301** (no misleading representations).
- **The rule map firms are being trained on:** 1.101 reasonable care; 3.102 competence for the tools used; 2.101 (copyright — the commentary explicitly references the Copyright Act's architectural-works provisions); 3.401 client confidentiality vs tool data flows; **4.102 responsible control** — you may not seal work you did not control; 5.301 attribution to colleagues.
- **Contract practice:** push "no-AI", "disclose-AI", "no-training-on-data" clauses down to consultants; verify, don't assume; coordinate professional-liability coverage.
- The AIA Trust adds the insurance-eye view: undisclosed GenAI trips candor, confidentiality, and attribution duties; tactics include understanding ToUs (training-on-inputs clauses), transparency statements, and documenting human transformation of outputs `[O SRC-288]`.

**RIBA's 2026 report** maps the same territory from the UK side: benefits real, ROI positive for most, but the open questions are *standards, skills and professional responsibility*, with early-career formation flagged as the sharpest unresolved risk `[O SRC-255/258]`.

**Practice reality on the ground** `[O]`: disclosure in the wild is mostly client-facing hedging; internal use is often quiet ("I don't trust AI and can tell when someone is using it on letters"); some offices push renders while senior staff push back; and the community's monitoring phrase — *"AI slop"* — polices the boundary socially before any rulebook does.

---

## 8. THE SOCIAL-MEDIA LAYER (as directed — what the feeds show about people) `[O]`

| Platform/phenomenon | What it reveals about handling |
|---|---|
| **Instagram restyle culture** — "Eiffel Tower as Gaudí would have designed it" account waves, starchitect-style reimaginings of landmarks, nostalgic + ironic framing `[O SRC-293]` | The dominant public-facing AI-architecture genre is **fan-fiction of icons** — engagement-optimised, authorship-light, and increasingly what non-architects see as "AI architecture" |
| **Disclosure-in-bio reality** — AI-influencer culture: creators disclose, followers ignore; "the lines blur easily" `[O SRC-295]` | Labeling alone does not manage perception; **context of publication** does (relevant to how a student posts process work) |
| **Institutional backlash** — British Museum AI post deleted after archaeologist pushback (Jan 2026) `[O SRC-296]`; Meta's Muse Image profile-picture remixing drew outcry + regulator attention (Jul 2026) `[O SRC-297]` | Public tolerance is thin where AI touches **heritage, identity, or consent** — architecture sits adjacent (buildings are heritage; site photos contain people) |
| **AI spam saturation** — platform-scale studies of AI-generated clickbait eroding trust in feeds `[O SRC-298]`; platform labeling regimes rolling out (TikTok/Meta; EU Art. 50 from Aug 2026 — v2 leg) | Audiences are getting better at pattern-matching "AI look"; unlabeled AI in a professional portfolio now reads as a **liability**, not a flex |
| **Community forums as the real curriculum** — r/Architects, r/midjourney, r/StableDiffusion, r/architecturestudent function as the de facto prompt academy: formulas, parameter lore, warnings, and workflow screenshots `[O throughout §4]` | The Commander's instinct to weight social sources is empirically right: **the technique lives in threads months before it reaches guides** |

---

## 9. SYNTHESIS — practice-vs-evidence, and the six-line student protocol `[N]`

**Where practice is right (adopt as-is):** minimal prompts; tool-held geometry; seed/sref locking; restart-on-drift; verify code/product claims against sources; hedge language with clients; treat AI as front-end sketch and back-end doctoring, not the middle of the job.

**Where the measured evidence extends practice (adopt from our legs):**
1. **Write the keep-list** — the 2/15 gap; worth ~2× geometric fidelity in our harness.
2. **Verify with numbers before delivery** — plate audit + fidelity harness; the field's eyeball verification misses silently deleted annotations.
3. **Viewpoint work goes back to the model** (or image→3D) — never img2img rotation.
4. **Annotations are a vector layer** — 0/15 prompts mention it; PD 1096 review reads labels, not vibes.
5. **Disclosure on the artifact** — the AIA ethics map plus competition/school rules make the disclosure line the cheapest insurance in the workflow.
6. **Keep the process artifact** — version history, inputs, prompts, parameters, outputs; it is simultaneously your defense against false accusation, your ethics compliance, and your portfolio's credibility.

**The six-line protocol for a student's own practice:**
```text
1 CUSTODY   lawful base or own capture; no unlicensed snippets; no watermark pipelines
2 INTENT    freeze what you asked for (atoms + invariants) before any enhancer touches it
3 CHANNELS  preserve-list in words; geometry in the tool (ControlNet / model export / viewport)
4 ITERATE   one variable at a time; restart on drift; keep the prompt log
5 VERIFY    fidelity harness + plate audit + annotation redraw (vectors)
6 DECLARE   disclosure line on the board; originals + logs retained
```

---

## 10. CONFLICTS & LIMITS

| # | Position A | Position B | Status |
|---|---|---|---|
| 1 | "AI adoption is near-universal" (98 % leaders, Autodesk) `[D]` | "Only 6 % of US architects use it regularly" (AIA) `[O]` | **RESOLVED as framing**: leader/tool-presence vs individual regular use; quote both or neither |
| 2 | "AI improved my productivity" (73 % RIBA users; 84 % Autodesk) `[O]/[D]` | "More problems than not; we avoid it" (r/Architects practitioners) `[O]` | **OPEN — perception vs task-dependence**: gains concentrate in viz/docs, losses in precision work |
| 3 | Practitioners trust tool-held geometry (ControlNet/Veras) `[O]` | Our runs show lossy paths survive tool-held setups only when input is clean; snippet inputs degrade invisibly `[I]` | **SUPPORTED both ways** — tool discipline works; input hygiene + verification still required |
| 4 | Studios normalise AI and report creativity gains `[R]/[O]` | 61 % of RIBA respondents expect early-career skills to suffer; 65.5 % of students fear creativity loss `[O]` | **OPEN — the profession's central dispute**, unresolved by current evidence |
| 5 | Social platforms label and users "see" AI `[O]` | Studies and backlash show labeling ≠ perception; disclosure-in-bio ignored `[O]` | **OPEN** — context and provenance do more work than labels |
| 6 | Audit coding artifacts: negation ("none of that cinematic fluff") scores as presence; "watermark" in a negative prompt scored as provenance | — | **DISCLOSED in §5**, corrected manually in the table; script ships the keyword lists so it can be improved |

**Limits** `[N]`: the adoption figures are surveys — self-selecting, heterogeneous definitions, one-year snapshots; the studio studies are small-N and some were run by the instructors who graded the students; the audit codes 16 items with a deterministic keyword instrument, and a human coder would disagree with some cells — the lists ship in the script precisely so the disagreement can be *executed*; social quotes are individuals, not the profession. Nothing here is Nota or Core; the social layer is practice signal at `[O]` cap.

---

## 11. REFERENCES — S012 practice leg (SRC-248 … SRC-299)

**Adoption & industry reports:** SRC-248 Rendershop adoption round-up (6/59/46 % synthesis) `[O]` · SRC-249 Fast Company — AIA 6 % report `[O]` · SRC-250 Dezeen — AIA study detail (53 % experimented; concerns) `[O]` · SRC-251 AIA×Deltek — Journey to Specification briefing `[O]` · SRC-252 Archinect — 2025 year-in-AI recap (Autodesk optimism dip; RIBA president) `[O]` · SRC-255 RIBA — AI Report 2026 (74 %) `[O]` · SRC-256 Toffu — RIBA 2025 (59 %; 41 % in 2024) `[O]` · SRC-257 Autodesk — 2026 AI Pulse (98 %/84 %/59 %) `[D]` · SRC-258 ProjectFlux — RIBA 2026 analysis (31 % intensive; 61 % early-career) `[O]` · SRC-259 Chaos — 2025 State of ArchViz (44/35/32/26 %) `[O]` · SRC-260 Chaos — AI workflows page (Enscape/Veras bundle) `[O]` · SRC-261 Elmtec — Enscape AI overview (55 % exploring/adopting) `[O]` · SRC-262 Architizer — State of ArchViz webinar (56 % active; use cases) `[O]` · SRC-263 Rendervi — 2026 research round-up (Bluebeam hours/savings; Chaos 4th survey) `[O]` · SRC-264 Chaos — best AI rendering tools 2026 (Veras 7-platform integration) `[O]` · SRC-293b Autodesk — State of Design & Make AI spotlight (maturity perception gap) `[D]`

**Prompting practice (guides & formulas):** SRC-278 MeltFlexAI — 45 MJ architecture prompts (six-part formula; `--sref/--oref/--hd` board workflow; cost note) `[O]` · SRC-279b Medium (S. Adineni) — MJ prompting elements `[O]` · SRC-280 Archgyan — SD for architectural rendering (ControlNet workflow; 0.7–0.8 start; "geometry comes from ControlNet") `[O]` · SRC-281 agentbus — SD+ControlNet build (prompt template; negative list; weights) `[O]` · SRC-283 The Architect's Diary — image generator review (Playbooks A/B/C; seed-lock; Veras Geometry Override 10 %; privacy note on public galleries) `[O]` · SRC-276 prompt-architects.com — structured prompt course (role/task/format/constraints/tone; scope limits) `[O]`

**Reddit & community (practice signal, `[O]`-capped):** SRC-271b r/midjourney — prompting and iteration (zoo example; ChatGPT-brainstorm → refine pipeline) · SRC-272 r/midjourney — architect's MJ creations ("[subject] in [location], [camera type]"; "none of that cinematic fluff"; RAW mode; concise is key) · SRC-273 r/midjourney — "Midjourney for Architecture" (dissertation student; "MJ won't let you see the same building from different angles"; inspiration-only verdict) · SRC-274 r/midjourney — sketch→artwork iteration (upload URL loop; "highlight the features you'd like preserved") · SRC-275b r/architecture — AI-generated drawings 2022 (variable-stacking mental model; "no diagrammatic reasoning") · SRC-276b r/midjourney — "render just the rendering step" (architecture student; MJ "will not accomplish what you're looking to do") · SRC-277b r/Architects — "AI made my top rendering artist's job obsolete" ("just a sketching tool"; "can't use AI for final renders") · SRC-285 r/Architects — ChatGPT for drawings? (code lookups with checks; staircase calc; zoning analysis; "always cross reference") · SRC-286b r/Architects — tired of hype (code GPT "dead wrong"; search replacement; spec MasterFormat 4 h→2.5 h; email cleanup) · SRC-287b r/civilengineering + r/StructuralEngineering — ChatGPT uses (submittal review; contract fault analysis; "emails and yearly goals"; "design: not ok") · SRC-288b r/Architects — AI rendering? ("shipping container mural" mismatch example; "presentation assistant" economics) · SRC-289b r/Architecturestudent — best AI for renders ("I hand drew; everyone else used AI"; tool recommendations) · SRC-290b r/Architects — "AI is making me depressed" (impossible renders; client-side cynicism; "they see shiny render") · SRC-291b r/Architects — how many firms push AI design ("AI slop"; "floor plans too dependent"; "move the sofa" reproducibility) · SRC-292b r/Architects — firm workflows ("AI render-enhanced Lumion exports… gutting"; deadline-only use) · SRC-293c r/archviz — boss review thread (presentability, lighting consistency critiques)

**Students & pedagogy:** SRC-265 Pith — GenAI in architectural design studios (95/96 % perceived creativity; demand-characteristics critique) `[O]` · SRC-266 MDPI Buildings 16(7):1445 — six-stage human–AI studio study (N=17+8; pre-design 4.2/5) `[R]` · SRC-267 ResearchGate — impact of GenAI hands-on (85 respondents; 75/72.5/50/48 % by task; +14 % form/aesthetics; 33 % want critical-thinking training) `[O]` · SRC-269 Education Sciences / RG — students' perceptions of AI image tools (N=42; 92.9 %; 78.4 % ideation; 65.5 % creativity concern; jury 67.6 %) `[O]` · SRC-269b Springer AI-a-ADS — MJ studio workshop (70 % outputs ≠ imagined; 70 % satisfied; 2.6/5 integration) `[O]` · SRC-275 Tandfonline — prompt engineering & creativity in architectural education (three-phase Boden curriculum) `[R]` · SRC-268 MDPI Buildings 15(17):3069 — Zhejiang dual-module studio (20 h skills; four ethics seminars) `[R]` · SRC-279 arXiv — discipline-agnostic AI literacy course (verification/attribution competencies; prompt sophistication growth) `[R]` · SRC-271 Pedagogical Research — how college students use ChatGPT (Guelph; 86.4 %; 53.8 % written assignments) `[O]` · SRC-294 Metaintro — entry-level hiring AI fluency 2026 `[O]`

**Detection climate (student handling):** SRC-289 r/edtech — accused thesis, version history defense `[O]` · SRC-290 Daily Dot — student vs professor detector reversal `[O]` · SRC-291 r/GradSchool — accusation thread (10-year-old paper flagged) `[O]` · SRC-292 r/Professors — Purdue commit-pattern sweep (~300 students) `[O]`

**Institutions & ethics:** SRC-286 AIA — AI Task Force (position statement; firm guidance) `[D]` · SRC-287 AIA — AI Firm Toolkit (disclosure guidance; Code rules map 3.301/4.102/3.401/2.101/1.101/3.102/5.301) `[D]` · SRC-288 AIA Trust — ethical challenges of GenAI (candor, confidentiality, attribution; NIST AI RMF; ToU tactics) `[O]` · SRC-288c Proving Ground — five ethical confrontations (seal/responsible control; energy) `[O]`

**Social-media layer:** SRC-293 Domus — Instagram architect-restyle culture `[O]` · SRC-295 Wired — AI influencer disclosure reality `[O]` · SRC-296 Artnet — British Museum AI post backlash `[O]` · SRC-297 BBC — Meta Muse Image outcry `[O]` · SRC-298 NPR — AI-generated spam study `[O]` · SRC-299 YouTube — ESOARCH AI-for-architects course + MJ V6 guide (tutorial ecosystem) `[O]`

*Registry note: IDs assigned across SRC-248…SRC-299 with letter-suffixed sub-rows used where several results belong to one source family; the canonical registry rows for this leg are appended in `01-research/REFERENCES.md`. Drafting IDs **253, 254, 270, 277, 282, 284** carry no delivered citation (253/270/277/284 folded out of their cluster cites at registry reconciliation so every citation traces to a registry row; 254/282 never used) — declared gaps, next free ID remains SRC-300. Quota: report/analysis class + social class (largest block), per the Commander's directive.*

*Sentinel: §5 numbers reproduce from `outputs/2026-09-29_prompt-practice-audit.py` + `..._results.json` (keyword lists included); every quote traces to the registry; social evidence capped `[O]`; `[S]`-class suggestions remain in §9 as protocol text only — nothing promoted.*
