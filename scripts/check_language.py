#!/usr/bin/env python3
"""Check a book's words and currency against the guide's US English and USD rules.

Usage: python3 scripts/check_language.py "<book folder>"
Reads manuscript.md, metadata.json (title, subtitle, description, keywords, series) and,
if present, cover-brief.json (every text value). Prints JSON. Exit 0 = pass, 1 = fail.

Guide sections 4 and 9: all text is US English and every price is in US dollars.
The word list below is the list of British forms found in review, plus common others.
Add a word here when a new one is found, and record the change in guide section 19.
"""
import json
import os
import re
import sys

BRITISH = {
    # -ise / -our / -re / -ogue family
    "organised": "organized", "organising": "organizing", "organise": "organize",
    "recognise": "recognize", "recognised": "recognized", "realise": "realize", "realised": "realized",
    "apologise": "apologize", "apologising": "apologizing", "reorganised": "reorganized",
    "unpractised": "unpracticed", "practise": "practice", "practised": "practiced", "practising": "practicing",
    "neighbour": "neighbor", "neighbours": "neighbors", "neighbourhood": "neighborhood",
    "colour": "color", "colours": "colors", "honour": "honor", "behaviour": "behavior",
    "favourite": "favorite", "centre": "center", "sceptical": "skeptical", "programme": "program",
    "programmes": "programs", "travelled": "traveled", "judgement": "judgment",
    # people and jobs
    "counsellor": "counselor", "counsellors": "counselors", "adviser": "advisor", "advisers": "advisors",
    "solicitor": "attorney", "solicitors": "attorneys",
    # time and money
    "fortnight": "two weeks", "fortnights": "two weeks", "quid": "dollars", "GBP": "USD",
    # everyday words
    "biscuit": "cookie", "biscuits": "cookies", "takeaway": "takeout", "takeaways": "takeouts",
    "loft": "attic", "fete": "fair", "lorry": "truck", "petrol": "gas",
    "queue": "line", "queues": "lines", "licence": "license", "cheque": "check", "tyre": "tire",
    "learnt": "learned", "whilst": "while", "amongst": "among", "mum": "mom",
}
# Words that are also normal US words or names when capitalised: match lowercase only.
LOWER_ONLY = {"biscuit", "biscuits", "loft", "mum", "queue", "queues", "tyre", "cheque"}
# Plain currency words for pounds sterling. Weight use ("a pound of flour") is allowed.
WEIGHT_WORDS = r"(?:of|bag|bags|flour|sugar|butter|cake|dog|cat|weight|weigh|weighed|heavier|lighter|lost|gained|gain|loss|loose|sack|box|bar|stone|cheese|meat|apples)"
STERLING = re.compile(r"\bpounds? sterling\b|\bpounds? \d", re.I)   # always fails
BARE_POUNDS = re.compile(r"\b\d[\d,]*\s?pounds?\b(?!\s+" + WEIGHT_WORDS + r"\b)", re.I)  # review only: may be weight
CURRENCY = re.compile(r"£|€")


def strip_markdown(text):
    text = re.sub(r"\\_", " ", text)            # fill-in lines are not words
    return text


def scan(text, label, issues):
    text = strip_markdown(text)
    for british, us in BRITISH.items():
        flags = 0 if british in LOWER_ONLY else re.I
        for m in re.finditer(r"\b" + re.escape(british) + r"\b", text, flags=flags):
            line = text.count("\n", 0, m.start()) + 1
            issues.append({"where": label, "line": line, "found": m.group(0), "use": us})
    for m in STERLING.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        issues.append({"where": label, "line": line, "found": m.group(0), "use": "$ (US dollars)", "kind": "fail"})
    for m in BARE_POUNDS.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        issues.append({"where": label, "line": line, "found": m.group(0), "use": "check: $ if money, pounds if weight", "kind": "review"})
    for m in CURRENCY.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        issues.append({"where": label, "line": line, "found": m.group(0), "use": "$ (US dollars)"})


def text_values(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, list):
        for x in obj:
            yield from text_values(x)
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from text_values(v)


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = sys.argv[1]
    issues = []
    man = os.path.join(folder, "manuscript.md")
    if os.path.exists(man):
        scan(open(man, encoding="utf-8").read(), "manuscript.md", issues)
    meta_path = os.path.join(folder, "metadata.json")
    if os.path.exists(meta_path):
        meta = json.load(open(meta_path, encoding="utf-8"))
        for key in ["title", "subtitle", "description", "keywords", "series"]:
            for value in text_values(meta.get(key, "")):
                scan(value, f"metadata.json {key}", issues)
    brief_path = os.path.join(folder, "cover-brief.json")
    if os.path.exists(brief_path):
        brief = json.load(open(brief_path, encoding="utf-8"))
        for value in text_values(brief):
            scan(value, "cover-brief.json", issues)
    fails = [i for i in issues if i.get("kind", "fail") == "fail"]
    result = {"folder": folder, "pass": not fails, "issues": issues[:200], "count": len(issues),
              "review": len(issues) - len(fails)}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
