# Cover creation guide (for robo 3.5)

Purpose: make one ebook cover for each book folder in ebooks-Final, prove it meets the cover rules, map it to the EPUB, and hand it to Kindle-4. This guide never publishes, uploads, commits, or pushes. The owner approves each cover before it is committed.

## 0. Principles (read these first)
1. A cover is sold at thumbnail size, about 160 by 256 pixels. If the title and the focal object are not clear at that size, the cover has failed, however beautiful it is at full size.
2. The cover must promise the book. A cozy mystery must look like a cozy mystery to a reader who scrolls past in one second. Genre signals matter more than originality.
3. One focal idea per cover. Pick one object or person and let it carry the story. Crowds and clutter read as noise.
4. Every cover must be distinguishable from every other cover in the register (Part B of this guide). Change the palette or the scene before you change anything else.
5. Never claim a check passed unless you ran it. Record what you did not run.

## 1. Read the inputs
- ebooks-Final/<folder>/metadata.json: title, subtitle, author, series, kdp_categories (use the first).
- ebooks-Final/<folder>/manuscript.md: the first 300 words, one middle chapter, and the final chapter. Note the setting, the object or motif that recurs, the character who matters most, and the tone (funny, tense, tender).
- ebooks-Raw/cover-styles.json: the profile for the first category. Its hue ranges, badge rule, tone words, avoid list, and imagery are binding.
- Part B of this guide: the house Canva prompt template, the rules, and the Cover register.

Write down, in one sentence, what the book is about and what its best visual clue is. For Shorthand for Murder that is: a court reporter whose steno tape proves a murder was covered up, with a lighthouse and a lake town. Clue: the steno tape. Mood: moody, warm, quiet.

## 2. Production path: Canva only
- Every cover is created in Canva, using the create-design tool with a prompt built from the template in Part B. There is no Pillow, SVG, HTML, or other drawn fallback.
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
4. Register check: the new cover must not match any row in the Cover register in Part B on category, palette, character, and scene. Add the new row after approval.

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

# Part B: Cover prompts and register

Use these prompts with the Canva `create-design` tool. Each book needs its own prompt, and no two covers may share the same category, palette, main character, or scene.

## B1. How to use

1. Look up the book's first category in `ebooks-Raw/cover-styles.json`. Use its reader, look, title style, palette hue ranges, badge rule, imagery, and avoid list for the brief and the design.
2. Write the book's cover brief next: `ebook-folder/cover-brief.json`. Set `genre` and `style_profile` to that exact pool path. Fill every field from metadata.json: the title lines exactly as on the cover, the subtitle, author, series line, tagline, badge (or "none" for adult books), genre, reader age, style, three or four palette colours as hex codes, the focal scene, the character, and supporting details. Check it with `python3 scripts/check_cover_brief.py "ebooks-Final/<folder>"` before any design.
3. Copy the template below and fill it in from the brief. Use the brief's exact title lines and palette names.
4. Check the **Cover register** below. The new book must differ from every cover listed in category, palette, character, and scene.
5. Send the prompt with the format `Portrait book cover 1600 x 2560`.
6. Wait for the job to finish, then read the design back. Confirm the title text is complete (Canva AI has dropped title lines before). If a line is missing, fix it in Canva before exporting.
7. Export as PNG, convert to 1600 x 2560 RGB JPEG as `cover-ebook.jpg`, then run `python3 scripts/check_cover.py "ebooks-Final/<folder>/cover-ebook.jpg" --book "ebooks-Final/<folder>"`. It must pass.
8. View the finished cover yourself. Confirm the author name, badge, series line, and tagline, which OCR may not read. Record the result in review-notes.md.
9. Add the book to the **Cover register**, with its Canva link and hex palette from the brief.

## B2. Template prompt

> [Category] cover for the US market, [age range] (for example, ages 7 to 9). The title must read exactly on [number] lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top in a bold ribbon: "[SERIES NAME] · BOOK [n]". Tagline below the title: "[Short hook, 3 to 6 words]". Bottom badge: "[AGE/GRADE BADGE]". Author name at bottom: "[Author name]". Style: [style words, e.g. vibrant, high-contrast, cozy, bold, bright]. Main scene: [describe one clear focal scene in 2 to 3 sentences]. Main character: [describe one character: age, hair, clothing, pose]. Supporting details: [2 to 3 small details, e.g. animals, objects, weather]. Color palette: [3 to 4 named colors]. Title should be bold, rounded, with a thick outline and drop shadow, so it reads at thumbnail size. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people.
>
> Format: Portrait book cover 1600 x 2560.

## B3. Rules for every cover

- **Original artwork only.** No existing characters, brands, or real people. No copyrighted book covers as references.
- **Title exact.** The title must match the topic entry word for word, and the line breaks must match the brief.
- **Readable at thumbnail size.** Big title, strong outline, high contrast against the background.
- **US market.** Use US grade levels (for example, "Grades 2–4") and US English spelling.
- **Age badge.** Show the age or grade range on the cover, as parents look for it.
- **Different from other covers.** Each cover must differ from the register in category, palette, character, and scene.
- **Match the category.** The cover follows the category's profile in `cover-styles.json`: its look, title style, and imagery, and it avoids what the profile's avoid list names. Check the palette against the profile's hue ranges.
- **Match the book.** The cover must show the brief's title lines, colours, and genre. Title text and palette are checked by script; the author, badge, series line, and tagline are confirmed by viewing.
- **Verify before use.** Read the design back, run the cover checks, and confirm the design is the one you approved.

