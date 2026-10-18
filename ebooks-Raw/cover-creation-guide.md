# Cover and ebook creation guide (for robo 3.5 and the Kindle team)

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

---

# Part B: Ebook creation prompts

Use these prompts for the book itself, alongside Part A (covers above). The cover has its own steps in Part A.

## B0. Reality checks (read first)
- An EPUB is reflowable. It has no fixed page numbers. The reader's device sets page breaks, so the table of contents links to chapters, not page numbers. Page numbers belong only in a print PDF. Do not promise page numbers in the ebook.
- Kindle and most e-readers ignore many colours and fancy fonts. Use bold, italic, and small caps for emphasis. Use colour only in the cover. Keep body text black on white, or on the reader's own background.
- Use embedded fonts only when licensed (EB Garamond, OFL, is saved in fonts/). Keep the font list short: one body font, one heading font.
- The guide's rules still apply: 25 to 40 chapters for cozy mysteries, 55,000 to 60,000 words, US English, fiction disclaimer, AI disclosure, title in the first 12 lines.

---

## Prompt 0: master brief (paste at the start of any ebook job)

> You are a professional ebook producer for the Skybee KDP pipeline. Your job is to turn an approved topic into a finished, compliant EPUB that a reader will finish.
> Inputs: the topic entry in ebook-topics/topics-log.json, the house guide (ebooks-Raw/guide.docx, version 2.1), and ebooks-Raw/ebook-prompts.md (this file).
> Standards: US English, US dollars, no placeholder text, no bracketed notes in the manuscript, no invented facts, sourced research claims only, and the required disclaimer and AI disclosure.
> Reader goal: each chapter must end with a reason to read the next one. Every section must earn its place.
> Output in order: the outline, the manuscript, the metadata, the stylesheet, the EPUB, the checks, the handoff note. Do not skip a stage. Do not publish, upload, or commit without owner approval.

---

## Prompt 1: planning (before writing a word)

> From the topic entry, write a one-page plan with these headings:
> 1. Promise: one sentence on what the reader will feel and get.
> 2. Reader: who buys it, what they expect (for example, cozy mystery readers want a clean puzzle, a likeable sleuth, and a satisfying ending).
> 3. Structure: the number of chapters (25 to 40), words per chapter (aim for 1,800 to 2,400 for a novel), and the page-turn hook for each.
> 4. Arc: setup, rising clues, midpoint twist, dark moment, reveal, resolution, and a hook for the next book.
> 5. Cast: names and roles, checked so no two names look alike (no Ann and Anna, no Dale and Dana).
> 6. Setting and sensory anchors: three details per location that the reader will remember.
> 7. Running motifs: one object or sound that returns and pays off.
> Check: the chapter count is within 25 to 40; the word target matches the topic entry; every outline beat maps to at least two chapters.

---

## Prompt 2: manuscript structure (sequence)

> Lay out the book in this exact sequence. Do not reorder.
> 1. Title page (title, subtitle, author "Skybee", series line), within the first 12 lines of manuscript.md.
> 2. Copyright page: "Copyright © 2026 Skybee. All rights reserved." followed by the fiction disclaimer and the AI disclosure, exactly as the guide requires.
> 3. Table of contents: generated by the build (--toc), not typed by hand. Do not add page numbers.
> 4. Chapters: each starts with "## Chapter N: Title" on its own line. Number them 1 to N with no gaps.
> 5. Closing: the AI disclosure as the final line of the manuscript.
> Check: no chapter is missing or duplicated; chapter headings are numbered in order; the copyright and disclosure lines are present; no placeholder text remains.

---

## Prompt 3: chapter writing (engagement)

> Write chapter N. Open with a concrete image, a line of dialogue, or a question the reader wants answered. No summary openings ("It had been a long day").
> Keep each scene in one point of view. Show one clue, one emotional beat, and one turn.
> Vary sentence length. Use a short sentence after a long one to land a beat.
> Use dialogue tags sparingly: "said" is nearly invisible; use action beats instead of adverbs.
> End the chapter on a question, a reveal, or a line that makes the reader turn the page. Do not end two chapters in a row with the same device.
> Check: the chapter has a clear turn; no paragraph runs longer than about 150 words; the POV does not switch without a break.

---

## Prompt 4: paragraph and line formatting

