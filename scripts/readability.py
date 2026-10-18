#!/usr/bin/env python3
"""Flesch-Kincaid grade level for a text file (used for kids' books, guide v2.1 section 13).

Usage: python3 scripts/readability.py <manuscript.md>
Prints JSON: grade, words, sentences, syllables. Target for ages 6 to 9: grade 2 to 4.
Method: sentences split on . ! ?; syllables counted by vowel groups (standard approximation).
"""
import json
import re
import sys


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(1, n)


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    text = open(sys.argv[1], encoding="utf-8").read()
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.M)  # drop headings
    text = re.sub(r"[*_`>\[\]()]", " ", text)
    sentences = [s for s in re.split(r"[.!?]+(?:\s|$)", text) if re.search(r"[A-Za-z]", s)]
    words = re.findall(r"[A-Za-z][A-Za-z'’-]*", text)
    if not words or not sentences:
        print(json.dumps({"error": "no text found"}))
        return 1
    syl = sum(syllables(w) for w in words)
    grade = 0.39 * (len(words) / len(sentences)) + 11.8 * (syl / len(words)) - 15.59
    print(json.dumps({"grade": round(grade, 1), "words": len(words),
                      "sentences": len(sentences), "syllables": syl}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
