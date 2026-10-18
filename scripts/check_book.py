#!/usr/bin/env python3
"""Run every mechanical check from the guide on one book folder.

Usage: python3 scripts/check_book.py "<book folder>"
Reads metadata.json, manuscript.md, book.epub, cover-ebook.jpg, and the topic entry in
ebook-topics/topics-log.json. Prints JSON with each check and pass/fail. Exit 0 = all pass.
Judgement checks (facts, reading quality, sensitive content) are NOT here: the robot reviews those.
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

AI_LINE = ("This book was created with the assistance of artificial intelligence tools. "
           "All content was reviewed and edited by the publisher.")
PLACEHOLDER = re.compile(r"\[(insert|tbd|todo|placeholder|name|author)|lorem ipsum|\bTODO\b|\bTBD\b|XXX", re.I)


def words_in_range(text):
    nums = [int(n.replace(",", "")) for n in re.findall(r"\d[\d,]*", text)]
    return (min(nums), max(nums)) if len(nums) >= 2 else (nums[0], nums[0]) if nums else (None, None)


def topic_for(folder):
    """Find the topic whose slug matches the book folder name (the picker's rule)."""
    base = os.path.basename(os.path.normpath(folder))
    with open(os.path.join(REPO, "ebook-topics", "topics-log.json"), encoding="utf-8") as f:
        for entry in json.load(f):
            topics = ([entry["selected_topic"]] if entry.get("selected_topic") else []) + (entry.get("selected_topics") or [])
            for t in topics:
                if t and t.get("topic_name") and slug(t["topic_name"]).startswith(base):
                    return t
    return None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", norm(s)).strip("-")


def norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def find_jar():
    """The epubcheck jar from the pip package (pip install --break-system-packages epubcheck)."""
    try:
        import epubcheck
        path = os.path.join(os.path.dirname(epubcheck.__file__), "epubcheck.jar")
        return path if os.path.exists(path) else ""
    except ImportError:
        return ""


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = sys.argv[1]
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    epubs = [n for n in os.listdir(folder) if n.endswith(".epub")]
    has_cover = os.path.exists(os.path.join(folder, "cover-ebook.jpg"))
    for name in ["manuscript.md", "metadata.json", "review-notes.md"]:
        add(f"file present: {name}", os.path.exists(os.path.join(folder, name)))
    add("file present: EPUB", bool(epubs), ", ".join(epubs) or "none")
    add("file present: cover-ebook.jpg", has_cover, "" if has_cover else "not made yet (Kindle-3 makes it)")
    add("file present: style.css", os.path.exists(os.path.join(folder, "style.css")), "stylesheet for the EPUB (guide section 7)")
    fonts_dir = os.path.join(folder, "fonts")
    licences = [n for n in os.listdir(fonts_dir) if "LICENSE" in n.upper() or "LICENCE" in n.upper()] if os.path.isdir(fonts_dir) else []
    add("font licence file saved (fonts/)", bool(licences), ", ".join(licences) or "no licence file in fonts/ (guide section 5)")
    required = [c for c in checks if "cover" not in c["check"]]
    if not all(c["pass"] for c in required):
        print(json.dumps({"folder": folder, "pass": False, "checks": checks}, indent=2))
        return 1

    m = json.load(open(os.path.join(folder, "metadata.json"), encoding="utf-8"))
    add("guide_version is 2.1", str(m.get("guide_version")) == "2.1", f"metadata says {m.get('guide_version')}")
    manuscript = open(os.path.join(folder, "manuscript.md"), encoding="utf-8").read()
    body_words = len(re.findall(r"\S+", manuscript))

    add("title and subtitle set", m.get("title") and m.get("subtitle"))
    add("author is Skybee", m.get("author") == "Skybee", str(m.get("author")))
    desc_words = len(str(m.get("description", "")).split())
    add("description 150-400 words", 150 <= desc_words <= 400, f"{desc_words} words")
    kws = m.get("keywords", [])
    add("exactly 7 keywords", len(kws) == 7, f"{len(kws)} keywords")
    long_kw = [k for k in kws if len(k) >= 50]
    add("each keyword under 50 characters", not long_kw, ", ".join(long_kw) or "ok")
    cats = m.get("kdp_categories") or ([m["kdp_category"]] if m.get("kdp_category") else [])
    add("two KDP categories", len(cats) >= 2, f"{len(cats)} category listed; guide needs 2")
    pool = {c["category"]: c for c in json.load(open(os.path.join(REPO, "ebook-topics", "category-pool.json"), encoding="utf-8"))["categories"]}
    for cat in cats[:2]:
        entry = pool.get(cat)
        add(f"category in pool and confirmed: {cat[-40:]}", bool(entry and entry.get("confirmed")),
            "not in pool" if not entry else ("confirmed" if entry.get("confirmed") else "owner has not confirmed this path yet"))
    ks = str(m.get("kdp_select", "")).strip().lower()
    want_ks = "enroll for 90 days" if m.get("series") else "no"
    add("KDP Select matches series rule", ks == want_ks,
        f"kdp_select '{m.get('kdp_select')}'; series {'yes' if m.get('series') else 'no'} needs '{want_ks}' (guide section 9)")
    age = str(m.get("reading_age", ""))
    if age:
        import subprocess as sp
        rd = json.loads(sp.run([sys.executable, os.path.join(HERE, "readability.py"), os.path.join(folder, "manuscript.md")],
                               capture_output=True, text=True).stdout or "{}")
        grade = rd.get("grade")
        lo, hi = (2, 4) if age.startswith("6") else (1, 3)
        add(f"readability for ages {age} (grade {lo} to {hi})", grade is not None and lo <= grade <= hi,
            f"grade {grade}")
    add("language en-US", m.get("language") == "en-US", str(m.get("language")))
    add("AI disclosure exact wording", m.get("ai_disclosure", "").strip() == AI_LINE)
    add("copyright line in manuscript", "Copyright © 2026 Skybee. All rights reserved." in manuscript)
    add("AI disclosure in manuscript", AI_LINE in manuscript)
    add("no placeholder text", not PLACEHOLDER.search(manuscript), (PLACEHOLDER.search(manuscript) or [""])[0] if PLACEHOLDER.search(manuscript) else "ok")

    topic = topic_for(folder)
    if topic is None:
        add("topic entry found in log", False, "no topic with this title in topics-log.json")
    else:
        lo, hi = words_in_range(str(topic.get("word_count", "")))
        if lo:
            add("word count within 10% of target", lo * 0.9 <= body_words <= hi * 1.1,
                f"{body_words} words; target {lo}-{hi}")
        else:
            add("word count within 10% of target", False, "topic has no word_count")

    # Guide section 4 and 9: US English and US dollars everywhere the reader sees text.
    lang = subprocess.run([sys.executable, os.path.join(HERE, "check_language.py"), folder], capture_output=True, text=True)
    lang_json = json.loads(lang.stdout) if lang.stdout.strip() else {"pass": False, "issues": [], "count": 0}
    first = " ".join(manuscript.split("\n")[:12]).lower()
    lang_detail = "; ".join(f"{i['where']} line {i['line']}: '{i['found']}' should be '{i['use']}'" for i in lang_json.get("issues", [])[:6]) or "ok"
    add("US English and US dollars", lang_json.get("pass", False), f"{lang_json.get('count', 0)} issue(s): {lang_detail}")

    # Guide section 8: the manuscript opens with a title page (title, subtitle, author).
    add("title page at the top of manuscript.md",
        norm(m.get("title", "")) in norm(first) and "skybee" in first,
        "title and author in the first 12 lines" if norm(m.get("title", "")) in norm(first) else "title page missing")

    # Guide section 3: a workbook has an answer block after its prompts (at least 10 blocks).
    if topic and "workbook" in str(topic.get("format", "")).lower():
        blocks = manuscript.count("**Your answer:**")
        add("workbook has answer blocks (guide section 3)", blocks >= 10, f"{blocks} answer blocks")

    chapters = len(re.findall(r"^#{1,2}\s", manuscript, re.M))
    add("chapters have headings", chapters >= 1, f"{chapters} headings")

    epub = os.path.join(folder, epubs[0]) if epubs else ""
    jar = find_jar()
    if not jar:
        add("epubcheck runs", False, "epubcheck jar not found; run: pip install --break-system-packages epubcheck")
    else:
        r = subprocess.run(["java", "-jar", jar, epub, "--quiet"], capture_output=True, text=True)
        out = (r.stdout + r.stderr)
        errors = len(re.findall(r"\bERROR\b", out))
        warnings = len(re.findall(r"\bWARNING\b", out))
        add("epubcheck: 0 errors, 0 warnings", errors == 0 and warnings == 0, f"{errors} errors, {warnings} warnings")

    brief = subprocess.run([sys.executable, os.path.join(HERE, "check_cover_brief.py"), folder], capture_output=True, text=True)
    brief_json = json.loads(brief.stdout) if brief.stdout.strip() else {"checks": [{"check": "cover brief", "pass": False, "detail": brief.stderr.strip()}]}
    for c in brief_json["checks"]:
        add("cover brief: " + c["check"], c["pass"], c["detail"])

    if not has_cover:
        cov_json = {"checks": []}
    else:
        cov = subprocess.run([sys.executable, os.path.join(HERE, "check_cover.py"), os.path.join(folder, "cover-ebook.jpg"),
                              "--book", folder], capture_output=True, text=True)
        cov_json = json.loads(cov.stdout)
    for c in cov_json["checks"]:
        add("cover: " + c["check"], c["pass"], c["detail"])

    ok = all(c["pass"] for c in checks)
    print(json.dumps({"folder": folder, "pass": ok, "checks": checks}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
