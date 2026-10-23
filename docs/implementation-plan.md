# AQua.CAI Lab Website — Implementation Plan v0.2

Date: 23 October 2026

Status: Draft for discussion. This document proposes the design and implementation sequence; it does not authorize construction or publication. Open decisions are intentional and should be resolved through revisions with the lab.

## 1. Goal and confirmed decisions

Create a small multipage academic website in the existing `ysaquacai-cloud/ysaquacai-cloud.github.io` repository. Visitors should understand the lab's research, find its people and outputs, and know how to contact or join it. The temporary Google Site is source material, not a binding design.

Confirmed: GitHub Pages hosting, a small multipage structure, and iterative plan review before implementation.

Working assumptions: prospective researchers and academic collaborators are the primary audience; English is the main language; a lab member will maintain content through GitHub. These assumptions require confirmation.

## 2. Source review and implications

Reviewed the temporary About, Research, Publications & Preprint, and Members pages, including expanded publication archives and homepage news. Also reviewed the repository listing and current index.html. Linked event-detail pages and individual scholarly records have not been audited.

| Observation | Proposed response |
|---|---|
| AQua.CAI expands to Advanced Quantum Computing and Artificial Intelligence. | Preserve the identity, subject to confirmation of official spelling and capitalization. |
| Four research areas are already identified. | Retain them as the initial research taxonomy; rewrite descriptions around concrete questions, methods, and outputs. |
| Research headings mix Korean and English; some descriptions are incomplete. | Adopt a deliberate language policy and consistent section templates. |
| The homepage contains a mission paragraph and two 2026 conference notices. | Add research and publication previews; show recent news directly instead of requiring an accordion click. |
| The Members page places a long PI biography before the team. | Keep a concise PI introduction on People, move the detailed biography to a PI profile page. |
| Member entries have uneven names, roles, and research descriptions. | Use one profile format and confirm the roster before migration. |
| The publication archive spans entries labeled 2008–2026 and mixes journal articles and preprints. | Use structured records and explicit publication status. |
| Some journal years differ from the years under which entries are listed; September arXiv identifiers appear under July. | Confirm the intended date convention rather than silently changing dates or assuming errors. |
| Address and telephone labels are blank. | Display only confirmed contact information. |
| The homepage uses a large brown scientific illustration. | Consider a smaller, more informative hero with an authentic research figure or lab image. The existing palette is optional. |
| GitHub currently contains README.md and a ten-line placeholder index.html. | Plan a new structure; retain repository history and inspect deployment settings before changing them. |

Source content is provisional. Do not infer missing affiliations, member identities, paper authors, recruitment openings, or research claims.

## 3. Recommended information architecture

Primary navigation: **Home · Research · Publications · People · Join & Contact**

Supporting pages: **PI profile** and **News archive**. Keep the archive in the homepage's “All news” link and footer rather than adding another primary navigation item. Individual research and event pages are optional later additions when enough public content exists.

| Page | Proposed URL | Purpose |
|---|---|---|
| Home | `/` | Explain the lab and direct visitors to its work and people |
| Research | `/research/` | Explain the four themes and connect them to actual outputs |
| Publications | `/publications/` | Provide a complete, readable scholarly record |
| People | `/people/` | Introduce the current team and, if applicable, alumni |
| Join & Contact | `/contact/` | Explain inquiries, opportunities, and location |
| PI profile | `/people/jeongho-bang/` | Present the detailed PI biography and professional links |
| News archive | `/news/` | Preserve dated public announcements |

Why this structure: the existing core categories are sound. A separate About page would largely duplicate the homepage, while recruitment and contact currently lack a clear destination. A PI subpage makes the rest of the team easier to discover.

Alternative: keep the PI's full biography on People in an accessible expandable section. This reduces page count but makes the team page more complex. The separate profile is preferred.

## 4. Page-by-page specification

### Home

Order of content:

