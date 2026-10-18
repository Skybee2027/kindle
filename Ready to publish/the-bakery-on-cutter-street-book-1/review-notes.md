# Review notes: The Bakery on Cutter Street, Book 1

## Status
- Manuscript: complete, 39 chapters, about 55,760 words (meets the guide's 55,000 minimum).
- EPUB: built with pandoc, cover embedded, validated with EPUBCheck 5.3.0 (0 errors, 0 warnings). EB Garamond embedded, OFL license in fonts/.
- DOCX: same text, for review or alternate upload.
- Cover: cover-ebook.jpg, 1600 x 2560 RGB JPEG, from the approved Canva design DAHYVdFvmjE.

## Guide compliance
- Length: 55,000 to 65,000 words. About 55,760, the bottom of the range.
- Chapters: 39, within the guide range of 25 to 40 (guide updated by owner direction).
- Covers: one per book (guide section 5 updated).
- Copyright and AI disclosure: copyright page reads "Copyright © 2026 Skybee. All rights reserved." with the AI disclosure as its last line, per the owner's decision.
- Description: 189 words (guide 150 to 400). Keywords: 7.

## Full read-through (2026-10-18)
All 39 chapters were read line by line. Fixes made in this pass:
- Chapter Five and Chapter Thirteen: Biscuit's arrival. He was Tom Kowalski's dog, walked by Hannah in Chapter Five, so Chapter Thirteen now says he had walked the street with her once before.
- Chapter Eleven: the market is now the second Saturday, not a repeat of the first market in Chapter Ten.
- Chapter Twelve and Chapter Eighteen: Hannah's time back in town. The dates now run from the summer (she was home by August, per Chapter Nine).
- Chapter Twelve: Mabel the second is described as settled, two months on, not in her first week.
- Chapter Sixteen: the starter is no longer described as named after the grandmother (Dorothy).
- Chapter Eighteen: Eli's line about "her apartment" and an undefined "last night" were corrected.
- Chapter Nineteen: Mrs. Ortiz's marriage timeline now fits Manny's death in 2015.
- Chapter Twenty-Three: Dale Henner was 31 in 1994, not 21 years younger.
- Chapter Twenty-Four: Eli's quoted line matches Chapter Twenty-One; the second town meeting is named as a second meeting.
- Chapter Twenty-Five: Eli's mother left when he was nine, matching Chapter Fourteen.
- Chapter Twenty-Six: the caller is the paper-shop woman, not the hardware owner (Eli runs the hardware store and is in the room).
- Chapter Twenty-Seven: the bakery sign is red paint, not gold leaf.
- Chapter Thirty: Eli's mother left a note, not a postcard, with no reference to the wrist (the postcard in Chapter Thirty-Six is the one that mentions the wrist).
- Chapter Thirty-Two: moved to the Wednesday before Christmas so it follows Chapters Thirty and Thirty-One; the confession now matches the letter Hannah posted in Chapter Thirty-One. Profanity removed.
- Chapter Thirty-Three: the appointment of Eli as trustee is dated December.
- Chapter Thirty-Four: the 1989 loan matches Chapter Twenty (Hollis lent Dorothy the money and she repaid him). Profanity removed.
- Chapter Thirty-Five: the rolling pin has been hidden for 36 years, not 35.
- Chapter Thirty-Six: the mother's letter is signed "Mom"; "apartment" and the red sign.
- Chapter Thirty-Eight: Mabel the third is two months old; Mabel the second died in February; the hammer box is dated 1978, the year the store opened.
- Chapter Thirty-Nine: the rolling pin label is in Hollis's hand; Eli's letter took years, not thirty years, to read.
- Spelling and idiom: converted to US English throughout (for example gray, color, mom, sidewalk, flashlight, cookies, parking lot, dish towel, sweater, dessert, line, mailbox, trash can, leash, pharmacy, around).

- Chapter Eleven: title changed to "Sold Out by Four", since the tables are not bare until four o'clock.
- Chapter Thirty-Six: the mother's new postcard no longer repeats the "sorry about the wrist" line from the earlier postcard in Chapter Twenty-Five.
- Chapter Thirty-Eight: Eli asks Hannah to be his partner, not his trustee, since Chapter Thirty-Seven already made her trustee. The proposal date is January, not spring.

## Continuity notes
- Timeline: Mabel the second (Chapters Eight to Eleven) and Mabel the third (Chapters Thirty-Eight to Thirty-Nine) are consistent with the dates above.
- The sign reads "THE CUTTER STREET BAKERY" (red, est. 1961). "Brooks & Sons" is the old lettering inside the front window. The new sign in Chapter Thirty-Seven reads "BROOKS & CARVER".
- Eli's mother, Ruth Carver, left when Eli was nine; her postcard arrives in Chapter Thirty-Six.
- Tom Kowalski keeps his own starter, descended from Dorothy's jar (Chapter Eleven).

## Recommended human checks before publishing
- Dialogue and rhythm: an editor pass is still recommended, since the text is AI-drafted.
- KDP browse category and keywords (check in the category picker).
- Confirm price ($3.99), royalty tier (70%), and the series name.

## Upload checklist (KDP)
- [ ] Manuscript: the-bakery-on-cutter-street.epub
- [ ] Cover: cover-ebook.jpg
- [ ] Title, subtitle, author (Skybee), description, keywords, category from metadata.json
- [ ] AI-content disclosure answered truthfully
- [ ] Price $3.99, 70% royalty

## Approval (owner-directed review, 2026-10-18)
- Cover: cover-ebook.jpg, 1600 x 2560 RGB JPEG, approved Canva design. PASS.
- EPUB: EPUBCheck 5.3.0, 0 errors, 0 warnings. PASS.
- Length: about 55,760 words; guide minimum 55,000. PASS.
- Chapters: 39, within the guide range of 25 to 40. PASS.
- Copyright line and AI disclosure present on copyright page. PASS.
- Description: 189 words (guide 150 to 400). PASS. Keywords: 7. PASS.
- Price $3.99, royalty 70%. PASS.
- Full line-by-line read of all 39 chapters completed; fixes listed above applied. PASS.
- Nothing has been uploaded to Amazon.

## Cover review (18 October 2026, added after the cover rules were revised)
- Brief written from the cover after it was made: see cover-brief.json. Its palette is the intended one (plum, rose, cream, gold).
- check_cover.py --book: passes. Palette 37% near brief colours; title readable at full and thumbnail size; title letters large.
- Viewed: "A Cutter Street Novel · Book 1" line at top, title "The Bakery on Cutter Street", tagline "Flour, Frost and a Second Chance", "BY SKYBEE" at bottom. The author line is the one OCR cannot read, so it was confirmed by viewing.
- Open issue for the owner: the cover prints "Flour, Frost and a Second Chance" as its subtitle, but metadata.json has the subtitle "A Cutter Street Novel, Book 1". Decide which one KDP uses; the cover and the KDP subtitle must match before upload.
- Review of prompts and code (18 October 2026): this book had no style.css. style.css was added (guide section 5: EB Garamond, left-aligned, first-line indent), and the EPUB was rebuilt with it. epubcheck passes with 0 errors and 0 warnings. guide_version changed from 2.0 to 2.1. KDP-FORM-ANSWERS.md regenerated. check_book.py passes all checks.
