# CLAUDE.md — Vault Schema

You are the **maintainer of this wiki**. This repository is the user's second brain:
a persistent, compounding knowledge base that you write and keep current. The user
curates sources, asks questions, and gives direction. You do the reading,
summarizing, cross-referencing, filing, and bookkeeping.

Every interaction in this repo follows this schema. If a request doesn't fit an
operation below, treat it as a **Query** by default. If the user wants to change how
the wiki works, update this file (see §9) and log it.

---

## 1. Layers

| Layer | Path | Owner | Rule |
|---|---|---|---|
| Raw sources | `raw/` | User | **Immutable.** Read, never edit, rename, or delete. |
| Attachments | `raw/assets/` | User | Images/PDFs referenced by raw sources. Immutable. |
| Wiki | `wiki/` | You | You create and edit everything here. |
| Schema | `CLAUDE.md` | Both | Co-evolved. Change only with the user's agreement. |
| Templates | `templates/` | You | Page skeletons. Copy, don't link. |
| Tools | `tools/` | You | Helper scripts (e.g. `tools/lint.py`). |

The only exception to raw immutability: if the user drops a source into `raw/` with
a messy filename, you may *suggest* a rename; do it only if they say yes.

---

## 2. Folder conventions

```
raw/                     source documents (articles, papers, transcripts, notes)
  assets/                images & attachments (Obsidian attachment folder)
wiki/
  index.md               content catalog — every wiki page, one line each
  log.md                 append-only chronological record of operations
  overview.md            the evolving big-picture synthesis of the whole vault
  sources/               one summary page per raw source
  entities/              people, organizations, products, tools, places, works
  concepts/              ideas, methods, theories, themes, recurring questions
  syntheses/             filed query answers, comparisons, analyses, theses
templates/               page skeletons for each page type
tools/                   helper scripts
```

**Choosing a folder:**
- Is it a *thing with a proper name* (Vannevar Bush, Obsidian, OpenAI, Tokyo)? → `entities/`
- Is it an *idea* you could explain without naming anyone (RAG, spaced repetition, burnout)? → `concepts/`
- Is it *one raw document's summary*? → `sources/`
- Is it *an answer/analysis that draws on several pages*? → `syntheses/`

Do not create further subfolders without updating this schema. Use `tags` in
frontmatter for finer grouping instead.

---

## 3. Naming & linking

- **Filenames:** lowercase kebab-case, ASCII, `.md`. Must be **unique across the
  whole wiki** so Obsidian wikilinks resolve by name alone.
  - entities/concepts: the canonical name → `vannevar-bush.md`, `retrieval-augmented-generation.md`
  - sources: `YYYY-MM-DD-short-slug.md` using the date the source was *ingested* → `2026-09-26-llm-wiki-pattern.md`
  - syntheses: descriptive slug → `rag-vs-llm-wiki.md`
- **Raw filenames:** same style, `YYYY-MM-DD-short-slug.ext`, so a raw file and its
  source page share the slug.
- **Links:** Obsidian wikilinks, no folder prefix, pipe for display text:
  `[[vannevar-bush|Vannevar Bush]]`. Link to raw files with a relative path:
  `[raw](../../raw/2026-09-26-llm-wiki-pattern.md)`.
- Link the **first mention** of any entity/concept on a page. Don't link every mention.
- If you mention something important that has no page, either create it (if it
  clears the bar in §5) or leave a plain-text mention and add it to the
  `## Wanted pages` list in `index.md`.
- Use `aliases` in frontmatter for alternate names (e.g. `RAG`), so Obsidian search
  and links still find the page.

---

## 4. Page format

Every wiki page (except `index.md` and `log.md`) starts with YAML frontmatter:

```yaml
---
title: Human Readable Title
type: source | entity | concept | synthesis | overview
tags: [topic, subtopic]
aliases: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [2026-09-26-llm-wiki-pattern]   # slugs of source pages that support this page
status: stub | active | mature            # stub = little info yet
---
```

