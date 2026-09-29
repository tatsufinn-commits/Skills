#!/usr/bin/env python3
"""@reimagine v0.1 — configuration grader.

Grades a CONFIG_WORKSHEET markdown file against the six configuration checks
(C1-C6). Scores the PACKAGE (completeness, explicitness, law, QA decidability,
traceability, disclosure) — never image quality, which stays [N] until a
runtime measurement tranche. Stdlib only; no network; no subprocess.

Usage:  python3 evals/grader.py <worksheet.md>     → exit 0 PASS / 1 FAIL
"""

import re
import sys

REQUIRED_KEYS = ["TASK", "CARD", "PROVIDER", "PHOTO", "PHOTO_SOURCE",
                 "SCHOOL", "STYLE_AUTHORITY", "RATIONALE"]
REQUIRED_SECTIONS = ["paste text", "preserve list", "alter list", "qa gate"]

PROJECTION_RE = re.compile(
    r"(camera|viewpoint|elevation|eye-?level|aerial|perspective|projection"
    r"|section|framing|\bview\b|\bplan\b)", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(
    "⟨|todo|tbd|placeholder|\\[replace|\\bfill in\\b", re.IGNORECASE)
FORBIDDEN_RE = re.compile(
    r"(remove|erase|strip|clean)\s+(the\s+)?(watermark|credit)", re.IGNORECASE)
NAMED_STYLE_RE = re.compile(r"style of\s+[A-Z]")
CHECK_VERB_RE = re.compile(
    r"(verify|confirm|compare|count|check|measure|overlay|inspect|validate)",
    re.IGNORECASE)
CARD_RE = re.compile(r"^(A|P|D|T)\d{2}$")
URL_RE = re.compile(r"https?://\S+")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

CHECK_NAMES = {
    "C1": "completeness", "C2": "explicitness", "C3": "lawful",
    "C4": "QA decidability", "C5": "traceability", "C6": "disclosure",
}


def parse(text):
    """Parse worksheet text into (keys, sections). KEY: lines are
    position-agnostic; '## Header' lines open sections."""
    keys, sections, current = {}, {}, None
    for line in text.splitlines():
            header = re.match(r"^##\s+(.+?)\s*$", line)
            if header:
                current = header.group(1).lower()
                sections.setdefault(current, [])
                continue
            key = re.match(r"^([A-Z][A-Z_]*):\s*(.*)$", line)
            if key:
                keys[key.group(1)] = key.group(2).strip()
                continue
            if current is not None:
                sections[current].append(line)
    return keys, sections


def _items(sections, name):
    out = []
    for line in sections.get(name, []):
        item = re.match(r"^\s*-\s+(.+?)\s*$", line)
        if item and not item.group(1).startswith("N/A"):
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
    scanned = paste + " " + " ".join(keys.get(k, "") for k in REQUIRED_KEYS)
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
        for name in ("preserve list", "alter list"):
            joined = " ".join(sections.get(name, []))
            if "N/A" not in joined:
                problems.append("'%s' must carry the N/A line for text-only briefs" % name)
    else:
        problems.append("PHOTO key must be yes/no")
    results.append(("C2", not problems, "; ".join(problems) or
                    "preserve/alter lists explicit, projection invariant present"
                    if photo == "yes" else "text-only brief correctly drops fidelity claims"))

    # C3 — lawful -----------------------------------------------------------
    problems = []
    source = keys.get("PHOTO_SOURCE", "").strip().lower()
    if source not in ("own", "licensed", "cleared", "none"):
        problems.append("PHOTO_SOURCE not eligible (%r) — Gate 0 blocks emission"
                        % source)
    forbidden = FORBIDDEN_RE.findall(text)
    if forbidden:
        problems.append("watermark/CMI removal language: %s" % forbidden)
    authority = keys.get("STYLE_AUTHORITY", "")
    if not authority:
        problems.append("style authority unstated")
    elif NAMED_STYLE_RE.search(authority):
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
    joined_qa = " ".join(sections.get("qa gate", []))
    if not ("reject-drift" in joined_qa.lower()
            or ("reject" in joined_qa.lower() and "drift" in joined_qa.lower())):
        problems.append("REJECT-DRIFT rule line missing")
    results.append(("C4", not problems, "; ".join(problems) or
                    "%d decidable QA checks + reject-drift rule" % len(boxes)))

    # C5 — traceability -----------------------------------------------------
    problems = []
    if not CARD_RE.match(keys.get("CARD", "")):
        problems.append("CARD must match (A|P|D|T)+2 digits (atlas ID)")
    if len(keys.get("RATIONALE", "")) < 15:
        problems.append("RATIONALE too thin (<15 chars)")
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
    results.append(("C6", not problems, "; ".join(problems) or
                    "disclosure complete (URL, access date, prompt description)"
                    if school == "yes" else "no school context — disclosure N/A"))

    return all(passed for _, passed, _ in results), results


def main(argv):
    if len(argv) != 2:
        print("usage: python3 evals/grader.py <worksheet.md>")
        return 2
    passed, results = grade(argv[1])
    for code, ok, detail in results:
        print("%s %-4s %-16s %s" % ("PASS" if ok else "FAIL", code,
                                    CHECK_NAMES[code], detail))
    passed_count = sum(1 for _, ok, _ in results if ok)
    print("— %d/6 checks passed" % passed_count)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
