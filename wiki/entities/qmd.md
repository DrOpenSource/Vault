---
title: qmd
type: entity
entity_kind: tool
tags: [tools, search]
aliases: []
url: https://github.com/tobi/qmd
created: 2026-09-26
updated: 2026-09-26
sources: [2026-09-26-llm-wiki-pattern]
status: stub
---

# qmd

A local, on-device search engine for markdown files using hybrid BM25/vector search
with LLM re-ranking. Offers both a CLI (the LLM can shell out to it) and an MCP server
(the LLM can use it as a native tool) ([[2026-09-26-llm-wiki-pattern]]).

## When to adopt
Recommended once the wiki outgrows `index.md`-based navigation; at small scale the
index is enough ([[2026-09-26-llm-wiki-pattern]]). Not installed in this vault yet.

## Connections
- [[llm-wiki]] — optional search layer
- [[retrieval-augmented-generation]] — similar retrieval techniques, applied over the compiled wiki

## Sources
- [[2026-09-26-llm-wiki-pattern]]
