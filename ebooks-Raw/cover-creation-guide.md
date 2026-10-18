# Cover creation guide (for robo 3.5)

Purpose: make one ebook cover for each book folder in ebooks-Final, prove it meets the cover rules, map it to the EPUB, and hand it to Kindle-4. This guide never publishes, uploads, commits, or pushes. The owner approves each cover before it is committed.

## 0. Principles (read these first)
1. A cover is sold at thumbnail size, about 160 by 256 pixels. If the title and the focal object are not clear at that size, the cover has failed, however beautiful it is at full size.
2. The cover must promise the book. A cozy mystery must look like a cozy mystery to a reader who scrolls past in one second. Genre signals matter more than originality.
3. One focal idea per cover. Pick one object or person and let it carry the story. Crowds and clutter read as noise.
4. Every cover must be distinguishable from every other cover in the register (ebooks-Raw/cover-prompts.md). Change the palette or the scene before you change anything else.
5. Never claim a check passed unless you ran it. Record what you did not run.

## 1. Read the inputs
- ebooks-Final/<folder>/metadata.json: title, subtitle, author, series, kdp_categories (use the first).
- ebooks-Final/<folder>/manuscript.md: the first 300 words, one middle chapter, and the final chapter. Note the setting, the object or motif that recurs, the character who matters most, and the tone (funny, tense, tender).
- ebooks-Raw/cover-styles.json: the profile for the first category. Its hue ranges, badge rule, tone words, avoid list, and imagery are binding.
- ebooks-Raw/cover-prompts.md: the house Canva prompt template, the rules, and the Cover register.

Write down, in one sentence, what the book is about and what its best visual clue is. For Shorthand for Murder that is: a court reporter whose steno tape proves a murder was covered up, with a lighthouse and a lake town. Clue: the steno tape. Mood: moody, warm, quiet.

## 2. Production path: Canva only
- Every cover is created in Canva, using the create-design tool with a prompt built from the template in cover-prompts.md. There is no Pillow, SVG, HTML, or other drawn fallback.
- If Canva cannot complete a design after three attempts, stop and report the blocker in the handoff. Do not draw a substitute.
- Export the Canva design as PNG (export-design), convert it to a 1600 by 2560 RGB JPEG, and save it as cover-ebook.jpg in the book folder.
- Read the design back after it completes. Canva AI sometimes drops title lines; fix the design in Canva if a line is missing.
- Use only Canva fonts and Canva elements, which avoids separate font licence questions.

## 3. Build the concept (three before one)
Sketch three different concepts before you commit to one. Each concept names: the focal object, the palette (three or four hex colours), the composition (where the title sits, where the focal object sits), and the one detail that signals the genre. Score each out of five on:
- Thumbnail clarity: can the title and the focal object be read at 160 by 256?
- Genre signal: would a fan of this category recognise it in one second?
- Story fit: does the clue or mood come from the manuscript, not from a generic template?
- Register distance: how different is it from the nearest cover in the register?
- Compliance: fits the hue ranges and the badge rule.
Keep the highest total. If two concepts tie, keep the one with the stronger thumbnail score.

## 4. Genre reasoning (apply the profile, then the book)
- Cozy and women sleuths: one warm light source, a clue or prop, a quiet town, a woman in a cardigan or seen from behind. Avoid bright cartoon colours, gore, and romance poses.
- Cozy mystery: a village or harbor at dusk, an object of the crime or the detective's tool, a warm window. Avoid blood, weapons in hand, and skulls.
- Romance: two people or a clear couple gesture, warm light, a place. Avoid violence.
- Children's books: one character, simple shapes, large type, the age badge visible.
- Non-fiction and how-to: a clean object or result shot, a sans-serif title, one strong colour block. No medical, financial, or legal promises on the cover.

