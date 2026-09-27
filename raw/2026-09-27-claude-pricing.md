---
title: "Claude API pricing and agent-building options (reference excerpt)"
url: https://docs.claude.com (via the claude-api reference skill bundled with Claude Code 2.1.283; price table cached 2026-06-24)
author: Anthropic
captured: 2026-09-27
note: Excerpts copied from the reference. Prices are first-party API list prices per million tokens (MTok). Check the live pricing page before relying on them. Subscription plan prices (Pro/Max) are NOT in this source.
---

## Current Models (cached: 2026-06-24)

| Model             | Model ID            | Context        | Input $/1M | Output $/1M |
| ----------------- | ------------------- | -------------- | ---------- | ----------- |
| Claude Fable 5.1    | `claude-fable-5-1`      | 1M             | $10.00     | $50.00      |
| Claude Fable 5 | `claude-fable-5` | 1M             | $10.00     | $50.00      |
| Claude Opus 5.5 (launching) | `claude-opus-5-5` | 1M | $4.00 | $20.00 |
| Claude Opus 5     | `claude-opus-5`       | 1M             | $5.00      | $25.00      |
| Claude Opus 4.8 | `claude-opus-4-8`  | 1M             | $5.00      | $25.00      |
| Claude Sonnet 5   | `claude-sonnet-5`   | 1M             | $2.00      | $10.00      |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 1M             | $3.00      | $15.00      |
| Claude Haiku 4.5  | `claude-haiku-4-5`  | 200K           | $1.00      | $5.00       |

## Prompt caching economics

"Cache reads cost ~0.1× base input price - 0.025× on Claude Fable 5.1 ($0.25/MTok) and 0.05× on Claude Opus 5.5 ($0.20/MTok) ... Cache writes cost 1.25× for 5-minute TTL, 2× for 1-hour TTL."

## Batch processing

"Batch processing (non-latency-sensitive; runs asynchronously at 50% cost)"

## Building an Agent: Four Approaches

"Two independent questions separate them: who supplies the harness (the agent loop + context management) and who supplies the deployment (the infra the agent runs on)."

| # | Approach | You write | Harness & deployment | Tools available |
|---|----------|-----------|----------------------|-----------------|
| 1 | Claude API - manual loop | The `while stop_reason == "tool_use"` loop yourself | You build the harness; you host | Only tools you define |
| 2 | Claude API - Tool Runner | Just the tool functions | SDK supplies the loop (harness only); you host | Only tools you define |
| 3 | Managed Agents (REST, beta) | Agent config + your tool results | Anthropic supplies the harness and hosts a per-session sandbox (harness + deployment) | Anthropic-hosted sandbox (bash, files, code exec) + Skills/MCP + your tools |
| 4 | Claude Agent SDK (separate product) | A prompt + options | SDK supplies the Claude Code harness + built-in tools (harness only); you host | Built-in Read/Write/Edit/Bash/Glob/Grep/WebSearch/WebFetch + MCP + subagents |

"Claude Agent SDK ... is Claude Code packaged as a library. It ships built-in tools (file read/write/edit, bash, grep, web search), the full agent loop, context management, hooks, subagents, permissions, and sessions."

"Managed Agents is the right choice when you want Anthropic to run the agent loop *and* host the container where tools execute."

Effort levels: "`low`/`medium`/`high`/`xhigh`/`max` ... use `low` for subagents or simple tasks ... Judge cost per completed task, not per request."