1. Compact header with lab wordmark and navigation.
2. Hero with AQua.CAI, its full name, verified university/unit affiliation, and a two-sentence mission. Primary link: Explore Research. Secondary link: Meet the Team.
3. Four research-theme previews, each with a concise explanation and a link to the relevant Research section.
4. Three selected papers, manually chosen for significance and breadth, using the same records as the Publications page.
5. Three recent news items with explicit dates and optional links; All News link to archive.
6. Brief invitation for research inquiries, linking to Join & Contact.
7. Shared footer with verified affiliation and email.

Provisional mission wording for discussion: “We study the foundations of quantum information and develop methods for quantum computing, learning, communication, and sensing. Our work connects theoretical questions with algorithms and applications on quantum systems.” The PI should approve the scientific emphasis before use.

Avoid unsupported claims of quantum advantage. If specific results demonstrate an advantage, connect the claim to the relevant publication and conditions.

### Research

Keep four initial themes:

| Theme | Content to prepare |
|---|---|
| Quantum Information Science | Core theoretical questions, mathematical/physical approaches, and representative findings |
| Quantum Computing & Algorithms | Algorithm design, simulation and optimization; confirm the scope of software and hardware work |
| Quantum Machine Learning & AI | Learning theory, hybrid methods, and specific projects such as Neural Information Causality, if still representative |
| Quantum Communication & Sensing | Confirm active directions and supply a complete description, including relevant communication/security/metrology work |

Each theme receives a stable anchor, 100–180 words of approved explanation, one meaningful figure where available, and two or three related papers. Use a common sequence: question → approach → current work → related outputs. Include named software or datasets only when public links exist.

The temporary site mentions access to an on-site IBM quantum computer. Confirm the wording, current access, and institutional relationship before repeating it. Do not imply ownership or partnership from that sentence alone.

Use static figures with captions rather than an automatic carousel. Create dedicated project pages only when a project has enough content to justify one.

### Publications

Display one canonical record per scholarly work, with a title, authors in official order, venue or preprint status, year, and DOI/arXiv links. Optional links: code, data, permitted manuscript, and BibTeX.

Proposed organization: Published & Accepted, followed by Preprints, each grouped by year with newest first. Show accepted items explicitly as “Accepted” or “In press”; do not invent volume or page data. For published work, use the journal publication year; for preprints, use the first public posting year. Preserve separate dates in the underlying records.

When a preprint becomes an article, update its existing record and retain the arXiv link. For substantially revised works with different identifiers, confirm with the lab whether they represent one work or distinct outputs before merging.

Do not use month headings unless dates are reliable and useful. Add year jump links. A small title/author search can be added if the final archive warrants it; the complete bibliography must remain available without JavaScript. Search is not required for the first release.

Before migration, audit metadata against publisher/arXiv records: exact titles, authors, dates, status, DOI, and version relationships. The temporary list is an inventory, not an authoritative bibliography.

### People and PI profile

People: short PI introduction, followed by postdoctoral researchers, graduate students, and any other confirmed categories. Show alumni only if entries are supplied. Preserve a lab-approved order within groups.

Each member entry: preferred English name, optional Korean name, role/program, two or three research interests, photo if approved, and selected professional links. Email is optional for individual members. Hide absent fields rather than showing blanks or dummy links.

PI profile: full name, verified title and affiliation, short biography, research interests, education, selected appointments, professional service, Scholar link, and optional CV. The temporary page identifies Prof. JeongHo Bang, but all current titles and official English unit names should be confirmed.

Do not automatically turn incomplete trial entries into final profiles. Confirm the complete roster, romanization, degree labels, and current/alumni status.

### Join & Contact

Include confirmed recruitment status, eligible visitor/applicant categories, research fit, and inquiry instructions. Link to official university admissions information where appropriate. Distinguish a general research inquiry from a formal application.

Use the listed `jbang@yonsei.ac.kr` as a candidate primary contact, pending confirmation. Add the exact campus, building, room, and address only when supplied. A directions link is sufficient; an embedded map is optional.

If no formal openings exist, use approved inquiry language rather than announcing vacancies. Begin with email links; a contact form would introduce an external service and maintenance obligations.

### News

Each record has a date, title, short description, and optional destination. Preserve conference notices if still useful as a record of activity; distinguish event dates from announcement dates. Review linked participation pages separately before deciding what belongs on the public site. Public news should explain the event's relevance; internal travel or participation logistics need not be migrated.

