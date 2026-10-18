#!/usr/bin/env python3
"""Pick the next ebook topic that has never been created.

A topic counts as USED (and is never picked again) if ANY of these is true:
  - its topic name is in ebooks-Final/used-topics.json
  - a folder in ebooks-Final matches its slug (lowercase, spaces to hyphens)
  - its row in ebooks-Raw/topics-list.xlsx has a Status other than "Selected"
    (for example "Used - ..." or "Drafted - ...")

Prints the first candidate that passes, as JSON. Exits 1 if none is left.
Run from the repository root.
"""
import json
import os
import re
import sys

import openpyxl

FINAL = "ebooks-Final"
USED_FILE = os.path.join(FINAL, "used-topics.json")
SHEET = "ebooks-Raw/topics-list.xlsx"
LOG = "ebook-topics/topics-log.json"
POOL = "ebook-topics/category-pool.json"


def norm(text):
    return re.sub(r"\s+", " ", (text or "").strip()).lower()


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", norm(text)).strip("-")


def topic_categories():
    """Map each topic's slug to its categories and to whether every category is confirmed in the pool."""
    pool = {}
    if os.path.exists(POOL):
        with open(POOL, encoding="utf-8") as f:
            pool = {c["category"]: bool(c.get("confirmed")) for c in json.load(f)["categories"]}
    out = {}
    if os.path.exists(LOG):
        with open(LOG, encoding="utf-8") as f:
            for entry in json.load(f):
                topics = ([entry["selected_topic"]] if entry.get("selected_topic") else []) + (entry.get("selected_topics") or [])
                for t in topics:
                    if t and t.get("topic_name"):
                        cats = t.get("categories") or []
                        ok = len(cats) == 2 and all(pool.get(c) for c in cats)
                        out[slug(t["topic_name"])] = (ok, cats)
    return out


def main():
    cats = topic_categories()
    used_names, used_slugs = set(), set()
    if os.path.exists(USED_FILE):
        with open(USED_FILE, encoding="utf-8") as f:
            for entry in json.load(f):
                used_names.add(norm(entry.get("topic")))
                used_slugs.add(entry.get("folder", ""))
    if os.path.isdir(FINAL):
        for name in os.listdir(FINAL):
            if os.path.isdir(os.path.join(FINAL, name)):
                used_slugs.add(name)

    ws = openpyxl.load_workbook(SHEET, read_only=True)["Topics"]
    rows = list(ws.iter_rows(values_only=True))
    header = [str(h) for h in rows[0]]
    status_i, topic_i = header.index("Status"), header.index("Topic")

    for row in rows[1:]:
        topic, status = row[topic_i], str(row[status_i] or "").strip()
        if not topic:
            continue
        reasons = []
        if not status.lower().startswith("selected"):
            reasons.append(f"status is '{status}'")
        if norm(topic) in used_names:
            reasons.append("listed in used-topics.json")
        if any(s and slug(topic).startswith(s) for s in used_slugs):
            reasons.append("folder exists in ebooks-Final")
        match = [v for k, v in cats.items() if slug(topic).startswith(k)]
        if not match:
            reasons.append("no categories in topic log")
        elif not match[0][0]:
            reasons.append("categories not all confirmed by owner in category-pool.json")
        if reasons:
            print(f"skip: {topic[:60]} ({'; '.join(reasons)})", file=sys.stderr)
            continue
        print(json.dumps({"topic": topic, "slug": slug(topic)}, ensure_ascii=False))
        return 0

    print("No unused candidate topic remains. Create nothing.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
