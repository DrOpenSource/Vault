---
title: "Claude API pricing and agent-building options"
type: source
kind: data
raw: raw/2026-09-27-claude-pricing.md
author: Anthropic
published: 2026-06-24
url: https://docs.claude.com
tags: [ai-product, pricing, agents]
aliases: [Claude pricing]
created: 2026-09-27
updated: 2026-09-27
sources: []
status: active
---

# Claude API pricing and agent-building options

> [raw source](../../raw/2026-09-27-claude-pricing.md) · Anthropic · reference data
> (price table cached 2026-06-24; check the live pricing page before relying on it)

## TL;DR
API prices per million tokens: **Opus 5 $5 in / $25 out**, **Opus 5.5 $4 / $20**,
**Sonnet 5 $2 / $10**, **Haiku 4.5 $1 / $5**, **Fable 5.1 $10 / $50**. Cached input
costs about 0.1× (writes 1.25×), and batch jobs cost 50%. There are four ways to build
an agent, which differ in who supplies the **harness** and who hosts it.

## Key takeaways
1. Output tokens cost 5× input tokens on every model, so verbose agents are expensive.
2. Caching cuts repeated context (system prompt, skills, codebase) to about 10% of
   the input price after the first write.
3. **Four agent options:**
   - Manual loop: you build and host everything.
   - Tool Runner: the SDK runs the loop; you host it.
   - **Claude Agent SDK**: Claude Code's harness as a library; you host it.
   - **Managed Agents**: Anthropic runs the loop and hosts the sandbox.
4. The effort setting (`low` to `max`) trades thoroughness against tokens. Use `low`
   for subagents and simple tasks. Judge "cost per completed task", not per request.

## Notable claims
- "Two independent questions separate them: who supplies the harness ... and who
  supplies the deployment."
- The Claude Agent SDK "is Claude Code packaged as a library."

## Entities & concepts touched
- [[agent-harness]], [[harness-cost-comparison]], [[claude-code]]

## Open questions
- Subscription plan prices and usage limits are not in this source. Add them from
  the pricing page if you want exact break-even numbers.
- Managed Agents runtime/container charges are not in this source.