## 5. Visual and language direction

Recommended visual direction: restrained academic design with a light background, dark navy text, and one teal or blue accent. These colors are a proposal, not an inferred branding requirement. Use generous spacing, readable text widths, consistent figure captions, and modest headers on inner pages. Avoid a large decorative banner on every page.

Use authentic research diagrams, approved lab photos, or an intentionally simple typographic hero. Reuse the current banner only if the lab wants it and has an appropriate source asset. Prepare approved portraits at a consistent aspect ratio.

Language options:

- Recommended initial option: English-first pages, with Korean names and official Korean affiliation text where useful.
- Alternative: complete English and Korean versions with a language switch and matching page routes. This increases translation and update work and should be chosen before implementation.

Do not mix heading languages arbitrarily. Set appropriate document language metadata and mark Korean text where applicable.

## 6. Proposed technical architecture

Recommended: Jekyll-generated static HTML with custom layouts, plain CSS, and minimal JavaScript, deployed to the existing GitHub Pages repository. Shared templates keep headers and footers consistent; Markdown and YAML separate recurring content from presentation. Content is present in generated HTML, including publications and member profiles.

GitHub documents built-in Jekyll support and recommends GitHub Actions for deployment automation. Final runtime versions and workflow permissions will be chosen against the supported environment during implementation, then pinned where appropriate.

Alternative: plain HTML/CSS files. This has less build setup but requires editing repeated layouts or adding a separate templating mechanism. Prefer it if the maintainer strongly prefers editing HTML and the content changes rarely. A client-side application framework is unnecessary for the proposed scope.

Proposed repository structure (not created yet):

```text
index.html                     Homepage template replacing the placeholder
research/index.html            Research overview
publications/index.html        Bibliography template
people/index.html              Team page
people/jeongho-bang.md          Detailed PI biography
contact.md                     Join and contact copy
news/index.html                News archive
_layouts/default.html          Shared document structure and metadata
_layouts/page.html             Standard inner-page layout
_includes/header.html          Navigation and mobile menu
_includes/footer.html          Shared contact and affiliation
_includes/publication.html     Reusable citation presentation
_data/site.yml                 Identity, navigation and contact details
_data/research.yml             Research descriptions and related paper IDs
_data/people.yml               Member profiles and display order
_data/publications.yml         Canonical scholarly records
_data/news.yml                 Dated announcements
assets/css/site.css            Design tokens and responsive styles
assets/js/navigation.js       Accessible mobile-menu enhancement
assets/images/                 Approved images, with optimized derivatives
404.html                       Helpful missing-page destination
_config.yml                    Site URL and build configuration
Gemfile / Gemfile.lock         Build dependencies
.github/workflows/pages.yml    Validation, build and authorized deployment
README.md                      Maintenance and preview instructions
```

Data fields:

- Research: stable ID, title, description, optional figure/caption, related publication IDs.
- People: stable ID, preferred names, category, role, interests, display order, optional photo/email/links, alumni flag.
- Publications: stable ID, title, author list, status, publication/preprint dates, venue, DOI/arXiv URLs, theme IDs, optional code/data/BibTeX links, selected flag.
- News: stable ID, announcement date, optional event dates, title, summary, optional link.

Data flow: a maintainer edits a content record → validation checks required fields and references → Jekyll generates the pages → the approved publishing workflow deploys static files. Featured papers and research links reference publication IDs rather than duplicate citations.

## 7. Implementation tasks and review points

These tasks begin only after the plan is satisfactory and the user requests implementation.

