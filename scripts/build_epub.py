#!/usr/bin/env python3
"""Build the EPUB for a book folder, the same way every time.

Usage: python3 scripts/build_epub.py "ebooks-Final/<folder>"
Needs: manuscript.md, metadata.json, style.css, fonts/ (*.woff2), and cover-ebook.jpg
(cover optional at this stage; Kindle-3 adds it before the final build).
Output: <title-slug>.epub in the folder. Any other .epub in the folder is removed first,
so a folder never holds two EPUBs. Exit 0 = built, 1 = failed, 2 = usage.
"""
import glob
import json
import os
import re
import subprocess
import sys


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = os.path.abspath(sys.argv[1])
    for name in ["manuscript.md", "metadata.json", "style.css"]:
        if not os.path.exists(os.path.join(folder, name)):
            print(f"missing {name}", file=sys.stderr)
            return 1
    with open(os.path.join(folder, "metadata.json"), encoding="utf-8") as f:
        meta = json.load(f)
    out_name = slug(meta["title"]) + ".epub"

    cmd = ["pandoc", "manuscript.md", "-o", out_name, "--css", "style.css",
           "--toc", "--toc-depth=2",
           "--metadata", f"title={meta['title']}",
           "--metadata", f"subtitle={meta.get('subtitle', '')}",
           "--metadata", f"author={meta.get('author', 'Skybee')}",
           "--metadata", f"lang={meta.get('language', 'en-US')}"]
    fonts = sorted(glob.glob(os.path.join(folder, "fonts", "*.woff2")))
    for font in fonts:
        cmd += ["--epub-embed-font", os.path.relpath(font, folder)]
    cover = os.path.join(folder, "cover-ebook.jpg")
    if os.path.exists(cover):
        cmd += ["--epub-cover-image", "cover-ebook.jpg"]

    # Build first, then remove other EPUBs, so a failed build never leaves a folder with no EPUB.
    r = subprocess.run(cmd, cwd=folder, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        return 1
    for old in glob.glob(os.path.join(folder, "*.epub")):
        if os.path.basename(old) != out_name:
            os.remove(old)
    print(json.dumps({"built": os.path.join(folder, out_name), "fonts_embedded": len(fonts), "cover": os.path.exists(cover)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
