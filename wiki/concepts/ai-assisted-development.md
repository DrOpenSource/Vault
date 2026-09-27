---
title: AI-Assisted Development
type: concept
tags: [ai-product, ai-coding, tools]
aliases: [Vibe coding, Vibe-coding, Agentic coding, Building with AI coding agents]
created: 2026-09-26
updated: 2026-09-27
sources: [2026-09-26-resume, 2026-09-26-ponytail, 2026-09-27-gstack]
status: stub
---

# AI-Assisted Development

Building software by writing specs and directing **AI coding agents** instead of
writing all the code by hand. The human's work shifts to discovery, specification,
scoping, QA and output evaluation. This is how you built 12 published apps and
several web/SaaS tools ([[2026-09-26-resume]]).

## Your workflow (from the resume)
Discovery → spec writing → build with AI coding agents → QA → release. Along the way
you turn "ambiguous ideas into agent-ready specs" ([[2026-09-26-resume]]).
Tools: [[claude-code|Claude Code]], Antigravity, [[n8n]] ([[2026-09-26-resume]]).

## Key insight
> [!tip] Insight
> The resume frames solo AI-assisted building as "the same judgment a PM exercises
> with an engineering team, minus the team" ([[2026-09-26-resume]]). So skill with
> AI agents doubles as practice in product management.

## Risk: agents over-build
AI coding agents tend to add dependencies, wrappers and abstractions the task doesn't
need. [[ponytail|Ponytail]] guards against this with a YAGNI → stdlib → native ladder
and reports about 54% less code at equal safety ([[2026-09-26-ponytail]]). See
[[yagni]].

## Managing several agents
The bottleneck moves from writing code to **process and review**. [[gstack]] gives every agent the same Think → Plan → Build → Review → Test → Ship → Reflect sprint, which its author says is what makes 10–15 parallel sessions workable ([[2026-09-27-gstack]]). Your plan: [[agent-management-plan]].

## Connections
- [[ai-product-development]]
- [[physician-technologist]]
- [[llm-wiki]] — another way of working through agents
- [[ponytail]] — playbook for keeping agent output minimal (not adopted)
- [[gstack]] — sprint process for agents (trialling)
- [[agent-harness]] — what the agents run inside

## Sources
- [[2026-09-26-resume]]
- [[2026-09-26-ponytail]]
- [[2026-09-27-gstack]]
