# Log

*Append-only. Newest at the bottom. Every entry header: `## [YYYY-MM-DD] <op> | <title>`.*
*Last 5 entries: `grep "^## \[" wiki/log.md | tail -5`*

## [2026-09-26] setup | Vault initialized
- Created schema `CLAUDE.md`, folder structure (`raw/`, `raw/assets/`, `wiki/{sources,entities,concepts,syntheses}`, `templates/`, `tools/`).
- Created `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`, page templates, `tools/lint.py`, `.obsidian/app.json` (attachments → `raw/assets`).

## [2026-09-26] ingest | LLM Wiki: a pattern for personal knowledge bases
- Saved user-pasted idea file to `raw/2026-09-26-llm-wiki-pattern.md`.
- Created source page: [[2026-09-26-llm-wiki-pattern]].
- Created concepts: [[llm-wiki]], [[retrieval-augmented-generation]], [[maintenance-burden]], [[memex]].
- Created entities: [[vannevar-bush]], [[obsidian]], [[qmd]].
- Updated: [[overview]], index. Added 4 Wanted pages (NotebookLM, Dataview, Marp, Tolkien Gateway).
- Discussion step skipped: user asked for a demonstration ingest. Open thread: which domains the vault should focus on.

## [2026-09-26] ingest | Vault focus statement (reflect)
- Saved the user's purpose statement to `raw/2026-09-26-vault-focus.md`; created source page [[2026-09-26-vault-focus]].
- Created: [[me]] (owner profile), [[generalist]], [[ai-product-development]], [[personal-productivity]].
- Updated: [[overview]] (rewritten around the vault's purpose and 4 themes), [[llm-wiki]], index.
- Open threads: current role, specialty, target role, definition of "productive". Proposed a schema tweak for domain tags (pending user approval).

## [2026-09-26] ingest | Resume — Dr. Shubham Kashyap
- Saved uploaded PDF to `raw/2026-09-26-resume.pdf`; created source page [[2026-09-26-resume]]. Phone and email kept out of the wiki.
- Created entities: [[mediq]], [[grow-baby-grow]], [[saathi]], [[athira-health]], [[docbot]], [[stemz-healthcare]], [[n8n]], [[claude-code]].
- Created concepts: [[physician-technologist]], [[ai-assisted-development]].
- Updated: [[me]] (rewritten as a full profile), [[ai-product-development]] (inferred advantages now sourced), [[generalist]], [[overview]], index.
- Discussion step skipped: the user asked directly to add the resume. Push held because the repo is public; resolved by the schema entry below.

## [2026-09-26] schema | Privacy rule for a public repo
- User chose to keep original PDFs out of git: added `raw/*.pdf` to `.gitignore`. The resume PDF is kept local only.
- Added `raw/2026-09-26-resume.md`, a text copy with email and phone removed; [[2026-09-26-resume]] now points to it.
- Updated `CLAUDE.md` §9 Privacy: the repo is public; commit redacted copies; flag personal material before pushing.
