---
title: "Cost: Claude Code subscription vs running your own harness"
type: synthesis
question: What is a harness, and what would it cost to manage my agents with a separate harness instead of Claude Code?
tags: [agents, pricing, ai-product]
aliases: [Harness cost, Agent cost comparison]
created: 2026-09-27
updated: 2026-09-27
sources: [2026-09-27-claude-pricing, 2026-09-27-gstack]
status: active
---

# Cost: Claude Code subscription vs running your own harness

**Question:** What is a harness, and what would it cost to manage my agents with a
separate harness instead of Claude Code?

> [!note] User view
> **2026-09-27:** Decided to skip a separate harness for now and stay on Claude Code, using your own [[full-stack-dev]] skill.

## Answer
For your own building work, **stay on Claude Code with a subscription and add
[[gstack]] on top**. It costs nothing beyond the plan, and Anthropic maintains the
harness. A separate harness (Claude Agent SDK, Managed Agents, or your own loop) is
**billed per token through the API**. For a heavy solo builder that plausibly comes
to **roughly $300–700+ per month of model usage**, plus hosting and your maintenance
time. It pays off only when the agent is *part of a product* or has to run
unattended *(inference; worked numbers below)*.

## What a harness is
See [[agent-harness]]. In short, it's the loop, tools, context and permissions around
the model. Claude Code *is* a harness. [[gstack]] is a set of instructions *inside*
it, not a harness itself ([[2026-09-27-gstack]]).

## Reasoning & evidence
**API prices** ([[2026-09-27-claude-pricing]]), per million tokens:

| Model | Input | Cached read (≈0.1×) | Cache write (1.25×) | Output |
|---|---|---|---|---|
| Opus 5 | $5 | $0.50 | $6.25 | $25 |
| Opus 5.5 | $4 | $0.20 | $5.00 | $20 |
| Sonnet 5 | $2 | $0.20 | $2.50 | $10 |
| Haiku 4.5 | $1 | $0.10 | $1.25 | $5 |

**One hour of agentic coding: a worked estimate** *(inference; assumptions: 60
model turns, about 80K tokens of context per turn, 90% served from cache, 150K output
tokens)*:

| Model | Cached reads (4.32M) | New input (0.48M, written to cache) | Output (0.15M) | **≈ per hour** |
|---|---|---|---|---|
| Opus 5 | $2.16 | $3.00 | $3.75 | **≈ $8.90** |
| Opus 5.5 | $0.86 | $2.40 | $3.00 | **≈ $6.30** |
| Sonnet 5 | $0.86 | $1.20 | $1.50 | **≈ $3.60** |

At **80 hours a month** (4 h/day × 20 days): Opus 5 ≈ $710, Opus 5.5 ≈ $500,
Sonnet 5 ≈ $290. **Parallel agents multiply this**: three lanes means about 3× the
cost *(inference)*.

**gstack's overhead on the API** *(inference from [[2026-09-27-gstack]] measurements)*:
about 7K always-on tokens per turn, cached, ≈ $0.21/hour on Opus 5. Plus each skill
you invoke (3K–51K tokens) written to cache once, ≈ $0.02–$0.32 on Opus 5. Small
next to the work itself.

**Hidden costs of your own harness** *(inference)*:
- Hosting: a server or container for the loop and tools.
- Engineering: permissions, sandboxing, retries, context management, logging. Claude
  Code already does all of this.
- Keeping up with model changes. The reference notes several breaking API changes
  between model generations ([[2026-09-27-claude-pricing]]).

## Decision table

| Situation | Best choice |
|---|---|
| You building your apps interactively | **Claude Code on a subscription, plus gstack** |
| Running several of your own agents in parallel | Claude Code sessions (worktrees, cloud sessions, or an orchestrator like Conductor) on the subscription, within its usage limits |
| An AI feature inside your product (e.g. a MediQ assistant) | **API** (Tool Runner or manual loop). Pay per token and design for caching and a low effort setting |
| Unattended or scheduled agents (nightly checks, reports) | **Managed Agents** or [[n8n]] plus API calls |
| Need full control or compliance over where data runs | Claude Agent SDK on your own infrastructure |

## Caveats
- **Subscription plan prices and usage limits aren't in the vault's sources.** Check
  the current Claude pricing page. As background, the top individual plans have
  historically cost well under the ~$300–700/month API-equivalent above
  *(background; verify)*.
- The hourly estimate depends heavily on context size and cache hit rate. Measure
  your own with `usage` data before deciding.
- Subscriptions have usage limits; heavy parallel use can hit them.

## Sources
- [[2026-09-27-claude-pricing]]
- [[2026-09-27-gstack]]
