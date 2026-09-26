---
title: LLM Wiki
type: concept
tags: [pkm, llm, knowledge-management]
aliases: [LLM-maintained wiki, LLM Wiki pattern, second brain]
created: 2026-09-26
updated: 2026-09-26
sources: [2026-09-26-llm-wiki-pattern]
status: active
---

# LLM Wiki

A pattern for personal knowledge management in which an LLM agent **incrementally
builds and maintains a persistent, interlinked collection of markdown pages** that
sits between the user and their raw sources. Each new source is read once and
integrated — updating entity pages, revising summaries, flagging contradictions — so
knowledge is "compiled once and then kept current, not re-derived on every query"
([[2026-09-26-llm-wiki-pattern]]). This vault is an instance of it.

## How it works

**Layers** ([[2026-09-26-llm-wiki-pattern]]):

| Layer | Role | Who writes it |
|---|---|---|
| Raw sources | Immutable source of truth | Human curates |
| Wiki | Summaries, entity/concept pages, comparisons, overview, synthesis | LLM only |
| Schema | Conventions + workflows (CLAUDE.md / AGENTS.md) | Co-evolved |

**Operations:**
- **Ingest** — read source, discuss takeaways, write summary, update index, update
  related pages, append to log. One source may touch 10–15 pages.
- **Query** — read index, drill into pages, answer with citations; file good answers
  back as new pages so exploration compounds too.
- **Lint** — find contradictions, stale claims, orphans, missing pages and links,
  gaps to research.

**Navigation:** `index.md` (catalog, content-oriented) and `log.md` (timeline,
append-only, prefix-parseable).

## Why it works
The expensive part of a wiki is bookkeeping, not thinking; LLMs drive the cost of
that bookkeeping toward zero ([[maintenance-burden]]). The human's job becomes
curating sources, directing analysis, and asking good questions
([[2026-09-26-llm-wiki-pattern]]).

## Contrast with RAG
| | [[retrieval-augmented-generation|RAG]] | LLM Wiki |
|---|---|---|
| When synthesis happens | At every query | At ingest, then maintained |
| Accumulation | None | Compounds with sources *and* questions |
| Contradictions | Rediscovered (or missed) each time | Flagged once, persist on the page |
| Infrastructure | Embeddings / vector store | Markdown + index file (search optional) |

## Open questions
> [!question] Open question
> How do errors propagate? A mistaken summary can be cited by later pages. Mitigations
> in this vault: inline citations to source pages, immutable raw layer, periodic lint
> *(inference)*.

## Connections
- [[memex]] — the 1945 antecedent; LLM Wiki supplies the missing maintainer
- [[obsidian]] — the reading/browsing front end ("the IDE")
- [[qmd]] — search layer for when the index outgrows itself

## Sources
- [[2026-09-26-llm-wiki-pattern]]
