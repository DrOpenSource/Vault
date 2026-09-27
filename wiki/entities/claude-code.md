---
title: Claude Code
type: entity
entity_kind: tool
tags: [tools, ai-coding]
aliases: []
created: 2026-09-26
updated: 2026-09-27
sources: [2026-09-26-resume, 2026-09-26-ponytail, 2026-09-27-gstack, 2026-09-27-claude-pricing]
status: stub
---

# Claude Code

An AI coding agent. It is in your toolkit for building and shipping products ([[2026-09-26-resume]]), and it is the agent that maintains this vault.

## Harness
Claude Code is an [[agent-harness]]: the loop, tools, permissions and context management around the model. The Claude Agent SDK is the same harness as a library ([[2026-09-27-claude-pricing]]). Staying on Claude Code rather than running your own harness is the recommendation in [[harness-cost-comparison]].

## Skills & plugins
- [[gstack]] — Garry Tan's sprint skill pack (about 55 skills); tried 2026-09-27. Adds about 7K always-on tokens, and 3K–51K per skill used ([[2026-09-27-gstack]]).
- [[ponytail]] — minimal-code ruleset; reviewed, and you decided not to use it. Install with `/plugin marketplace add DietrichGebert/ponytail`, then `/plugin install ponytail@ponytail` as a separate prompt ([[2026-09-26-ponytail]]).

## Connections
- [[agent-management-plan]] — your operating plan for Claude Code agents
- [[ai-assisted-development]]
- [[llm-wiki]] — this vault runs on it
- [[me]]

## Sources
- [[2026-09-26-resume]]
- [[2026-09-26-ponytail]]
- [[2026-09-27-gstack]]
- [[2026-09-27-claude-pricing]]
