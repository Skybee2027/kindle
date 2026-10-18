#!/usr/bin/env python3
"""Check a cover: file rules, uniqueness, and whether it matches its book.

Usage:
  python3 scripts/check_cover.py <cover.jpg>                 # file rules and uniqueness
  python3 scripts/check_cover.py <cover.jpg> --book <folder>  # also match the brief and metadata

File rules: 1600 x 2560 pixels, RGB JPEG, not blank, not a near-copy of another cover.
With --book (reads <folder>/cover-brief.json and <folder>/metadata.json):
  - palette: at least PALETTE_MIN of the cover's pixels are close to the brief's colours
  - text (read by tesseract, the OCR tool): the title is readable at full size and at
    thumbnail size (160 x 256 pixels, what a shopper sees). Author, badge, series line and
    tagline are checked by OCR when it can read them; otherwise they are listed for Kindle-3
    to confirm by viewing the cover.
  - title size: title letters are at least TITLE_MIN_HEIGHT of the cover height
Prints JSON. Exit 0 = pass, 1 = fail, 2 = usage.
"""
import csv
import difflib
import glob
import io
import json
import os
import re
import subprocess
import sys
import tempfile

from PIL import Image, ImageStat

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_HAMMING = 10          # out of 64 bits; below this two covers look alike
PALETTE_MIN = 0.20        # share of pixels that must be close to the brief's colours
PALETTE_DIST = 70         # RGB distance that counts as "close"
TITLE_MIN_HEIGHT = 0.035  # title letter height as a share of the cover height
WORD_MATCH = 0.75         # fuzzy match ratio for OCR words
TITLE_WORDS_FULL = 0.85
TITLE_WORDS_THUMB = 0.50
TEXT_WORD_FULL = 0.75


def ahash(img):
    g = img.convert("L").resize((8, 8), Image.LANCZOS)
    px = list(g.get_flattened_data() if hasattr(g, "get_flattened_data") else g.getdata())
    avg = sum(px) / len(px)
    bits = 0
    for p in px:
        bits = (bits << 1) | (1 if p >= avg else 0)
    return bits


def hamming(a, b):
    return bin(a ^ b).count("1")


def norm_words(s):
    return re.findall(r"[a-z0-9]+", s.lower())