1. **Finalize the content brief.** Confirm identity, audience, language, roster, research descriptions, and recruitment wording. Deliver a content checklist with owners and a list of assets. Acceptance: no unresolved factual assumptions in launch copy.
2. **Audit and prepare migration data.** Review scholarly records and event links; normalize people and research content. Acceptance: citations have verified metadata, uncertain items are held for review, and missing optional information is omitted cleanly.
3. **Prepare a design preview.** Show Home and one inner-page layout at desktop and mobile sizes using representative approved content. Acceptance: the lab agrees on hierarchy, palette, typography, and image treatment before full layout implementation.
4. **Build the shared site foundation.** Add templates, navigation, styles, metadata, data structure, and local build instructions. Acceptance: all proposed routes render, shared navigation is consistent, and mobile navigation works with a keyboard.
5. **Implement page content.** Populate Home, Research, Publications, People, PI profile, Join & Contact, and News. Acceptance: no placeholder text, broken data references, duplicate scholarly records, or empty profile controls.
6. **Verify the complete site.** Run build, content-validation and internal-link checks; manually review desktop, tablet and mobile layouts, keyboard access, images, and citations. Acceptance criteria are listed below.
7. **Review the complete preview with the lab.** Incorporate factual and visual corrections. Acceptance: launch copy and design are accepted; only then proceed with the requested publication step.
8. **Deploy and hand over.** Inspect actual Pages settings, configure the agreed workflow, and verify the public site and direct links after deployment. Record a rollback procedure and instructions for ordinary updates. Preserve the Google Site until the new site is accepted; later add a move notice there if requested.

## 8. Verification and completion criteria

- All intended routes work when opened directly and refreshed, including the PI page and 404 page.
- No horizontal page overflow at 360, 768, and 1440 pixel viewport widths; long paper titles, Korean names, and URLs wrap correctly.
- Primary content and links remain usable without JavaScript; mobile navigation has a usable fallback.
- Keyboard users can reach and operate navigation with visible focus; menus expose correct state and do not trap focus.
- Semantic headings, a skip link, meaningful link labels, alt text, and WCAG AA text-contrast targets are checked.
- All internal links and image paths resolve. DOI/arXiv and institutional links are spot-checked manually where automated requests are blocked.
- Publication validators reject missing required fields, duplicate IDs, invalid statuses and unknown theme references. Tests cover a preprint becoming published and an entry without optional links.
- Templates handle members without portraits, papers with long author lists, and a news list with fewer than three items.
- Titles and descriptions are unique; canonical URLs use the verified public domain. Add a sitemap, robots.txt and an approved social-preview image.
- Images are resized and compressed; noncritical images load lazily. Avoid automatic video, large animation libraries, and unnecessary remote fonts.
- No unapproved biographies, fabricated content, unfinished labels, or private event logistics appear in the published site.
- A maintainer can add a publication or member through the documented content files and preview the result before publication.

## 9. Launch scope and later additions

First release: seven routes, shared responsive design, four research themes, verified bibliography, consistent people profiles, contact/recruitment information, and a small news archive.

Possible later additions: full bilingual content, dedicated project pages, publication search/filtering, a resources page, a gallery, event pages, or a custom domain. Add these when content and maintenance needs justify them. No login, database, contact form, analytics, or CMS is proposed for the initial release.

## 10. Decisions for the next revision

| Decision | Proposed default | Lab response |
|---|---|---|
| Primary audience | Prospective researchers and academic collaborators | |
| Official name | AQua.CAI — Advanced Quantum Computing and Artificial Intelligence | |
| Official affiliation | Confirm exact English and Korean unit names | |
| Languages | English-first, with selected Korean names/affiliation | |
| Navigation | Home, Research, Publications, People, Join & Contact | |
| Research themes | Retain the existing four, revise descriptions | |
| Publication grouping | Status, then journal/preprint year | |
| PI biography | Separate supporting page | |
| Recruitment | Confirm current status and inquiry instructions | |
| Visual style | Light, restrained academic design; navy plus one accent | |
| Maintenance | GitHub editing of Markdown/YAML content | |
| Technical approach | Jekyll and GitHub Pages | |

## Sources

- Temporary About: https://sites.google.com/view/aqua-cai-temporary/about
- Temporary Research: https://sites.google.com/view/aqua-cai-temporary/research
- Temporary Publications: https://sites.google.com/view/aqua-cai-temporary/publications-preprint
- Temporary Members: https://sites.google.com/view/aqua-cai-temporary/members
- Repository: https://github.com/ysaquacai-cloud/ysaquacai-cloud.github.io
- Current source: https://github.com/ysaquacai-cloud/ysaquacai-cloud.github.io/blob/main/index.html
- GitHub Pages and Jekyll: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll
