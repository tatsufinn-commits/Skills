#!/usr/bin/env python3
"""@reimagine v0.1.2 — configuration grader.

Grades a CONFIG_WORKSHEET markdown file against the six CORE configuration
checks (C1-C6) plus one conditional check — F11 tool settings, which fires
only when PHOTO: yes, giving seven result rows (six for text-only runs).
Scores the PACKAGE (completeness, explicitness, law, QA decidability,
traceability, disclosure) — never image quality, which stays [N] until a
runtime measurement tranche. Stdlib only; no network; no subprocess.

Usage:  python3 evals/grader.py <worksheet.md>     → exit 0 PASS / 1 FAIL
        Invalid usage or a missing/unreadable worksheet exits 2.
"""

import re
import sys

REQUIRED_KEYS = ["TASK", "CARD", "PROVIDER", "PHOTO", "PHOTO_SOURCE",
                 "SCHOOL", "STYLE_AUTHORITY", "RATIONALE"]
REQUIRED_SECTIONS = ["paste text", "preserve list", "alter list", "qa gate"]
KNOWN_KEYS = set(REQUIRED_KEYS + ["AUDIENCE", "DEADLINE"])

PROJECTION_RE = re.compile(
    r"(camera|viewpoint|elevation|eye-?level|aerial|perspective|projection"
    r"|section|framing|\bview\b|\bplan\b)", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(
    r"⟨|\btodo\b|\btbd\b|placeholder|\[replace|\bfill in\b", re.IGNORECASE)
# CMI tripwire (v0.1.2, R1): inflected action stems (covering nominalizations
# such as removal/deletion/erasure via stem+\w*), pluralized mark nouns, BOTH
# word orders (verb→mark and mark→verb), with a negation window so compliance
# prose ("watermarks must never be removed") is not flagged. Lexical
# tripwire, not enforcement — paraphrase-level evasion still passes; the
# refusal duty is the operator's (see VECTORS.md and card G2).
CMI_ACTION_RE = r"(?:remov|eras|strip|delet|obscur|scrub|wip|clean)\w*"
CMI_MARK_RE = r"(?:watermark|credit|attribution|logo)s?|CMI"
CMI_FORWARD_RE = re.compile(
    r"\b(?:" + CMI_ACTION_RE + r")(?:\W+\w+){0,4}\W+(?:" + CMI_MARK_RE + r")\b",
    re.IGNORECASE)
CMI_REVERSED_RE = re.compile(
    r"\b(?:" + CMI_MARK_RE + r")(?:\W+\w+){0,3}\W+(?:" + CMI_ACTION_RE + r")\b",
    re.IGNORECASE)
CMI_NEGATED_RE = re.compile(
    r"\b(?:not|never|no|don'?t|doesn'?t|didn'?t|can'?t|cannot|mustn'?t|won'?t"
    r"|isn'?t|aren'?t|without|avoid)\b", re.IGNORECASE)


def _cmi_violations(text):
    """Return CMI-violation spans found in `text`.

    A candidate span is suppressed when a negation sits inside the span or in
    the 24 characters preceding it, so instructions to preserve marks are not
    misread as instructions to destroy them.
    """
    hits = []
    for pattern in (CMI_FORWARD_RE, CMI_REVERSED_RE):
        for match in pattern.finditer(text):
            window = text[max(0, match.start() - 24):match.end()]
            if not CMI_NEGATED_RE.search(window):
                hits.append(match.group(0).strip())
    return hits
NAMED_STYLE_RE = re.compile(
    r"(?i:style\s+of|manner\s+of|work\s+of|inspired\s+by)\s+"
    r"(?:the\s+)?[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’-]*"
    r"(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’-]*)*")
CHECK_VERB_RE = re.compile(
    r"\b(verify|confirm|compare|count|check|measure|overlay|inspect|validate)\b",
    re.IGNORECASE)
CARD_IDS = frozenset((
    "A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08", "A09", "A10", "A11", "A12",
    "P01", "P02", "P03", "P04", "P05", "P06", "P07", "P08", "P09", "P10",
    "D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10",
    "T01", "T02",
))
ELIGIBLE_PHOTO_SOURCES = frozenset(("own", "licensed", "cleared"))
URL_RE = re.compile(r"https?://\S+")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
TEXT_ONLY_PRESERVE = "N/A — text-only brief; fidelity claims dropped"

CHECK_NAMES = {
    "C1": "completeness", "C2": "explicitness", "C3": "lawful",
    "C4": "QA decidability", "C5": "traceability", "C6": "disclosure",
}


def parse(text):
    """Parse worksheet text into (known keys, normalized sections).

    Only documented key names are recognized. Key-like lines in a section stay
    section content, so ordinary QA, settings, and log prose cannot overwrite
    the worksheet header fields.
    """
    keys, sections, current = {}, {}, None
    for line in text.splitlines():
        header = re.match(r"^##\s+(.+?)\s*$", line)
        if header:
            current = header.group(1).lower()
            sections.setdefault(current, [])
            continue
        key = re.match(r"^([A-Z][A-Z_]*):\s*(.*)$", line)
        if key and key.group(1) in KNOWN_KEYS:
            keys[key.group(1)] = key.group(2).strip()
            continue
        if current is not None:
            sections[current].append(line)
    return keys, sections


def _items(sections, name):
    out = []
    for line in sections.get(name, []):
        item = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if item:
            out.append(item.group(1))
    return out


def _qa_boxes(sections):
    out = []
    for line in sections.get("qa gate", []):
        box = re.match(r"^\s*-\s*\[( |x|X)\]\s*(.+?)\s*$", line)
        if box:
            out.append(box.group(2))
    return out


def _paste_text(sections):
    lines = [ln.strip() for ln in sections.get("paste text", [])]
    return "\n".join(ln for ln in lines if ln and not ln.startswith("```"))


def _has_affirmative_reject_drift_rule(lines):
    """Require an anchored, affirmative reject-drift instruction with escalation."""
    for line in lines:
        match = re.match(r"^\s*REJECT-DRIFT RULE:\s*(.*)$", line, re.IGNORECASE)
        if not match:
            continue
        rule = match.group(1)
        lower = rule.lower()
        if not re.search(r"\breject\b", lower) or not re.search(r"\bdrift\b", lower):
            continue
        if not re.search(r"\b(authoritative|redo|editor)\b", lower):
            continue
        # Disallow formulations such as "never reject outputs; drift is
        # acceptable" even though they contain all three required keywords.
        if re.search(
                r"\b(?:never|not|no|don't|dont|cannot|can't)\b"
                r"(?:\W+\w+){0,3}\W+reject\b", lower):
            continue
        if re.search(
                r"\b(?:never|not|no|don't|dont|cannot|can't|avoid|skip)\b"
                r"(?:\W+\w+){0,4}\W+(?:authoritative|redo|editor)\b", lower):
            continue
        return True
    return False


def grade(path):
    """Return (all_pass, results) with results = [(code, passed, detail)]."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    keys, sections = parse(text)
    results = []

    # C1 — completeness -----------------------------------------------------
    problems = []
    for key in REQUIRED_KEYS:
        if not keys.get(key):
            problems.append("missing/empty key %s" % key)
    for section in REQUIRED_SECTIONS:
        if section not in sections:
            problems.append("missing section '%s'" % section)
    paste = _paste_text(sections)
    if REQUIRED_SECTIONS[0] in sections and not paste.strip():
        problems.append("paste text is empty")
    scanned = "\n".join(text for content in sections.values()
                        for text in content)
    scanned += "\n" + "\n".join(keys.values())
    hits = PLACEHOLDER_RE.findall(scanned)
    if hits:
        problems.append("placeholder tokens present: %s" % sorted(set(hits)))
    results.append(("C1", not problems, "; ".join(problems) or
                    "all keys/sections present, no placeholders"))

    # C2 — explicitness -----------------------------------------------------
    photo = keys.get("PHOTO", "").strip().lower()
    problems = []
    if photo == "yes":
        preserve, alter = _items(sections, "preserve list"), _items(sections, "alter list")
        if not preserve:
            problems.append("no preserve items")
        if not alter:
            problems.append("no alter items")
        if preserve and not PROJECTION_RE.search(" ".join(preserve)):
            problems.append("preserve list lacks the projection/view invariant")
    elif photo == "no":
        preserve_items = _items(sections, "preserve list")
        alter_items = _items(sections, "alter list")
        if TEXT_ONLY_PRESERVE not in preserve_items:
            problems.append("preserve list must contain the literal text-only N/A line")
        if not any(item == "N/A" or item.startswith("N/A ") for item in alter_items):
            problems.append("alter list must contain an N/A item for text-only briefs")
    else:
        problems.append("PHOTO key must be yes/no")
    detail = "; ".join(problems) if problems else (
        "preserve/alter lists explicit, projection invariant present" if photo == "yes"
        else "documented N/A preserve/alter items; fidelity claims dropped")
    results.append(("C2", not problems, detail))

    # C3 — lawful -----------------------------------------------------------
    problems = []
    source = keys.get("PHOTO_SOURCE", "").strip().lower()
    if photo == "yes":
        if source not in ELIGIBLE_PHOTO_SOURCES:
            problems.append("Gate 0 — rights unresolved; do not emit.")
    elif photo == "no":
        if source not in ELIGIBLE_PHOTO_SOURCES and source != "none":
            problems.append("PHOTO_SOURCE must be none when PHOTO is no")
    elif source not in ELIGIBLE_PHOTO_SOURCES and source != "none":
        problems.append("PHOTO_SOURCE not eligible (%r) — Gate 0 blocks emission" % source)
    forbidden = _cmi_violations(text)
    if forbidden:
        problems.append("watermark/CMI removal language: %s" % forbidden)
    authority = keys.get("STYLE_AUTHORITY", "")
    if not authority:
        problems.append("style authority unstated")
    elif NAMED_STYLE_RE.search(authority) or NAMED_STYLE_RE.search(text):
        problems.append("named-style imitation — reformulate to a lawful rung "
                        "(movement/palette, own precedent, public-domain master)")
    results.append(("C3", not problems, "; ".join(problems) or
                    "source eligible, CMI intact, style authority lawful"))

    # C4 — QA decidability --------------------------------------------------
    problems = []
    boxes = _qa_boxes(sections)
    if len(boxes) < 5:
        problems.append("only %d QA boxes (need >=5)" % len(boxes))
    undecidable = [b for b in boxes if not CHECK_VERB_RE.search(b)]
    if undecidable:
        problems.append("QA lines without a check verb: %d" % len(undecidable))
    if not _has_affirmative_reject_drift_rule(sections.get("qa gate", [])):
        problems.append("anchored affirmative REJECT-DRIFT RULE with escalation missing")
    results.append(("C4", not problems, "; ".join(problems) or
                    "%d decidable QA checks + affirmative reject-drift rule" % len(boxes)))

    # C5 — traceability -----------------------------------------------------
    problems = []
    card = keys.get("CARD", "").strip()
    if card not in CARD_IDS:
        problems.append("CARD must be one of the 34 enumerated atlas IDs (A01-A12, P01-P10, "
                        "D01-D10, T01-T02)")
    rationale = keys.get("RATIONALE", "").strip()
    rationale_non_ws = re.sub(r"\s+", "", rationale)
    rationale_tokens = re.findall(r"[\w'-]+", rationale.casefold())
    # Floor adopted per ruling D-003 (teamwork-lt-001): MENDER's stricter
    # union. Lexical by construction — six distinct junk tokens still pass;
    # the depth limit is declared in the fix record, not pretended away.
    if (len(rationale_non_ws) < 30 or len(rationale_tokens) < 6
            or len(set(rationale_tokens)) < 5):
        problems.append("RATIONALE must be substantive (>=30 non-whitespace "
                        "chars, >=6 tokens, >=5 distinct tokens)")
    if not keys.get("PROVIDER"):
        problems.append("PROVIDER unstated")
    results.append(("C5", not problems, "; ".join(problems) or
                    "card/provider/rationale traceable"))

    # C6 — disclosure -------------------------------------------------------
    school = keys.get("SCHOOL", "").strip().lower()
    problems = []
    if school == "yes":
        disclosure = " ".join(sections.get("disclosure", []))
        if "disclosure" not in sections:
            problems.append("school context flagged but no Disclosure section")
        else:
            if not URL_RE.search(disclosure):
                problems.append("disclosure lacks a URL")
            if not DATE_RE.search(disclosure):
                problems.append("disclosure lacks an access date (YYYY-MM-DD)")
            if "prompt" not in disclosure.lower():
                problems.append("disclosure lacks a prompt description")
    elif school != "no":
        problems.append("SCHOOL key must be yes/no")
    detail = "; ".join(problems) if problems else (
        "disclosure complete (URL, access date, prompt description)" if school == "yes"
        else "no school context — disclosure N/A")
    results.append(("C6", not problems, detail))

    # F11 — photo tools -----------------------------------------------------
    if photo == "yes":
        tool_items = _items(sections, "tool settings")
        tool_ok = bool(tool_items)
        tool_detail = ("tool settings section contains >=1 item" if tool_ok else
                       "PHOTO=yes requires a tool settings section with >=1 item")
        results.append(("F11", tool_ok, tool_detail))

    return all(passed for _, passed, _ in results), results


def main(argv):
    if len(argv) != 2:
        print("usage: python3 evals/grader.py <worksheet.md>", file=sys.stderr)
        return 2
    path = argv[1]
    try:
        passed, results = grade(path)
    except OSError as exc:
        if isinstance(exc, FileNotFoundError):
            print("error: worksheet not found: %s" % path, file=sys.stderr)
        else:
            print("error: cannot read worksheet %s: %s" % (path, exc), file=sys.stderr)
        return 2
    for code, ok, detail in results:
        print("%s %-4s %-16s %s" % ("PASS" if ok else "FAIL", code,
                                    CHECK_NAMES.get(code, "tool settings"), detail))
    passed_count = sum(1 for _, ok, _ in results if ok)
    print("— %d/%d checks passed" % (passed_count, len(results)))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
