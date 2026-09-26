---
title: YAGNI
type: concept
tags: [software-engineering, ai-coding]
aliases: [You aren't gonna need it, Over-engineering, Minimal code]
created: 2026-09-26
updated: 2026-09-26
sources: [2026-09-26-ponytail]
status: stub
---

# YAGNI (You Aren't Gonna Need It)

The principle of not building something until there is a real, present need for it.
Speculative features, one-implementation abstractions and scaffolding "for later"
cost code, bugs and maintenance without paying off ([[2026-09-26-ponytail]]). The
term comes from Extreme Programming *(background)*.

## In AI-assisted development
AI coding agents tend to over-build: they add a library, a wrapper and a stylesheet
where a native `<input type="date">` would do. [[ponytail|Ponytail]] makes YAGNI the
first rung of its ladder and reports cuts of up to 94% on such tasks
([[2026-09-26-ponytail]]).

## Limits
YAGNI never applies to safety: validation at trust boundaries, data-loss handling,
security and accessibility stay in ([[2026-09-26-ponytail]]). In clinical software,
guideline logic and alerts belong on that list too *(inference)*.

## Connections
- [[ponytail]] — puts YAGNI into practice for agents
- [[ai-assisted-development]]
- [[maintenance-burden]] — code that isn't written doesn't need maintaining *(inference)*

## Sources
- [[2026-09-26-ponytail]]
