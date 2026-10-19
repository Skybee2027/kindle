# Review notes: Study Smarter, Not Longer (A Workbook for Adults Returning to School)

Guide version: 2.1
Topic: "Study Smarter, Not Longer: A Workbook for Adults Returning to School" (ebook-topics/topics-log.json)
Format: workbook, text-only EPUB, US English, US dollars
Price: $4.99 (70% royalty tier), KDP Select: no (standalone)

## Structure
- Nine chapters, each with a "## Chapter N: Title" heading, matching the nine-item chapter outline in the topic entry.
- Title page at the top of manuscript.md (title, subtitle, "By Skybee"), then the copyright page with the non-fiction disclaimer and the AI disclosure as its last line. The AI disclosure is repeated as the final line of the manuscript.
- Chapter-to-outline mapping: Ch 1 Why Going Back Feels Hard (baseline self-check); Ch 2 Your Week, Mapped (protected blocks, buffer); Ch 3 Retrieval Practice (Roediger and Karpicke, 2006); Ch 4 Spacing Things Out (Cepeda et al., 2006; 2008); Ch 5 Shuffling It Up (interleaving; Rohrer and Taylor, 2007); Ch 6 Reading With Purpose (three passes); Ch 7 Notes That Work (two-column method); Ch 8 Test Review Without Panic (error log, practice tests); Ch 9 Keep Going (habit tracking, asking for help, 30-day plan).
- Worked examples follow a small cast of returning students: Maya, Tomasz, Renata, Marcus, and Gordon (a study partner in Ch 5). The names were checked for look-alikes (see below).
- Activity blocks: 106 blocks, each with "**Your answer:**" and three or more lines of escaped underscores. The Thirty-Day Plan in Chapter 9 has one day activity per day, each with an answer block.

## Word count
- About 16,090 words in manuscript.md (metadata word_count 16092). Topic target 16,000 to 19,000 words; check_book.py range with the 10 percent tolerance is 14,400 to 20,900. Within range.

## Research claims and sources
- Every research claim in the text cites a named source, and each source is listed in metadata.json "sources": Dunlosky et al. (2013); Roediger and Karpicke (2006); Cepeda et al. (2006); Cepeda et al. (2008); Rohrer and Taylor (2007); Pashler et al. (2008); Gollwitzer (1999).
- Claims are limited to what these sources report. Dunlosky et al. (2013) utility ratings are cited as ratings, not as effect sizes. No effect sizes or percentages are given.
- Two claims were narrowed during drafting to match the sources: the Roediger and Karpicke description was restated without claims about study time, and the spacing section states that the strongest evidence is for verbal recall.
- Learning-style claims are excluded and the Pashler et al. (2008) review is cited as evidence against them.
- The worked examples are fictional. They are presented as illustrations, not as reported studies.

## Checks run on this package
- scripts/check_language.py: pass, 0 issues (US spelling, no British forms, no pound signs).
- scripts/check_names_sources.py: first run failed with look-alike candidates made by ordinary capitalized words in headings and sentence openers ("Ask"/"Asking", "Build"/"Building", "Cover"/"Over", "Exam"/"Example", "Mix"/"Mixing", "Not"/"Note"/"Notice", "Out"/"Put", "Prompt"/"Prompts", "Read"/"Reading", "Study"/"Studying"). These were not character names. The affected headings and sentence openers were reworded (for example "Getting Help" for "Asking for Help", and "Activity" for "Prompt" in the activity labels). Second run: pass. Character names are Maya, Tomasz, Renata, Marcus, and Gordon, which do not look alike; no names are reused for another person.
- scripts/build_epub.py: built study-smarter-not-longer.epub with EB Garamond embedded (3 woff2 files) and the OFL license in fonts/.
- epubcheck (run directly on the built EPUB): 0 errors, 0 warnings.
- scripts/check_book.py (final run): 30 of 32 checks pass. The two failures are the cover items that Kindle-3 makes: "file present: cover-ebook.jpg" and "cover brief: cover brief present" (cover-brief.json missing). Every other check passes, including the title page, disclaimer, AI disclosure, US English and dollars, distinct names and sourced claims, workbook answer blocks, word count, and epubcheck.
- scripts/make_kdp_answers.py: KDP-FORM-ANSWERS.md generated from metadata.json.

## Checks not run, and why
- Readability (scripts/readability.py): not required. This is an adult workbook with no reading_age in metadata.
- Cover brief and cover checks: not run. Kindle-3 makes the cover and cover-brief.json.
- Kindle Previewer read-through: owner step before upload, not run here.

## Judgment review (read-through)
- Full read-through completed for structure, repeated passages, and contradictions. Continuity fixes: Tomasz's certification exam timeline is consistent across Chapters 2, 8, and 9; Marcus is the payroll-certification student in Chapters 3, 7, and 4 (the five-month plan); Maya's statistics course is used in Chapters 1, 5, and 7.
- Non-fiction disclaimer is present and exact. The book gives no medical, financial, or legal advice; the health-related note in Chapter 8 refers readers to a health professional and makes no medical claim.
- No real brands, trademarked products, or real living people are named. Study tools are described generically (paper, phone, flashcards).
- No promises about grades. Tomasz's and Marcus's results are presented as their own experiences in the examples.

## Open questions for the owner
- The Dunlosky et al. (2013) utility ratings are cited as the review's ratings. The owner may want the book to say "rated" wherever a reader might read the rating as a measured benefit; the current text already does this.
- Cepeda et al. (2008) is cited for the claim that the best gap rises with the retention interval. Please confirm this reading before publishing if the owner wants the exact wording checked by a reviewer.
- The book uses a "Sources and Further Reading" back-matter heading that is not a numbered chapter. Confirm this is acceptable for the KDP listing.

## Cover
The cover checks (cover-ebook.jpg, cover-brief.json, and the cover checks in check_book.py) are not run here and remain open.

Cover: pending, to be created by Kindle-3 (cover brief and cover).
