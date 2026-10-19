# Review notes: Shorthand for Murder (Lantern Bay Cozy Mystery, Book 1)

Guide version: 2.1
Topic: "Shorthand for Murder: A Lantern Bay Cozy Mystery, Book 1" (ebook-topics/topics-log.json)
Format: text-only EPUB, US English, US dollars
Cover: created in Canva (design DAHYZj0dpJ8, https://canva.link/b2hhonvsog6szdn), author "Skybee" in small text, approved by owner 2026-10-18. Cover checks: check_cover_brief.py and check_cover.py pass.

## Structure
- 30 chapters, each with a "## Chapter N: Title" heading. The topic outline lists 10 story beats; each beat was expanded into three chapters to meet the 25 to 40 chapter rule in guide section 3.
- Front matter: title, subtitle, author, copyright line, fiction disclaimer, AI disclosure (all in the first 12 lines or immediately after).
- Back matter: AI disclosure repeated as the last line.
- Word count: about 65,500 words including front and back matter. Target 55,000 to 60,000 with the 10 percent tolerance in check_book.py (up to 66,000). Close to the upper limit; a trim of 2,000 to 3,000 words would give more margin.

## Checks run on this package
- scripts/check_language.py: pass, 0 issues (US spelling, no British word list hits, no pound sterling).
- scripts/check_names_sources.py: pass after renaming look-alike names and words (Hall to Center, Harborline to Tidewater, Dorn to Corliss, Councilor to Council Member, Priya Nand to Priya Rao, and others). No research claims; sources is empty.
- scripts/build_epub.py: built EPUB with EB Garamond embedded (3 woff2 files) and the OFL license saved in fonts/.
- scripts/check_book.py: run after build; see the final run recorded in the run log.
- epubcheck: run through check_book.py; result recorded in the run log.

## Checks not run
- Readability: not required (adult cozy mystery, no reading_age).
- Cover brief and cover checks: not run; the cover belongs to Kindle-3.

## Judgement review (read-through)
- Continuity fixes made during drafting: Tessa's sign-in time, Dale's notebook times, bangle count (two bangles, bare right wrist), council roster and forged vote tally, Fennick Falls described as a market town in Carrow County, Helen's approval time (11:52 p.m.), the file history times (created 10:58 p.m., changed 11:41 p.m.).
- Dark content: one death (a fall after a struggle), no graphic violence on page. Profanity removed from the cozy voice.
- Real people, places, and brands: none used. Harbor and town names are fictional. The Bait and Tackle, Gull Café, and Harbor Center names are invented.
- Sources: none needed; the book makes no research claims.

## Open questions for the owner
- The 30-chapter structure and the expanded beats should be confirmed as the template for future Lantern Bay books.
- Length is near the top of the allowed range; trimming is an option if the owner wants more margin.
- The final chapter introduces a new thread (a login from the old clerk credentials on the night of July 14). The owner may want to confirm it for Book 2.

## Guide conformance pass (book creating guide, version 2.1)
- Section 5: body text changed from justified to left-aligned, ragged right. First-line indent kept for the novel. One font family (EB Garamond), licence saved in fonts/.
- Section 8: title page now reads "By Skybee" under the subtitle. Copyright, fiction disclaimer, and AI disclosure use the exact wording.
- Section 11: metadata.json now includes word_count, chapters, format, price_usd, royalty_tier, content_warnings, files, and the cover string.
- Section 14: manuscript.docx regenerated from the updated manuscript; KDP-FORM-ANSWERS.md regenerated from metadata.json.
- Checks run after these changes: build_epub.py (cover true, 3 fonts embedded); epubcheck (0 errors, 0 warnings); check_book.py (all checks pass).
- Open item for owner: the approved cover shows a small series line and a small tagline. Section 6 says no small text except the author name. Owner to decide whether to keep the cover as approved or ask for a revision.

## Cover review (Kindle-3, 2026-10-19)
- Designs made in this run: 0 (cover-ebook.jpg already present and owner-approved; no redesign).
- Scripts: check_cover_brief.py pass (11 checks); check_cover.py pass (12 checks); check_language.py pass (0 issues).
- Visual review at full size:
  - Title lines "Shorthand" / "for Murder": present, largest element, readable. Pass.
  - Subtitle "A Lantern Bay Cozy Mystery, Book 1": present, spelled as metadata. Pass.
  - Author "Skybee": present at bottom, spelled correctly. Pass.
  - Series line "LANTERN BAY COZY MYSTERY": present and spelled as brief. Pass (small text; see open item).
  - Tagline "Every word on the record.": present and spelled as brief. Pass (small text; see open item).
  - Badge: none (rule for Women Sleuths is "none"). Pass.
  - Genre and look: a woman seen from behind at a lit typewriter in a window over a river town at dusk, with a steno-tape ribbon. Matches the profile's look (one sleuth figure, clue motif, quiet town, elegant serif title in cream on deep colour).
  - Avoid list (bright cartoon colours, romance-cover poses, gore): none present.
  - Palette: deep plum, amber, cream as briefed.
- Open item: the series line and tagline are small. The cover guide section 5 asks for the series line and tagline to be short, and the owner noted this before. Owner to confirm the cover as approved.
- Why it suits the book: the steno tape running from a lit window over a lake town shows the court-reporter clue and the cozy, moody tone of the mystery.

## Kindle-3 run status (2026-10-19)
- Cover checks: pass. EPUB rebuilt with cover; epubcheck 0 errors, 0 warnings.
- check_book.py: pass (54 checks).
- KDP-FORM-ANSWERS.md regenerated from metadata.json.
- Not completed: full judgement read of manuscript.md (guide step 7, 65,511 words). Only the mechanical checks and earlier continuity notes above were confirmed in this run. Not approved into "Ready to publish/".
