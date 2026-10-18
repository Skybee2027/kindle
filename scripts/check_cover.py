#!/usr/bin/env python3
"""Check a cover against the guide and against earlier covers.

Usage: python3 scripts/check_cover.py <cover.jpg> [compare-folder ...]
Checks: 1600 x 2560 pixels, RGB JPEG. Compares a perceptual hash with every other
cover-ebook.jpg in the compare folders (default: ebooks-Final); a near-match fails.
Prints JSON. Exit 0 = pass, 1 = fail.
"""
import glob
import json
import os
import sys

from PIL import Image

MAX_HAMMING = 10  # out of 64 bits; below this the covers look alike


def ahash(img):
    g = img.convert("L").resize((8, 8), Image.LANCZOS)
    px = list(g.getdata())
    avg = sum(px) / len(px)
    bits = 0
    for p in px:
        bits = (bits << 1) | (1 if p >= avg else 0)
    return bits


def hamming(a, b):
    return bin(a ^ b).count("1")


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cover = sys.argv[1]
    compare = sys.argv[2:] or ["ebooks-Final"]
    checks = []
    img = Image.open(cover)
    checks.append({"check": "size 1600x2560", "pass": img.size == (1600, 2560), "detail": f"{img.size[0]}x{img.size[1]}"})
    checks.append({"check": "RGB JPEG", "pass": img.format == "JPEG" and img.mode == "RGB", "detail": f"{img.format} {img.mode}"})

    mine = ahash(img)
    closest = None
    for folder in compare:
        for other in glob.glob(os.path.join(folder, "*", "cover-ebook.jpg")):
            if os.path.abspath(other) == os.path.abspath(cover):
                continue
            d = hamming(mine, ahash(Image.open(other)))
            if closest is None or d < closest[0]:
                closest = (d, other)
    if closest is None:
        checks.append({"check": "different from earlier covers", "pass": True, "detail": "no earlier covers"})
    else:
        checks.append({"check": "different from earlier covers", "pass": closest[0] > MAX_HAMMING,
                       "detail": f"closest {closest[1]} distance {closest[0]} (needs more than {MAX_HAMMING})"})
    ok = all(c["pass"] for c in checks)
    print(json.dumps({"file": cover, "pass": ok, "checks": checks}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