def ocr_words(path):
    """Return [(text, height_px)] from tesseract, or None if tesseract is missing."""
    try:
        out = subprocess.run(["tesseract", path, "stdout", "tsv"], capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        return []  # OCR too slow: treat as nothing read, so the text checks fail visibly
    rows = csv.DictReader(io.StringIO(out.stdout), delimiter="\t", quoting=csv.QUOTE_NONE)
    words = []
    for r in rows:
        t = (r.get("text") or "").strip()
        if t and r.get("level") == "5":
            words.append((t, int(r.get("height") or 0)))
    return words


def found(target_words, ocr):
    """Share of target words found in OCR output (fuzzy)."""
    if not target_words:
        return 1.0
    ocr_tokens = [w for t, _ in ocr for w in norm_words(t)]
    hits = 0
    for tw in target_words:
        if any(difflib.SequenceMatcher(None, tw, ow).ratio() >= WORD_MATCH for ow in ocr_tokens):
            hits += 1
    return hits / len(target_words)


def hex_to_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def palette_share(img, palette_hex):
    small = img.convert("RGB").resize((160, 256), Image.LANCZOS)
    cols = [hex_to_rgb(h) for h in palette_hex]
    close = 0
    px = list(small.get_flattened_data() if hasattr(small, "get_flattened_data") else small.getdata())
    for r, g, b in px:
        if min(((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2) ** 0.5 for cr, cg, cb in cols) <= PALETTE_DIST:
            close += 1
    return close / len(px)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__, file=sys.stderr)
        return 2
    cover = args[0]
    book = None
    if "--book" in args:
        i = args.index("--book")
        book = os.path.abspath(args[i + 1])
    checks = []

    def add(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    if not os.path.exists(cover):
        print(json.dumps({"file": cover, "pass": False, "checks": [{"check": "cover file present", "pass": False, "detail": "cover-ebook.jpg not found"}]}, indent=2))
        return 1
    img = Image.open(cover)
    add("size 1600x2560", img.size == (1600, 2560), f"{img.size[0]}x{img.size[1]}")
    add("RGB JPEG", img.format == "JPEG" and img.mode == "RGB", f"{img.format} {img.mode}")
    spread = ImageStat.Stat(img.convert("L")).stddev[0]
    add("not blank", spread > 20, f"contrast spread {spread:.1f}")

    mine = ahash(img)
    closest = None
    for other in glob.glob(os.path.join(REPO, "ebooks-Final", "*", "cover-ebook.jpg")):
        if os.path.abspath(other) == os.path.abspath(cover):
            continue
        d = hamming(mine, ahash(Image.open(other)))
        if closest is None or d < closest[0]:
            closest = (d, other)
    if closest is None:
        add("different from earlier covers", True, "no earlier covers")
    else:
        add("different from earlier covers", closest[0] > MAX_HAMMING,
            f"closest {os.path.relpath(closest[1], REPO)} distance {closest[0]} (needs more than {MAX_HAMMING})")

    if book:
        brief_path = os.path.join(book, "cover-brief.json")
        meta_path = os.path.join(book, "metadata.json")
        if not os.path.exists(brief_path):
            add("cover brief present", False, "cover-brief.json missing")
        else:
            with open(brief_path, encoding="utf-8") as f:
                brief = json.load(f)
            with open(meta_path, encoding="utf-8") as f:
                meta = json.load(f)
            palette = brief.get("palette") or []
            if not palette or not all(re.match(r"^#[0-9A-Fa-f]{6}$", str(c)) for c in palette):
                add("palette matches brief", False, "brief has no valid #RRGGBB palette")
            else:
                share = palette_share(img, palette)
                add("palette matches brief", share >= PALETTE_MIN, f"{share:.0%} of pixels near brief colours (needs {PALETTE_MIN:.0%})")

            ocr = ocr_words(cover)
            if ocr is None:
                add("text readable (tesseract installed)", False, "tesseract not installed; cannot read the cover text")
            else:
                title_words = norm_words(" ".join(brief.get("title_lines", [])))
                share_full = found(title_words, ocr)
                add("title readable at full size", share_full >= TITLE_WORDS_FULL,
                    f"{share_full:.0%} of title words found (needs {TITLE_WORDS_FULL:.0%})")

                title_heights = [h for t, h in ocr if any(w in title_words for w in norm_words(t))]
                tall = sorted(title_heights)[len(title_heights) // 2] if title_heights else 0
                add("title letters large enough", tall >= TITLE_MIN_HEIGHT * 2560,
                    f"median title letter height {tall}px (needs {int(TITLE_MIN_HEIGHT * 2560)}px)")

                # Decorative text OCR often cannot read (author name, badge, series line, tagline).
                # These are not failed by OCR; Kindle-3 must confirm them by viewing the cover.
                visual = []
                for label, key in [("author", "author"), ("age or grade badge", "badge"),
                                   ("series line", "series_line"), ("tagline", "tagline")]:
                    value = brief.get(key, "")
                    if not value or value.lower().startswith("none"):
                        continue
                    share = found(norm_words(value), ocr)
                    if share >= TEXT_WORD_FULL:
                        add(f"{label} readable", True, f"'{value}' found by OCR")
                    else:
                        visual.append(f"{label}: '{value}'")
                if visual:
                    notes_path = os.path.join(book, "review-notes.md")
                    notes = open(notes_path, encoding="utf-8").read() if os.path.exists(notes_path) else ""
                    missing = [v for v in visual if v.split(": ", 1)[1].strip("'") not in notes]
                    add("viewed by eye and recorded (OCR could not read)", not missing,
                        ("recorded in review-notes.md: " if not missing else "not yet recorded in review-notes.md: ")
                        + "; ".join(missing or visual))

                # Thumbnail: what a shopper sees in the store, enlarged so OCR can work on it.
                with tempfile.TemporaryDirectory() as tmp:
                    thumb_path = os.path.join(tmp, "thumb.png")
                    img.convert("RGB").resize((160, 256), Image.LANCZOS).resize((480, 768), Image.LANCZOS).save(thumb_path)
                    thumb = ocr_words(thumb_path) or []
                share_thumb = found(title_words, thumb)
                add("title readable at thumbnail size", share_thumb >= TITLE_WORDS_THUMB,
                    f"{share_thumb:.0%} of title words found at 160 x 256 (needs {TITLE_WORDS_THUMB:.0%})")

    ok = all(c["pass"] for c in checks)
    print(json.dumps({"file": cover, "pass": ok, "checks": checks}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
