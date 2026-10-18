#!/usr/bin/env python3
"""Validate a book's cover brief before any cover is designed.

Usage: python3 scripts/check_cover_brief.py "ebooks-Final/<folder>"
Reads <folder>/cover-brief.json and <folder>/metadata.json. Every check must pass.
Checks: all fields present and filled (no brackets or placeholders); title lines
join to the metadata title; author matches; palette is 3 or 4 hex colours; the
brief is not a copy of another book's brief (same category and palette), so each
cover stays different. Prints JSON. Exit 0 = pass, 1 = fail.
"""
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["title_lines", "subtitle", "author", "series_line", "tagline", "badge",
            "genre", "age_or_reader", "style", "palette", "focal_scene", "character",
            "supporting_details", "canva_link_or_none"]
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
PLACEHOLDER = re.compile(r"\[|\]|TODO|TBD|placeholder|lorem", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = os.path.abspath(sys.argv[1])
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    brief_path = os.path.join(folder, "cover-brief.json")
    meta_path = os.path.join(folder, "metadata.json")
    if not os.path.exists(brief_path):
        add("cover brief present", False, "cover-brief.json missing; write it before designing the cover")
        print(json.dumps({"folder": folder, "pass": False, "checks": checks}, indent=2))
        return 1
    brief = load(brief_path)
    meta = load(meta_path)

    missing = [k for k in REQUIRED if k not in brief or brief[k] in ("", [], None)]
    add("brief fields filled", not missing, "missing: " + ", ".join(missing) if missing else "all present")
    def flat(v):
        return " ".join(flat(x) for x in v) if isinstance(v, list) else str(v)

    text_fields = " ".join(flat(v) for v in brief.values())
    add("no placeholders in brief", not PLACEHOLDER.search(text_fields), "")

    title_lines = brief.get("title_lines", [])
    add("title lines are 2 or 3", 2 <= len(title_lines) <= 3, f"{len(title_lines)} lines")
    add("title lines match metadata title",
        norm(" ".join(title_lines)) == norm(meta.get("title", "")),
        f"brief: {' / '.join(title_lines)} | metadata: {meta.get('title', '')}")
    add("author matches metadata", norm(brief.get("author", "")) == norm(meta.get("author", "")),
        f"brief: {brief.get('author')} | metadata: {meta.get('author')}")
    add("subtitle matches metadata", norm(brief.get("subtitle", "")) == norm(meta.get("subtitle", "")),
        f"brief: {brief.get('subtitle')} | metadata: {meta.get('subtitle')}")

    palette = brief.get("palette", [])
    add("palette has 3 or 4 hex colours", isinstance(palette, list) and 3 <= len(palette) <= 4 and all(HEX.match(c) for c in palette),
        ", ".join(palette) if isinstance(palette, list) else "not a list")

    # Each book needs its own look: same category and same palette as another book is refused.
    mine = (norm(brief.get("genre", "")), sorted(c.upper() for c in palette if isinstance(c, str)))
    clash = None
    for other_path in glob.glob(os.path.join(REPO, "ebooks-Final", "*", "cover-brief.json")):
        if os.path.abspath(os.path.dirname(other_path)) == folder:
            continue
        o = load(other_path)
        theirs = (norm(o.get("genre", "")), sorted(c.upper() for c in o.get("palette", []) if isinstance(c, str)))
        if theirs[0] == mine[0] and theirs[1] == mine[1]:
            clash = os.path.basename(os.path.dirname(other_path))
    add("not a copy of another book's brief", clash is None,
        "same genre and palette as " + clash if clash else "unique")

    ok = all(c["pass"] for c in checks)
    print(json.dumps({"folder": folder, "pass": ok, "checks": checks}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
