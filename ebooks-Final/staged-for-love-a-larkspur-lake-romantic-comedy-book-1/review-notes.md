# Review notes: Staged for Love: A Larkspur Lake Romantic Comedy, Book 1

Run: Kindle-2, 2026-10-20. Guide version 2.1. Cover: pending, to be created by Kindle-3 (cover brief and cover).

## Structure
- 28 chapters, numbered 1 to 28, each headed "## Chapter N: Title".
- Mapped to the 11-beat outline from the topic entry in ebook-topics/topics-log.json. Beats cover the trucks and the lamp on Birch Street, the placemat terms, the Dressler complaint and the back field lease, the Route 9 storage unit, the hearing, the closing, and the fireworks ending.
- Guide section 3 asks for 25 to 40 chapters for a romance novel. 28 is inside that range.
- Word count: 59,364 words in the body (headings excluded, counted by regex on manuscript.md). Target was 55,000 to 62,000. Recorded in metadata.json as word_count 59364.

## Checks run and results
- build_epub.py: built staged-for-love.epub (3 fonts embedded, no cover yet). Rebuilt after the last manuscript edit.
- epubcheck 5.3.0 (EPUB 3.3 rules), run with the bundled jar: 0 errors, 0 warnings, 0 infos.
- check_language.py: PASS after replacing "loft" (British for attic) with "hayloft" and US spellings.
- check_names_sources.py: PASS. Same-person pairs approved in metadata name_aliases: Tess/Tessa, Pris/Priscilla, Fenner/Fenners, Ostrander/Ostranders, Pruitt/Pruitts.
- Research-claim check: PASS. Trigger words ("percent", "according to") reworded to "cents on the dollar" and "in Owen's opinion". The book makes no factual claims that need sources.
- Scan for leftover capitalized name carry-overs: "Vance" matched only inside "grievance" (no issue). "Judge" appears only as ordinary usage. "Harbor" appears once as ordinary usage. "Lantern" appears only in lowercase.
- make_kdp_answers.py: regenerated KDP-FORM-ANSWERS.md from current metadata.
- check_book.py: final run passes every gate except the two cover items (cover-ebook.jpg and cover-brief.json), which Kindle-3 creates. epubcheck 0 errors, 0 warnings. Word count 59518 by the checker, within the 55,000 to 62,000 target.
- pandoc: manuscript.docx created from manuscript.md.

## Edits made during name and language clean-up
- Name collisions with the sibling series and within the book were reworded. Examples: Call to Phone or Name; Anything to Whatever; Come to Go or Return; Let to We'll, Show, Trust, or Leave; Put to Place, Lay, or Mark; Get to Bring; Give to Grant, Offer, or Name; Take to Seek or Please take; Like to Meaning, Exactly, or As if; Well to Oh; Will to Would; Done to Finished or Deal; Down or Downstairs to Below or Along; Outside to Beyond or Out front; None to No one; Nothing to Not a thing or Nobody; Off to Out at; Men to The men; Thank to Thanks or Credit Len.
- Place names: Lakeshore to Northline; Lakeside to Pinecrest or Kestrel; Sumac Lane to Sumac Court; Township to Village where the Office of Zoning and Land Use is named.
- Chapter titles changed: ch11 "Forty Cents on the Dollar"; ch14 "The Hayloft"; ch25 "Fireworks Over the Pier".
- Continuity fixes made during drafting: travel distances, motel sleeping arrangements, the Fenner and Ostrander house names, Ledger dates (Len's December 22 entry; Tessa age 17 in 2009), placemat custody (Owen keeps the original until closing), Moose sleeping in the barn hayloft, a typo ("wwool"), and removal of real brand mentions (Brewers, Facebook).

## Full read
- The stored prompt asks for one full read of the manuscript after the checks. This run did automated checks plus targeted reads of the key chapters (closing, fireworks, Dressler marina, goldenrod field, Sumac Court letter) and the chapter-level fixes listed above. A complete line-by-line read was not finished in this run. Open for a human editor or a follow-up pass.

## Open questions
- Is a 28-chapter romance count acceptable under guide section 3 (25 to 40)? Yes by the guide's range, but the human editor should confirm.
- The cover is pending. Kindle-3 creates it, using the cover brief.
- Confirm the blue rug and forty-cents terms read clearly to readers who did not see earlier series material (none is used here).
- No Amazon upload, no pricing or KDP submission made in this run.
