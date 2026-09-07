# Junwen Lou academic website

Live site: https://llljjjwww333.github.io/

## Structure

Independent About, Research, CV, Publications, and Projects pages share one profile sidebar and navigation. The site is English-only, uses system sans-serif fonts, and serves both English and Chinese PDF CVs.

## Update the academic background

Edit `site.json`, then run `python tools/build_pages.py`. No third-party Python packages are required for the website build.

- `education`: append a record with `degree`, `institution`, `period`, and `details`. List the most recent degree first. Only add confirmed education, not possible future programs.
- `publications`: add `title`, `authors`, `status`, and an optional `url`.
- `bio`: introductory paragraphs independent of any particular institution.
- `sections`: HTML content for research, experience, projects, awards, and skills. Add an experience entry within the experience section as your background grows.
- `teaching` and `service`: reserved arrays of text entries. Empty arrays stay hidden; populated arrays appear on the CV page.
- `updated`: visible update month.

The generated HTML works without JavaScript or a server-side build. Commit the generated pages and styles after rebuilding. PDF CVs are separate files: replace `files/Junwen_Lou_CV_EN.pdf` and `files/Junwen_Lou_CV_ZH.pdf` when their content changes. Updating website data does not automatically modify PDFs.

## Reference

Structure informed by https://xd-w.github.io/cv/ (reviewed during this revision). Code and personal content are independently authored from the user's CV. Existing manuscript and patent status remain unchanged.

Do not upload `tmp/`: it contains local checks and authentication files. The deployment package excludes it.
