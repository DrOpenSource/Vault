---
title: Agent Harness
type: concept
tags: [agents, ai-product, ai-coding]
aliases: [Harness, Agent loop, Agent scaffold]
created: 2026-09-27
updated: 2026-09-27
sources: [2026-09-27-claude-pricing, 2026-09-27-gstack]
status: active
---

# Agent Harness

The **software around a model** that turns it into an agent. It includes the agent
loop (call the model → run the tool it asks for → send back the result → repeat),
the tools themselves (file edit, shell, web), context management, permissions,
hooks, subagents and sessions. The model supplies the judgement; the harness
supplies the hands and the memory ([[2026-09-27-claude-pricing]]).

## Harness vs deployment
Two separate questions: **who supplies the harness** and **who hosts it**
([[2026-09-27-claude-pricing]]).

| Option | Harness from | Hosted by | Billing |
|---|---|---|---|
| **[[claude-code\|Claude Code]]** (what you use now) | Anthropic | Your machine or Claude's cloud | Subscription plan or API key *(background)* |
| Claude Agent SDK | Anthropic (Claude Code as a library) | **You** | API, per token *(inference)* |
| Managed Agents | Anthropic | **Anthropic** (per-session sandbox) | API tokens plus runtime *(inference; runtime price not in source)* |
| API Tool Runner / manual loop | You (SDK helper or hand-written) | **You** | API, per token |

## What sits on top of a harness
- **Skills / playbooks** such as [[gstack]] and [[ponytail]]. These are instructions
  loaded into a harness, not harnesses themselves ([[2026-09-27-gstack]]).
- **Orchestrators** that run many harness sessions in parallel, for example
  Conductor, which [[gstack]]'s author uses for 10–15 sessions
  ([[2026-09-27-gstack]]).

## Why it matters to you
For building your own apps, the harness is already built and maintained for you
(Claude Code). Building your own makes sense when an **agent is part of your
product**, for example an AI feature inside [[mediq|MediQ]], or when you need
control, compliance or scheduled runs *(inference)*. See [[harness-cost-comparison]].

## Connections
- [[harness-cost-comparison]], [[agent-management-plan]]
- [[ai-assisted-development]], [[ai-product-development]]

## Sources
- [[2026-09-27-claude-pricing]]
- [[2026-09-27-gstack]]
