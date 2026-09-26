---
title: Obsidian
type: entity
entity_kind: tool
tags: [tools, pkm]
aliases: [Obsidian.md, Obsidian Web Clipper]
created: 2026-09-26
updated: 2026-09-26
sources: [2026-09-26-llm-wiki-pattern]
status: active
---

# Obsidian

Markdown note-taking app used as the **reading and browsing front end** of an
[[llm-wiki]]: the LLM edits files on one side, the human follows links, checks the
graph view, and reads updated pages in real time on the other. "Obsidian is the IDE;
the LLM is the programmer; the wiki is the codebase" ([[2026-09-26-llm-wiki-pattern]]).

## Features and plugins recommended
| Feature | Use in the vault |
|---|---|
| Graph view | See the wiki's shape — hubs and orphans |
| Obsidian Web Clipper (browser extension) | Convert web articles to markdown for `raw/` |
| Attachment folder = `raw/assets/` + hotkey for "Download attachments for current file" | Keep images local so the LLM can view them |
| Dataview (plugin) | Query YAML frontmatter into dynamic tables |
| Marp (plugin) | Render markdown slide decks from wiki content |

All from [[2026-09-26-llm-wiki-pattern]]. This vault ships `.obsidian/app.json` with
the attachment folder already set to `raw/assets`.

## Connections
- [[llm-wiki]] — its role in the pattern
- [[qmd]] — complementary search tool for the LLM side

## Sources
- [[2026-09-26-llm-wiki-pattern]]