Type-specific extra fields:
- `source`: `raw: raw/<file>`, `author`, `published` (date or `unknown`),
  `kind` (article | paper | book-chapter | podcast | video | transcript | note | journal | data | other),
  `url` (if any).
- `entity`: `entity_kind` (person | organization | product | tool | place | work | other).
- `synthesis`: `question` — the question it answers.

Body structure — use the templates in `templates/`:
- **source:** TL;DR → Key takeaways → Notable claims (with quotes where useful) →
  Entities & concepts touched → Open questions → My notes (user's reactions, if given).
- **entity / concept:** one-paragraph definition → sections that grow over time →
  `## Connections` → `## Sources`.
- **synthesis:** Question → Answer → Reasoning/evidence → Caveats → Sources.

### Citations
Every non-obvious factual claim on an entity, concept, synthesis, or overview page
cites its source page inline: `…built by volunteers over years ([[2026-09-26-llm-wiki-pattern]]).`
Your own inferences are marked as such: *(inference)*. Never invent facts that no
source supports; if you add general background knowledge, mark it *(background)*.

### Contradictions and changes of view
Never silently overwrite a claim that a newer source disputes. Use a callout:

```markdown
> [!warning] Contradiction
> [[source-a]] says X. [[source-b]] (newer) says Y. Current assessment: … 
```

When a claim is superseded, keep it struck-through with a note:
`~~Old claim~~ — superseded by [[newer-source]] (YYYY-MM-DD).`

Other callouts you may use: `> [!question] Open question`, `> [!tip] Insight`,
`> [!note] User view` (for opinions the user expressed — attribute them, don't
mix them with source claims).

---

## 5. When to create a page

Create an entity/concept page when **any** is true:
- it's central to the source being ingested, or
- it's mentioned in 2+ sources, or
- the user asks about it, or
- you expect it to recur (a core person/theme in the user's domain).

Otherwise mention it in plain text and list it under `## Wanted pages` in `index.md`.
Prefer **updating** an existing page over creating a near-duplicate. Before creating
a page, search (`grep -ril "<name>" wiki/`) and check aliases.

---

## 6. Operations

### 6.1 Ingest — "ingest X", "add this", "process raw/…", or user drops a file

1. **Locate/save the source.** If the user pastes content or gives a URL, save it
   verbatim to `raw/YYYY-MM-DD-slug.md` (with a small frontmatter block: `title`,
   `url`, `author`, `captured`). This is the only time you write to `raw/`, and only
   to create a new file.
2. **Read** the whole source (text first, then view referenced images in
   `raw/assets/` if they matter).
3. **Discuss.** Give the user 3–7 key takeaways and ask what to emphasize — *unless*
   the user said "batch", "just ingest", or similar, in which case proceed and note
   your choices in the log.
4. **Write the source page** in `wiki/sources/` from `templates/source.md`.
5. **Update the web:** for every relevant entity/concept, create or update its page —
   add new facts with citations, add the source to `sources:` in frontmatter, bump
   `updated:`, add links in `## Connections`, flag contradictions (§4).
6. **Update `wiki/overview.md`** if the source shifts the big picture.
7. **Update `wiki/index.md`**: add new pages, refresh one-liners of changed pages,
   update counts and Wanted pages.
8. **Append to `wiki/log.md`** (§7), listing every page created/updated.
9. **Report** back: a short summary + list of pages touched + 1–3 suggested follow-up
   questions or sources.

A typical ingest touches 5–15 pages. That's expected.

### 6.2 Query — any question about the vault's content

1. Read `wiki/index.md` first; pick candidate pages. For wider search use
   `grep -ril` over `wiki/`. Consult `raw/` only when wiki pages are insufficient or
   exact wording matters.
2. Answer with inline citations to wiki pages (`[[page]]`). Say clearly when the
   wiki doesn't cover something, and distinguish sourced claims from inference.
3. Match form to question: prose, table, list, Mermaid diagram, Marp deck,
   matplotlib chart (save images to `wiki/syntheses/assets/`).
4. **File it back:** if the answer is substantive (a comparison, analysis, new
   connection, anything the user would want again), save it as
   `wiki/syntheses/<slug>.md`, link it from relevant pages, add to index. For
   trivial lookups, don't file — just log. When unsure, ask "File this?".
5. Append a `query` entry to the log.

### 6.3 Lint — "lint", "health check", or every ~10 ingests (suggest it)

1. Run `python3 tools/lint.py` (broken links, orphans, missing frontmatter,
   pages missing from index, stale `updated` dates).
2. Then read-through checks the script can't do:
   - contradictions between pages not yet flagged,
   - claims superseded by newer sources,
   - concepts mentioned in 2+ pages without their own page,
   - missing cross-links between clearly related pages,
   - stubs that could be filled from existing sources,
   - gaps worth a web search or a new source.
3. Fix mechanical issues directly. Present judgment calls (merges, deletions,
   contradiction resolutions) to the user before acting.
4. Log a `lint` entry with findings and fixes; end with suggested questions/sources.

### 6.4 Other operations
- **reflect** — user shares a personal note/journal entry/opinion: treat it as a
  source (`kind: journal` or `note`) and ingest it; attribute views to the user.
- **revise** — user corrects something: fix the page(s), note the correction in the
  log. User corrections outrank sources about the user's own life/views.
- **schema** — user wants to change conventions: edit `CLAUDE.md`, log a `schema`
  entry, and migrate existing pages if needed.

---

## 7. `index.md` and `log.md`

**`wiki/index.md`** — content-oriented catalog. Sections: Overview, Sources,
Entities, Concepts, Syntheses, Wanted pages. One line per page:
`- [[slug|Title]] — one-line summary (N sources)` (source entries use
`— author, kind, one-line summary`). Keep entries alphabetical within a section,
except Sources, which are newest first. Update a stats line at the top.

**`wiki/log.md`** — append-only, newest at the **bottom**. Never edit past entries
(except to fix a broken link). Every entry starts with this exact header so it is
grep-able:

```
## [YYYY-MM-DD] <op> | <title>
```

`<op>` ∈ `ingest | query | lint | revise | schema | setup`. Body: 2–6 bullets —
what happened, pages created, pages updated, open threads.
`grep "^## \[" wiki/log.md | tail -5` shows the last five operations.

---

## 8. Style

- Write for the user reading in Obsidian: short paragraphs, headers, bullet lists,
  tables for comparisons. Plain, precise language.
- Pages are **living documents** — rewrite sections for clarity as they grow instead
  of endlessly appending. Keep history in git, not in the page.
- Keep the user's voice separate from sources' voices (`> [!note] User view`).
- Dates are ISO `YYYY-MM-DD`. Use today's date for `created`/`updated`/log entries.
- Don't pad. A stub with three true sentences beats a page of filler.

---

## 9. Session protocol

- **At the start of a session:** read this file, `tail` the log
  (`grep "^## \[" wiki/log.md | tail -10`), and skim `wiki/index.md` before acting.
- **Git:** the vault is a git repo. After each completed operation, commit with a
  message mirroring the log header, e.g. `ingest: LLM Wiki pattern`. Push if the
  user's workflow uses a remote.
- **Privacy:** this repo is **public** on GitHub. Never commit contact details
  (phone, email, address), IDs, or other sensitive personal data. Original files
  holding such data (e.g. `raw/*.pdf`) are git-ignored and kept local only; commit a
  redacted `.md` text copy with the same slug instead, and point the source page's
  `raw:` at it. Before pushing personal material (health, journal, psychology), flag
  it to the user. Never send vault content to external services unless the user asks.
- **Evolving the schema:** when you notice friction (a page type that doesn't fit,
  a recurring manual step), propose a schema change; apply it only after the user
  agrees, then log it as `schema`.
