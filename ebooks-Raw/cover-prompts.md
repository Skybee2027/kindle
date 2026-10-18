# Cover Prompts for Canva AI

Use these prompts with the Canva `create-design` tool. Each book needs its own prompt, and no two covers may share the same category, palette, main character, or scene.

## How to use

1. Look up the book's first category in `ebooks-Raw/cover-styles.json`. Use its reader, look, title style, palette hue ranges, badge rule, imagery, and avoid list for the brief and the design.
2. Write the book's cover brief next: `ebook-folder/cover-brief.json`. Set `genre` and `style_profile` to that exact pool path. Fill every field from metadata.json: the title lines exactly as on the cover, the subtitle, author, series line, tagline, badge (or "none" for adult books), genre, reader age, style, three or four palette colours as hex codes, the focal scene, the character, and supporting details. Check it with `python3 scripts/check_cover_brief.py "ebooks-Final/<folder>"` before any design.
3. Copy the template below and fill it in from the brief. Use the brief's exact title lines and palette names.
4. Check the **Cover register** below. The new book must differ from every cover listed in category, palette, character, and scene.
5. Send the prompt with the format `Portrait book cover 1600 x 2560`.
6. Wait for the job to finish, then read the design back. Confirm the title text is complete (Canva AI has dropped title lines before). If a line is missing, fix it in Canva before exporting.
7. Export as PNG, convert to 1600 x 2560 RGB JPEG as `cover-ebook.jpg`, then run `python3 scripts/check_cover.py "ebooks-Final/<folder>/cover-ebook.jpg" --book "ebooks-Final/<folder>"`. It must pass.
8. View the finished cover yourself. Confirm the author name, badge, series line, and tagline, which OCR may not read. Record the result in review-notes.md.
9. Add the book to the **Cover register**, with its Canva link and hex palette from the brief.

## Template prompt

> [Category] cover for the US market, [age range] (for example, ages 7 to 9). The title must read exactly on [number] lines: "[Title line 1]" on the first line and "[Title line 2]" on the second line. Series line at top in a bold ribbon: "[SERIES NAME] · BOOK [n]". Tagline below the title: "[Short hook, 3 to 6 words]". Bottom badge: "[AGE/GRADE BADGE]". Author name at bottom: "[Author name]". Style: [style words, e.g. vibrant, high-contrast, cozy, bold, bright]. Main scene: [describe one clear focal scene in 2 to 3 sentences]. Main character: [describe one character: age, hair, clothing, pose]. Supporting details: [2 to 3 small details, e.g. animals, objects, weather]. Color palette: [3 to 4 named colors]. Title should be bold, rounded, with a thick outline and drop shadow, so it reads at thumbnail size. Keep the top third clear for the title. Original artwork, no existing characters, brands, or real people.
>
> Format: Portrait book cover 1600 x 2560.

## Rules for every cover

- **Original artwork only.** No existing characters, brands, or real people. No copyrighted book covers as references.
- **Title exact.** The title must match the topic entry word for word, and the line breaks must match the brief.
- **Readable at thumbnail size.** Big title, strong outline, high contrast against the background.
- **US market.** Use US grade levels (for example, "Grades 2–4") and US English spelling.
- **Age badge.** Show the age or grade range on the cover, as parents look for it.
- **Different from other covers.** Each cover must differ from the register in category, palette, character, and scene.
- **Match the category.** The cover follows the category's profile in `cover-styles.json`: its look, title style, and imagery, and it avoids what the profile's avoid list names. Check the palette against the profile's hue ranges.
- **Match the book.** The cover must show the brief's title lines, colours, and genre. Title text and palette are checked by script; the author, badge, series line, and tagline are confirmed by viewing.
- **Verify before use.** Read the design back, run the cover checks, and confirm the design is the one you approved.

## Cover register (never reuse these)

| Book | Category | Palette | Main character | Scene | Canva link |
|---|---|---|---|---|---|
| The Bakery on Cutter Street (Cutter Street Novel, Book 1) | Adult small-town romance, contemporary, sweet | Plum, rose, cream, gold (#6B2D5C, #C8707A, #F5EBDD, #D4A548) | Woman holding a loaf of bread, a man holding a wrench, and a dog | Snowy bakery storefront on Cutter Street | https://canva.link/k2uuo12fdna991p |

## Ready-to-use prompts for other categories

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

## Notes

- `cover-styles.json` holds all 14 approved categories. A brief for a category that has no entry must be refused, and the category must be confirmed in `category-pool.json` first.

- If a prompt produces a cover that is too similar to one in the register, change the palette and scene before sending it.
- Keep the title text exactly as written in the topic entry, including the line breaks.
- For every book, save the final approved Canva link and hex palette in the Cover register so no future cover repeats them.
- The Bakery cover was made before the brief rule existed. Its brief was written afterwards from the cover, and its subtitle differs from metadata.json. See its review-notes.md.