## 5. Typography rules
- Author name "Skybee": small, clean sans or serif, bottom of the cover, clearly smaller than the subtitle and the series line. It is credit text, not a headline.
- Title: two or three lines, exactly as metadata.title splits them. Largest element on the cover. Letter height at least 3.5 percent of the cover height (the checker enforces this).
- Title font: a bold serif for mysteries and literary books, a rounded bold sans for children's books, a clean sans for how-to books. Use only fonts licensed for this use (Canva fonts or a font with a saved licence file).
- Subtitle: smaller, one line, in the accent colour.
- Author name: bottom, readable, never smaller than the subtitle.
- Series line and tagline: short. A tagline is under 8 words.
- Keep every text element at least 120 pixels from the edges and at least 80 pixels from other text.

## 6. Colour rules
- Use three or four colours: one dark ground, one accent, one light text colour, and optionally one secondary.
- Check contrast: light text on the dark ground must be clearly legible at thumbnail size.
- Each palette colour should fall inside the profile's hue ranges, or be near-neutral (low saturation). Two colours must be on-style (the checker needs two).
- Avoid a palette used by another book's brief (the checker refuses an exact genre and palette clash).

## 7. Smart prompt writing (for Path A)
Build the prompt from slots, then check it:
- Slot: category and audience line.
- Slot: exact title lines (copy from metadata, do not reword).
- Slot: series line and tagline.
- Slot: bottom badge (from the profile's badge rule) and author name.
- Slot: style words (three to five), taken from the profile's tone.
- Slot: one focal scene (two or three sentences) drawn from the manuscript clue.
- Slot: one character or "none", with a description of pose and clothing, never a real person or a known fictional character.
- Slot: two or three supporting details.
- Slot: palette, by name and hex.
- Slot: typography hints (weight, outline, shadow).
- Closing line: original artwork, no existing characters, brands, or real people, and keep the top third clear.
Prompt check before sending: the title appears twice with identical wording, every hex code is one you chose, the avoid list is named, and the prompt contains no real person or brand.

## 8. Quality review loop (repeat until it passes or you stop)
1. Read the design back. Confirm the title lines are complete and spelled as metadata.
2. Run the checks (section 9). Note every failure.
3. Look at the cover at full size and at thumbnail size (resize to 160 by 256 and view it). Ask: can I name the book and the genre in one second?
4. If a check fails, change one thing only (palette, title size, or composition) and rerun. Do not rewrite everything.
5. Stop after three revisions. If it still fails, write the blockers in the handoff and do not force a pass.

## 9. Validate (run from the repository root, in this order)
1. python3 scripts/check_cover_brief.py "ebooks-Final/<folder>"  (must pass)
2. python3 scripts/check_cover.py "ebooks-Final/<folder>/cover-ebook.jpg" --book "ebooks-Final/<folder>"  (must pass)
3. Visual review by you: author name, badge if any, series line, and tagline are legible. OCR may miss small text; say so.
4. Register check: the new cover must not match any row in the Cover register in cover-prompts.md on category, palette, character, and scene. Add the new row after approval.

## 10. Map the cover to the ebook
- Save cover-ebook.jpg in the same folder as manuscript.md and metadata.json.
- Rebuild: python3 scripts/build_epub.py "ebooks-Final/<folder>". The output must report cover true.
- Run epubcheck via the Java jar from the pip package (python3 -c "import epubcheck,os;print(os.path.join(os.path.dirname(epubcheck.__file__),'epubcheck.jar'))"). Require 0 errors and 0 warnings.
- Do not edit manuscript.md or metadata.json to make a cover fit.

## 11. Handoff to Kindle-4
Write ebooks-Final/<folder>/cover-handoff.md with these sections: book and folder, production path used (A or B), the concept chosen and why (three scores), files produced, check results (pass, fail, or not run, with reasons), visual review notes, EPUB rebuild and epubcheck result, Canva link if any, register row proposed, and open questions for the owner. Kindle-4 cannot be messaged from this run, so the handoff file is the handoff.

Do not commit or push. Do not update review-notes.md to say the cover is done until the owner approves. Report to the owner with the cover path and the handoff path.

## 12. Never do
- Publish, upload to Amazon, or change metadata.json, manuscript.md, or topic records.
- Copy another book's cover or use a known character, brand, logo, or real person.
- Use gore, weapons held toward the viewer, or romance poses on a mystery.
- Claim a check passed that did not run.
- Invent a designer, a licence, or a font you cannot show a licence for.
