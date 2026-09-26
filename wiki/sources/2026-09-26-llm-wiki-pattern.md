---
title: "LLM Wiki: a pattern for personal knowledge bases"
type: source
kind: note
raw: raw/2026-09-26-llm-wiki-pattern.md
author: unknown (idea file shared by the user)
published: unknown
url: 
tags: [pkm, llm, knowledge-management, meta]
aliases: [LLM Wiki idea file]
created: 2026-09-26
updated: 2026-09-26
sources: []
status: active
---

# LLM Wiki: a pattern for personal knowledge bases

> [raw source](../../raw/2026-09-26-llm-wiki-pattern.md) · author unknown · idea file / note
> This is the founding document of this vault — the vault is an instance of the pattern it describes.

## TL;DR
Instead of having an LLM re-retrieve fragments from raw documents on every question
([[retrieval-augmented-generation|RAG]]), have it **incrementally build and maintain a
persistent, interlinked markdown wiki** between you and your sources. Knowledge is
compiled once, kept current, and compounds with every source and question. The human
curates and asks; the LLM does all the bookkeeping.

## Key takeaways
1. **Compounding vs. rediscovering.** RAG re-derives knowledge per query; an
   [[llm-wiki|LLM wiki]] accumulates it — cross-references, flagged contradictions
   and syntheses already exist when you ask.
2. **Three layers:** immutable raw sources → LLM-owned wiki → a schema file
   (CLAUDE.md / AGENTS.md) that makes the LLM a disciplined maintainer. The schema is
   co-evolved.
3. **Three operations:** *ingest* (one source may touch 10–15 pages), *query*
   (good answers get filed back as pages), *lint* (periodic health checks).
4. **Two navigation files:** `index.md` (content catalog, read first on every query)
   and `log.md` (append-only, grep-able timeline). Index alone scales to ~100 sources
   / hundreds of pages without embeddings.
5. **The bottleneck is maintenance, not thinking.** Wikis die because upkeep grows
   faster than value; LLMs make upkeep nearly free ([[maintenance-burden]]).
6. **Lineage:** spiritually closest to [[vannevar-bush|Vannevar Bush]]'s
   [[memex|Memex]] (1945) — private, curated, with associative trails; the LLM
   solves the maintenance problem Bush couldn't.
7. **Tooling is optional:** [[obsidian|Obsidian]] as the reading "IDE", git for
   history, [[qmd]] for search once the index isn't enough.

## Notable claims
- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
- NotebookLM, ChatGPT file uploads, and most RAG systems work in the
  rediscover-per-query mode.
- An index file "works surprisingly well at moderate scale (~100 sources, ~hundreds
  of pages) and avoids the need for embedding-based RAG infrastructure."
- LLMs can't read markdown with inline images in one pass — read text first, then
  view images separately.
- Suggested use cases: personal (goals, health, psychology), research, reading a
  book (a personal Tolkien Gateway–style companion wiki), business/team wikis,
  competitive analysis, due diligence, trip planning, course notes, hobbies.

## Entities & concepts touched
- [[llm-wiki]] — the pattern itself (primary subject)
- [[retrieval-augmented-generation]] — the contrasting approach
- [[maintenance-burden]] — the problem the pattern solves
- [[memex]] and [[vannevar-bush]] — historical antecedent
- [[obsidian]] — recommended viewer, plus Web Clipper, Dataview, Marp plugins
- [[qmd]] — recommended local search engine

## Open questions
- At what size does `index.md` stop being enough and real search become necessary for *this* vault?
- How much human review of each ingest is right? (The author prefers one-at-a-time, involved ingests.)
- How should personal/sensitive material (health, psychology) be handled differently, if at all?
- Risk not discussed in the source: LLM summarization errors compounding across pages *(inference)* — citations and lint are the mitigation.

## My notes
<!-- Add your reactions here, or tell me and I'll add them. -->
