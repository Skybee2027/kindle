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
