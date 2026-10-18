#!/usr/bin/env python3
"""Check a book for near-identical character names and for unsourced research claims.

Usage: python3 scripts/check_names_sources.py "<book folder>"
Reads manuscript.md and metadata.json. Prints JSON. Exit 0 = pass, 1 = fail.

Guide section 4 (distinct names; sourced claims):
  - Names: capitalized words that appear at least twice and are not ordinary words are
    compared. A pair fails when one is the start of the other (Ann and Anna) or when they
    differ by one letter (Hannah and Hanna). A person can then rename one of them, or list an
    approved nickname in metadata.json as "name_aliases": [["Han", "Hannah"]].
  - Sources: when the text makes a research claim (researchers, studies, research shows,
    according to, percent), metadata.json must list at least one source.
Both checks produce candidates for the robot to fix. They do not replace reading the book.
"""
import json
import os
import re
import sys
from collections import Counter

ORDINARY = {
    "The", "This", "That", "These", "Those", "There", "Here", "When", "What", "Where", "Which", "Who",
    "How", "Why", "If", "In", "On", "At", "For", "From", "With", "After", "Before", "Then", "Now",
    "Chapter", "Day", "Days", "Week", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
    "Sunday", "January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December", "Going", "Looking", "Story", "Notes", "Review", "Copyright",
    "Skybee", "Introduction", "Questions", "Readers", "About", "Workbook", "Your", "Answer", "Some",
    "Many", "Most", "Each", "Every", "Other", "Another", "One", "Two", "Three", "Just", "But", "And",
    "You", "They", "She", "He", "It", "We", "I", "My", "Our", "Their", "His", "Her", "Its", "Yes", "No",
    "Also", "Still", "Only", "Even", "Once", "Often", "Never", "Always", "Tea", "Pay", "Work", "Plan",
    "Shape", "Rhythm", "Trial", "Trials", "Friction", "Circle", "Cutter", "Street", "Bakery", "Second",
    "Act", "Book", "Dad", "Mom", "Mrs", "Mr", "Ms", "Gran", "God", "Dear", "Grandma", "Grandpa", "Mum",
}
# Character names are NOT listed here. A name used twice must be checked for look-alikes.
RESEARCH = re.compile(r"\b(researchers?|studies|study|scientists?|research (shows|suggests|has|found)|"
                      r"according to|percent|per cent)\b|%", re.I)


def edit_one(a, b):
    """True if a and b differ by exactly one letter (substitution, insertion or deletion)."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    for i in range(len(long_)):
        if long_[:i] + long_[i + 1:] == short:
            return True
    return False


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = sys.argv[1]
    for name in ["manuscript.md", "metadata.json"]:
        if not os.path.exists(os.path.join(folder, name)):
            print(json.dumps({"folder": folder, "pass": False, "problems": [{"check": "file present", "detail": f"{name} missing"}]}, indent=2))
            return 1
    text = open(os.path.join(folder, "manuscript.md"), encoding="utf-8").read()
    meta = json.load(open(os.path.join(folder, "metadata.json"), encoding="utf-8"))
    problems = []

    # A name is counted where it follows a lowercase word or comma ("told Anna", "with Harriet").
    # Sentence openers and dialogue starts are skipped, because they are ordinary words.
    # Every capitalized word used at least twice, at any position, that is not an ordinary word.
    # Sentence-start words are included; the pair rule below is what decides a clash, so a
    # harmless word only matters if it looks like another name.
    counts = Counter(w for w in re.findall(r"\b([A-Z][a-z]{2,})\b", text) if w not in ORDINARY)
    names = sorted(w for w, n in counts.items() if n >= 2)
    pairs = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if (len(a) >= 3 and b.startswith(a)) or (len(b) >= 3 and a.startswith(b)) or edit_one(a.lower(), b.lower()):
                pairs.append([a, b])
    # Approved nicknames are listed in metadata.json as "name_aliases": [["Han", "Hannah"], ...].
    aliases = {frozenset(x) for x in meta.get("name_aliases", []) if len(x) == 2}
    for a, b in pairs:
        if frozenset([a, b]) in aliases:
            continue
        problems.append({"check": "distinct names", "detail": f"'{a}' and '{b}' look alike; rename one character throughout the book"})

    if RESEARCH.search(text) and not meta.get("sources"):
        problems.append({"check": "research claims have sources", "detail": "the text makes a research claim, but metadata.json sources is empty"})

    result = {"folder": folder, "pass": not problems, "problems": problems, "names_checked": names}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
