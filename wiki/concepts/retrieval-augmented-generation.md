---
title: Retrieval-Augmented Generation
type: concept
tags: [llm, retrieval]
aliases: [RAG]
created: 2026-09-26
updated: 2026-09-26
sources: [2026-09-26-llm-wiki-pattern]
status: stub
---

# Retrieval-Augmented Generation (RAG)

An approach where a user uploads documents, the system retrieves relevant chunks at
query time, and the LLM generates an answer from them. It works, but "the LLM is
rediscovering knowledge from scratch on every question" — nothing accumulates
between queries ([[2026-09-26-llm-wiki-pattern]]).

## Examples cited
NotebookLM, ChatGPT file uploads, and most RAG systems ([[2026-09-26-llm-wiki-pattern]]).

## Weakness highlighted
Subtle questions that require synthesizing several documents force the model to
find and re-assemble the same fragments every time ([[2026-09-26-llm-wiki-pattern]]).

## Connections
- [[llm-wiki]] — the alternative: synthesize at ingest, maintain persistently
- [[qmd]] — uses retrieval techniques (BM25/vector) but *over the wiki*, not in place of it *(inference)*

## Sources
- [[2026-09-26-llm-wiki-pattern]]