## B4. Cover register (never reuse these)

| Book | Category | Palette | Main character | Scene | Canva link |
|---|---|---|---|---|---|
| The Bakery on Cutter Street (Cutter Street Novel, Book 1) | Adult small-town romance, contemporary, sweet | Plum, rose, cream, gold (#6B2D5C, #C8707A, #F5EBDD, #D4A548) | Woman holding a loaf of bread, a man holding a wrench, and a dog | Snowy bakery storefront on Cutter Street | https://canva.link/k2uuo12fdna991p |

## B5. Ready-to-use prompts for other categories

Each prompt below uses a different category, palette, character, and scene from the register above. Change the title and series details before use.

### 1. Cozy mystery (adult, cozy)

> Cozy mystery cover for the US market, adult readers. The title must read exactly on two lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top: "[SERIES NAME] · BOOK 1". Tagline below the title: "A [small coastal town] mystery." Bottom badge: "A COZY MYSTERY". Author name at bottom: "[Author name]". Style: warm, moody, elegant, high-contrast. Main scene: a quaint seaside village at dusk, a lighthouse in the distance, and a small tea shop with glowing windows. Main character: a woman in her forties in a cardigan holding a teacup, looking thoughtful. Supporting details: foggy harbor, a rowboat, lanterns. Color palette: deep teal, warm amber, cream, and plum. Title should be bold and serif, with a gold outline and drop shadow. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people.
>
> Format: Portrait book cover 1600 x 2560.

### 2. Bedtime story collection (ages 3 to 6)

> Bedtime story collection cover for the US market, ages 3 to 6. The title must read exactly on two lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top: "[COLLECTION NAME] · STORIES FOR BEDTIME". Tagline below the title: "[Short, soothing hook, 3 to 6 words]". Bottom badge: "AGES 3–6". Author name at bottom: "[Author name]". Style: soft, dreamy, gentle, calming. Main scene: a starry night sky over a quiet hilltop, a crescent moon, and a small cottage with one warm window lit. Main character: a small fox in pajamas holding a stuffed toy, sleepy eyes. Supporting details: drifting clouds, a few glowing stars, a blanket. Color palette: midnight blue, lavender, soft gold, and mint. Title should be rounded and gentle, with a light outline and soft glow. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people.
>
> Format: Portrait book cover 1600 x 2560.

### 3. Early reader (ages 4 to 7, learning to read)

> Early reader cover for the US market, ages 4 to 7, learning to read. The title must read exactly on two lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top: "[SERIES NAME] · READ IT YOURSELF" (or the series name and a level badge). Tagline below the title: "[Simple, encouraging hook]". Bottom badge: "LEVEL 2 · GRADES K–1". Author name at bottom: "[Author name]". Style: playful, bright, cheerful, simple shapes. Main scene: a sunny classroom corner with a big open book, colorful alphabet blocks, and a paper rocket on a shelf. Main character: a boy with round glasses and a backpack, holding up a pencil and smiling. Supporting details: a few block letters, a ladybug, a bright sun. Color palette: tomato red, sunshine yellow, bright blue, and white. Title should be extra large and chunky, with a thick navy outline. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people.
>
> Format: Portrait book cover 1600 x 2560.

### 4. Large-print puzzle book (adults, 55 and up)

> Large-print puzzle book cover for the US market, adults 55 and up. The title must read exactly on two lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top: "LARGE PRINT · [PUZZLE TYPE]". Tagline below the title: "[Relaxing, friendly hook]". Bottom badge: "100+ PUZZLES · LARGE PRINT". Author name at bottom: "[Author name]". Style: clean, friendly, bold, uncluttered. Main scene: a cozy armchair by a window with a steaming mug of coffee, a large puzzle grid on a side table, and a pencil resting on it. Main character: none. Supporting details: a small potted plant, soft window light, a folded newspaper. Color palette: forest green, warm cream, coral, and slate gray. Title should be very large, with a high-contrast color block behind it. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people.
>
> Format: Portrait book cover 1600 x 2560.

### 5. Practical how-to guide (adults)

> Practical how-to guide cover for the US market, adult readers. The title must read exactly on two lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top: "[TOPIC] MADE SIMPLE". Tagline below the title: "[Clear benefit, 3 to 6 words]". Bottom badge: "STEP-BY-STEP". Author name at bottom: "[Author name]". Style: clean, modern, confident, bright. Main scene: a tidy kitchen counter with a laptop, a notebook with a checklist, and a bowl of fresh ingredients. Main character: none. Supporting details: a small plant, a clock, neat labels. Color palette: charcoal, mint green, orange, and white. Title should be bold and sans-serif, with a clean color block. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people. No medical, financial, or legal claims on the cover.
>
> Format: Portrait book cover 1600 x 2560.

## B6. Notes

- `cover-styles.json` holds all 14 approved categories. A brief for a category that has no entry must be refused, and the category must be confirmed in `category-pool.json` first.

- If a prompt produces a cover that is too similar to one in the register, change the palette and scene before sending it.
- Keep the title text exactly as written in the topic entry, including the line breaks.
- For every book, save the final approved Canva link and hex palette in the Cover register so no future cover repeats them.
- The Bakery cover was made before the brief rule existed. Its brief was written afterwards from the cover, and its subtitle differs from metadata.json. See its review-notes.md.
