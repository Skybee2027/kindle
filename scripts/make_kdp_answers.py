#!/usr/bin/env python3
"""Write KDP-FORM-ANSWERS.md for one book, from its metadata.json.

Usage: python3 scripts/make_kdp_answers.py "<book folder>"
Writes the file into the book folder. Run it again after any metadata change.
The answers are copied from metadata.json, so the form and the files always match.
"""
import json
import os
import sys


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    folder = sys.argv[1]
    with open(os.path.join(folder, "metadata.json"), encoding="utf-8") as f:
        m = json.load(f)

    desc = m.get("description", "")
    desc_words = len(desc.split())
    kw = m.get("keywords", [])
    series = m.get("series", "")
    series_line = f"{series}, Book {m.get('series_number')}" if series else "Not part of a series"
    lines = [
        "# KDP form answers",
        "",
        "Copy each answer into the matching field in KDP. Nothing here is uploaded automatically.",
        "",
        "## Details",
        f"- **Language:** {m.get('language', 'en-US')}",
        f"- **Book title:** {m.get('title', '')}",
        f"- **Subtitle:** {m.get('subtitle', '')}",
        f"- **Series:** {series_line}",
        f"- **Author:** {m.get('author', 'Skybee')}",
        "- **Contributors:** none",
        "- **Publishing rights:** I hold the rights to publish this book",
        "",
        "## Description (paste as is)",
        desc,
        "",
        f"_Description length: {desc_words} words (KDP allows up to 4,000 characters)._",
        "",
        "## Keywords (7 boxes, one per box)",
    ]
    lines += [f"{i}. {k}" for i, k in enumerate(kw, 1)]
    lines += [
        "",
        "## Categories",
    ]
    cats = m.get("kdp_categories") or ([m["kdp_category"]] if m.get("kdp_category") else [])
    lines += [f"- {c}" for c in cats] or ["- NO CATEGORY SET: add two in metadata.json (kdp_categories)"]
    lines += [
        "- Check each path in the KDP category picker. KDP needs two.",
        "",
        "## Content",
        f"- **Content warnings:** {m.get('content_warnings', 'None')}",
        f"- **AI-generated content:** {m.get('ai_disclosure', '')}",
        "- **Public domain:** No",
        "",
        "## Pricing and rights",
        f"- **Territories:** Worldwide",
        f"- **Price (USD):** {m.get('price_usd', '')}",
        f"- **Royalty:** {m.get('royalty_tier', '')}",
        f"- **KDP Select (enrol):** {m.get('kdp_select') or 'MISSING: set kdp_select in metadata.json (guide section 9)'}",
        "- **Lending:** Enabled",
        "",
        "## Files to upload",
        f"- **Manuscript:** {m.get('files', {}).get('epub', '')}",
        f"- **Cover:** {m.get('cover', 'cover-ebook.jpg')}",
        "",
        "## Before you press Publish",
        "- Check the cover, title, and author on the KDP preview.",
        "- Use the Kindle Previewer on the EPUB, and read the first and last pages.",
        "- Tell me when it is live, and I will record it.",
        "",
    ]
    out = os.path.join(folder, "KDP-FORM-ANSWERS.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
