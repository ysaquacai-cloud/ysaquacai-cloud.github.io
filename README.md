# AQua.CAI lab website

English-only Jekyll website for Advanced Quantum Computing and Artificial Intelligence at Yonsei University.

## Local preview

Install Ruby (3.3 recommended) and Bundler 2.4.22, then:

```sh
bundle install
python3 -m unittest discover -s tests
bundle exec ruby tests/test_templates.rb
python3 scripts/validate.py
bundle exec jekyll build
python3 scripts/validate.py --site
bundle exec jekyll serve
```

Open http://127.0.0.1:4000. Normal content changes are rebuilt by the development server. The generated `_site/` directory is ignored by Git.

## Edit content

- `_data/publications.json`: title, ordered authors, ISO date, year, status (`published`, `accepted`, or `preprint`), venue, HTTPS URL, themes, optional DOI/arXiv links. Preserve each stable ID when a preprint becomes published. `selected: true` features a record on the homepage. Use zero-padded ISO dates (`2026-05-10`) for chronological sorting. Retain arXiv links when adding journal information.
- `_data/people.json`: name, role, group, interests, initials, optional email. Current groups: `Principal investigator`, `Postdoctoral researchers`, `Graduate students`. PI summary and full biography also live in the People templates.
- `_data/research.json`: four research themes and their related publication IDs.
- `_data/news.json`: event title, dates, summary, category; newest first. Homepage shows up to three entries.
- `_data/site.json`: navigation, shared contact information, Scholar link.
- `people/jeongho-bang/index.html`: PI biography and appointments.
- `contact/index.html`: research inquiry guidance.
- `assets/css/site.css`: shared colors, typography and responsive styles.

Optional information should be omitted rather than filled with placeholders. The site uses original SVG artwork and text initials instead of supplied portraits. Font files are served from Google Fonts with system fallbacks.

Read [content review notes](docs/content-review.md) for the remaining editorial confirmations, including two members whose preferred English names are needed. These notes are excluded from the published site.

## GitHub Pages

The workflow validates and builds pull requests. Pushes to `main` build and deploy through GitHub Actions. In repository **Settings → Pages**, select **GitHub Actions** as the build source. Public URL: https://ysaquacai-cloud.github.io/.

An unsuccessful validation prevents deployment. No secrets are needed; the deployment job uses the scoped GitHub Pages token permissions. If branch protections require a pull request, merge the reviewed feature branch through the repository's normal process.

After deployment, verify the homepage, `/research/`, `/publications/`, `/people/`, `/people/jeongho-bang/`, `/contact/`, `/news/`, and an unknown URL. Confirm publication search and the mobile menu work.

## Rollback

Revert the website commit on `main` and let the deployment workflow rebuild. To restore the original build settings, record the previous Pages source before changing it. Do not force-push over other contributors' changes.

## Bibliography provenance

The initial 61 records came from the temporary Google Site. Titles, ordered authors and dates were retrieved from Crossref or arXiv on 23 October 2026. arXiv first-submission dates are used where available. Journal online publication dates may differ from printed issue years. The original and substantially revised relativistic simulation records remain separately linked, as in the supplied source.