> Format every paragraph as plain text with one blank line between paragraphs. Do not use hard line breaks inside a paragraph.
> Use straight quotation marks consistently, or curly quotes consistently, one style across the book (match the existing manuscript).
> Italics for thoughts, documents, and titles of works, marked with single asterisks. Bold only for a chapter-level warning or a character's shouted word, sparingly.
> Scene breaks: a centred "* * *" line, not a blank line alone, so the break survives the EPUB.
> Dialogue: each new speaker starts a new paragraph.
> Avoid em-dash overuse; one dash per paragraph is a good ceiling.
> Check: no line is wider than a phone screen when converted; no stray asterisks, brackets, or markdown errors remain; scene breaks are consistent.

---

## Prompt 5: title, headings, and alignment (stylesheet)

> Write or confirm style.css so that:
> - Body text is justified, with a first-line indent of about 1.5em, except the first paragraph after a heading (no indent).
> - Chapter headings are centred, large, and given space above (page break before each chapter).
> - The title page is centred, with the title as the largest text, the subtitle smaller and in italics, and the author last.
> - Margins are small and even (about 5 percent). No fixed pixel widths. No text in images except the cover.
> - Fonts: embedded EB Garamond, with a serif fallback (Georgia, serif). Body size 1em, line height about 1.5.
> - Colour: black text on white only. Do not rely on colour to carry meaning.
> Check: run epubcheck; check the stylesheet loads (no RSC-007 errors); the first paragraph after each heading is not indented.

---

## Prompt 6: emphasis and visual interest (within ebook limits)

> Add interest with structure, not decoration:
> - A short epigraph or one-line quote under the title page, if the topic supports it, with a credit line.
> - Chapter titles that promise a clue or a feeling ("The Silver Link" over "Chapter 20").
> - A bold character name at the top of a document excerpt, once, for clarity.
> - Italic sound cues or document text, used consistently.
> - A closing "Reader's note" only if the guide allows it. Do not add promotional links the guide does not permit.
> Check: every emphasis style is used consistently; no decorative fonts; the emphasis aids reading.

---

## Prompt 7: engagement and retention

> For every chapter, answer in one sentence each: What does the reader learn? What do they fear or want now? What question is open? Make sure the open question changes at least once per chapter.
> Build three reading tensions into the book: a question answered at the midpoint, a false lead that seems true for two chapters, and a final reveal that the earlier clues already support.
> Keep the cast memorable: give each major character one habit or phrase that identifies them on the page.
> Check: no chapter lacks a question; the reveal is fair (every clue is shown earlier); no character speaks in a way that makes them indistinguishable from another.

---

## Prompt 8: metadata and front matter

> Complete metadata.json: title, subtitle, author "Skybee", language "en-US", guide_version "2.1", series and series_number, a description of 150 to 400 words that sells the book without spoilers, exactly seven keywords each under 50 characters, two KDP categories confirmed in the category pool, kdp_select "enroll for 90 days" for series books, and the exact AI disclosure.
> Run make_kdp_answers.py so KDP-FORM-ANSWERS.md matches metadata.json.
> Check: check_book.py metadata checks pass.

---

## Prompt 9: the build and the proof

> Run, in order:
> 1. python3 scripts/build_epub.py "ebooks-Final/<folder>"  (the output must report cover true when a cover exists)
> 2. Run epubcheck with the Java jar from the pip package. Require 0 errors and 0 warnings.
> 3. python3 scripts/check_book.py "ebooks-Final/<folder>". Only cover checks may fail, and only before the cover is approved.
> 4. Read the first chapter and the final chapter in the built EPUB (unzip and read the XHTML). Confirm the title page, copyright, table of contents, and chapter order.
> 5. Record every result in review-notes.md. Do not claim a check passed that did not run.

---

## Prompt 10: handoff

> Write review-notes.md with: the structure (chapter count and beat mapping), word count, checks run and their results, checks not run and why, continuity fixes, open questions for the owner, and the cover status. Then stop. Do not commit or publish without owner approval.

---

## Quick checklist (paste into any job)

- [ ] Title page in the first 12 lines; title, subtitle, author correct
- [ ] Copyright and fiction disclaimer present; AI disclosure present and last
- [ ] Table of contents generated by the build; no page numbers in the EPUB
- [ ] Chapters numbered in order with no gaps; each chapter has a turn and a hook
- [ ] Paragraphs clean; scene breaks consistent; no stray markup
- [ ] Headings centred; body justified; first paragraphs unindented
- [ ] One body font and one heading font, embedded and licensed
- [ ] Emphasis (bold, italic) used consistently; colour only on the cover
- [ ] Names distinct; facts checked; research claims sourced
- [ ] epubcheck 0 errors, 0 warnings; check_book.py passes apart from cover items awaiting approval
- [ ] review-notes.md written with every check recorded honestly
