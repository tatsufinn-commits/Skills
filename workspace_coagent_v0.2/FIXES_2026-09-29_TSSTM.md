# FIXES — TSSTM v0.2.1 polish (2026-09-29, S021)

Commander-ordered workspace polish ("let's work on it to make it possible").
All changes local in the Skills workspace, awaiting Commander push. Evidence: S020
review (outputs/2026-09-29_coagent-workspace-review.md) + S021 tests.

| Finding | Fix | File | Test |
|---|---|---|---|
| **F-1** turn numbering counted any `### T` in the file — a body *mentioning* the pattern skipped a number (self-demonstrated live in the S020 pilot: T1 → T3) | count **anchored** headers only: `re.findall(r"^### T(\d+)", text, re.M)`; extracted `next_turn()` / `render_block()` / `main_cli()` for testability (CLI unchanged) | `scripts/append_turn.py` | `test_counts_anchored_headers_only`, `test_sequential_numbering_despite_body_mention`, `test_init_append_outcome_cycle` |
| **F-3** append left the file handle unclosed | `with path.open("a") as fh:` | `scripts/append_turn.py` | tests run under `warnings.simplefilter("error", ResourceWarning)` |
| **F-4** meeting ID interpolated into `sed` unescaped — `/`, `&`, `;` would corrupt substitution | charset validation before use: letters/digits/`.`/`_`/`-` only, fail fast with a clear error; simplified the double-sed to one pass | `scripts/init_meeting.sh` | `test_rejects_unsafe_ids` (a/b, x&y, semi;colon, "sp ace", "") |
| **F-2** write-permission table cited unnumbered filenames (`MESSAGES.md`, `ROSTER.md`…) while shipped files are numbered (`02_MESSAGES.md`, `01_ROSTER.md`…) | table rewritten to the numbered room files + path note appended | `extension/BRANCH_TEAM_PROTOCOL.md` | `test_creates_room_with_placeholders_filled` (numbered files exist) |

**NOT fixed (needs Design pass):**
- **F-5** "Marciale (thin)" in GROUND_RULES.md remains unglossed — I will not invent meaning (flag, never fill).
- **F-6** the letter's capability wording ("branches are in your hands") — the Design pass's own document to amend; the package docs already state the Commander-carrier reality.

**Verification:** `python3 tests/test_scripts.py` → **10/10 OK** (from `workspace_coagent_v0.2/`; stdlib only; pycache excluded). Regression suite added at `tests/test_scripts.py` — run it with any future edit to these scripts.
