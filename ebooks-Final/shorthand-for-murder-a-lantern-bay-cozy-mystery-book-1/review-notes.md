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

## Proofreading log (owner's read-and-fix cycle, 18 October 2026)
- Pass 1 of 11 complete: every line of manuscript.md read in order from front matter to the final AI disclosure.
- Fixes in pass 1: Chapter 1 and 2 wording and timeline; Chapter 4 stair count (thirteen) and hyphenation; Chapter 6 recess length (fifteen minutes) and adjournment gap (seven minutes, sixteen minutes total); Chapter 7 clerk's upload time and Tessa's sign-in day; Chapter 9 photo timestamp (9:52 p.m.); Chapter 13 file-history timing; Chapter 14 Dale's notebook times (9:09) and a stray phrase; Chapter 15 Bernice's account of the recess and the email's domain; Chapter 16 Tessa's whereabouts and Priya's report of the car; Chapter 17 Sheriff's visit day and Bo's initials; Chapter 18 Walt's count of "did not go in" (three); Chapter 20 audit-log times and witness wording; Chapter 22 funeral day; Chapter 23 transcript timing; Chapter 26 recording length (4:52) and the time since the steps; Chapter 27 vote tally (none for, five against); Chapter 28 Bernice's address, company name, office location, drive handling and who sent the June copy; Chapter 29 the transcript confirmation and Joan Cho's name (state records contact renamed Irene Lasko); Chapter 30 the login time (11:26 p.m.) and the boat name.
- Mechanical checks after pass 1: no double spaces, no stray markup, 30 chapters in order, Joan Cho used only for the Lantern Bay librarian.
- Rebuilt after pass 1: manuscript.docx (pandoc), shorthand-for-murder.epub (build_epub.py), epubcheck 0 errors and 0 warnings, check_book.py pass. metadata word_count set to 65445; KDP-FORM-ANSWERS.md regenerated.
- Remaining: passes 2 to 11 (5 full read-and-fix passes, then 3 passes, repeated twice more). Not yet started.
