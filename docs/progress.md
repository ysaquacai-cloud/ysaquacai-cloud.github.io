# Implementation ledger

Plan: ../implementation-plan.md; approved in conversation with English-only requirement.

Ruling: Work in a fresh clone on feat/english-lab-website because this task had no local repository or existing checkout to protect.
Ruling: Use JSON content files instead of YAML; Jekyll supports both and JSON enables dependency-free validation.
Ruling: Use initials instead of photos because no original approved portraits were supplied.
Ruling: Omit two incomplete member records pending preferred English spellings; preserve the names in content-review.md.
Ruling: Use the supplied university affiliation and omit unconfirmed unit/room/hardware details.
Ruling: Implement a lightweight publication search because the archive contains 61 records; preserve all HTML for no-JavaScript access.
Ruling: Retain a linked substantial revision as a separate record to avoid inventing an equivalence decision.

Content audit: all 61 scholarly records verified against arXiv/Crossref metadata. Source-derived biographies and research copy require normal lab review.
Validation unit tests: seven tests observed failing before validator existed and passing afterward.

Final review: independent reviewer found Bundler compatibility, accepted-record rendering, and absent optional-email handling. All three corrected. Two regression tests observed failing before template fixes and passing afterward; Bundler 2.4.22 installed and bundle install/build passed.
Final verification: 7 content tests + 2 template tests pass; all generated internal links pass. Desktop and mobile layouts inspected; homepage has no horizontal overflow at 360 and 768 pixels. Mobile menu opens and closes with Escape. Publication query and status filtering tested. Automated empty-string clearing in the browser tool did not reliably dispatch input and is not claimed as verified.
User explicitly authorized GitHub commit/push. Publishing now proceeds after collaborator access was granted.
