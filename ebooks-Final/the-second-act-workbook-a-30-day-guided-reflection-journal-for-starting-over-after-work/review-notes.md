# Review notes: The Second Act Workbook

Topic: "The Second Act Workbook: A 30-Day Guided Reflection Journal for Starting Over After Work" (ebook-topics/topics-log.json, selected 2026-10-18). Picked by scripts/pick_topic.py. Format: workbook (text-only EPUB). Target 14,000 to 16,000 words. Price $4.99. Categories: Self-Help > Personal Transformation; Self-Help > Aging or Retirement (both confirmed in ebook-topics/category-pool.json). KDP Select: no (standalone).

## Checks run (scripts/check_book.py)

- All checks pass except the two cover items, which are pending because Kindle-3 has not made the cover: "file present: cover-ebook.jpg" and "cover brief: cover brief present".
- Word count: 13,329 words, within the 10 percent tolerance of guide section 3.
- US English and US dollars (scripts/check_language.py): 0 issues.
- Title page at the top of manuscript.md (guide section 8): present.
- Workbook answer blocks (guide section 3): 38 blocks, one after each of the 30 day prompts and each of the 8 review questions.
- epubcheck: 0 errors, 0 warnings.
- Chapters: ten, with headings. Description: 302 words. Keywords: 7, each under 50 characters.

## Fixes made after the owner's review

- Spelling changed from British to US English throughout (organized, realize, neighbor, counselor, color, and others). Checked by scripts/check_language.py.
- Money: "forty pounds" in Chapter 3 changed to "forty dollars". No other currency found.
- Terms changed for a US reader: fortnight to two weeks, biscuits to cookies, takeaway to takeout, loft to attic, post to mail, shops to stores, charity shop to thrift store, rambling to hiking, fete to fair, solicitor to attorney.
- A title page was added to the top of the manuscript (title, subtitle, author). Guide section 8 requires one.
- Fill-in lines added. Every day prompt (Days 1 to 30) and every review question on the 90-day sheet now has an answer block, so the book can be used as a workbook.
- Name clashes removed: Chapter 4's friend Anna is now Laura, so she no longer sounds like Ann in Chapter 5. Chapter 3's reader Desmond is now Gerald, so the name belongs only to the Chapter 9 reader.
- Chapter 10 example: "a sourdough class" changed to "a watercolor class", so it does not repeat Chapter 5.
- Description in metadata.json checked for British spelling: none left.
- manuscript.docx regenerated from the corrected manuscript.md. The EPUB and KDP-FORM-ANSWERS.md were rebuilt.

## Open items for the owner (not done)

- Cover: pending. Kindle-3 makes it.
- Reader review: the topic entry asks for a panel of two or three people from the target age group to read the first three chapters. This has not been done.
- Editing: the topic entry asks for a human editor to check the opening stories for clichés. This has not been done.
- Citation: the one study cited, Pennebaker and Beall (1986), needs to be checked against the journal before upload. It is used only to say that structured private writing has been studied since the 1980s.
- Sales figures in the topic entry are estimates, not verified data.
- Category paths: the owner should confirm both paths still match the KDP category picker.
- Keyword "retirement journal for women": the owner may want to review it.

Cover: pending, to be created by Kindle-3 (cover brief and cover).
