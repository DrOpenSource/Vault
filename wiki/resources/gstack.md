---
title: gstack
type: resource
resource_kind: repo
url: https://github.com/garrytan/gstack
version: v1.91.2.0
checked: 2026-09-27
install_status: not-installed
decision: condensed into full-stack-dev (2026-09-27)
tags: [ai-coding, agents, claude-code, playbook]
aliases: [Garry's Stack, gstack skills]
created: 2026-09-27
updated: 2026-09-27
sources: [2026-09-27-gstack, 2026-09-27-claude-pricing]
status: active
---

# gstack — playbook

> [!note] User view
> **2026-09-27:** Rather than install all of gstack, you had its method condensed into your own skill, [[full-stack-dev|Full-Stack Dev]], which you can install in any project. This page stays as the reference for the original.

> Garry Tan's free skill pack that turns [[claude-code|Claude Code]] into a virtual
> engineering team running one sprint process. [GitHub](https://github.com/garrytan/gstack)
> · v1.91.2.0 · MIT ([[2026-09-27-gstack]]).
> **Status:** tried in this vault's cloud session on 2026-09-27; not yet installed on
> your own machine.

## What it is
About 55 Markdown **skills** (slash commands) plus helper tools. They are *not* a
separate [[agent-harness]]: they run inside Claude Code and tell it how to behave at
each stage ([[2026-09-27-gstack]]).

```
Think → Plan → Build → Review → Test → Ship → Reflect
/office-hours → /autoplan → (build) → /review → /qa → /ship → /retro
```

Each step writes something the next step reads (design doc → test plan → review
log), so nothing falls through the cracks ([[2026-09-27-gstack]]).

## When to use it / when not
**Use it for:**
- Turning a vague idea into a spec and plan before any code (`/office-hours`,
  `/spec`, `/autoplan`). This fits your spec-first way of building *(inference)*.
- Running several agents in parallel. The shared process keeps them from creating
  chaos ([[2026-09-27-gstack]]).
- Review, QA and release discipline you'd otherwise skip when working solo.

**Skip or trim for:**
- **Native Android work.** `/qa`, `/design-review`, `/benchmark` and `/canary` drive
  a web browser, and the device QA tools are iOS-only ([[2026-09-27-gstack]]). For
  [[mediq|MediQ]] and [[grow-baby-grow|Grow Baby Grow]], use the planning, review,
  ship and retro skills. For [[saathi|Saathi]] (web) and your product sites, the
  browser skills apply.
- Quick fixes. The author himself says "simple — no gstack needed"
  ([[2026-09-27-gstack]]).
- Maintaining this vault. It's a knowledge base, not a code project.

## Setup
On your own machine, paste into Claude Code ([[2026-09-27-gstack]]):
```
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup
```
Requires Git and **Bun**; on Windows also Node.

Recommended settings for you *(inference)*:
- `./setup --prefix`: commands become `/gstack-qa`, `/gstack-review` and so on, so
  they don't clash with other skills (Claude Code already has a built-in
  `/code-review`).
- Answer **no** to telemetry (it's off by default anyway), or run
  `gstack-config set telemetry off`.
- Skip the browser download if you don't need web QA yet:
  `GSTACK_SKIP_PLAYWRIGHT=1 ./setup`.

## How to use it best (your workflow)
Start with **these 10 skills only** *(inference)*. The rest are specialised (iOS,
design generation that needs OpenAI, GBrain, deploy automation).

| Your stage | Skill | Use |
|---|---|---|
| Idea → problem | `/office-hours` | Six forcing questions; pushes back on your framing. Good for new health-app ideas |
| Problem → spec | `/spec` | Five-phase spec with a quality gate; matches your "agent-ready specs" habit |
| Spec → reviewed plan | `/autoplan` | CEO → design → eng review in one command; only taste decisions come to you |
| Build | (plain Claude Code) | Implement the approved plan |
| Before merge | `/review` | Finds bugs that pass CI; auto-fixes obvious ones |
| Web apps only | `/qa <url>` | Real-browser testing plus regression tests (Saathi, sites) |
| Release | `/ship` | Tests, coverage audit, changelog, PR |
| Debugging | `/investigate` | Root cause first; stops after 3 failed fixes |
| Risky work | `/guard` | Destructive-command warnings plus edits limited to one folder |
| Weekly | `/retro` | Shipping streaks, test health; paste it here to ingest it into the vault |

> [!warning] Clinical safety rule
> gstack's "Boil the Ocean" ethos pushes for completeness, which is good for clinical
> logic (tests, edge cases). The risk is scope creep in features
> ([[2026-09-27-gstack]]). In each health app's `CLAUDE.md`, state which clinical
> rules are fixed (guideline thresholds, danger-sign alerts, dosing) and that each
> needs a test. Then run `/review` against them *(inference)*.

For managing several agents at once, see [[agent-management-plan]].

## Commands / reference
- Plan-stage reviews: `/plan-ceo-review` (4 scope modes), `/plan-eng-review`,
  `/plan-design-review`, `/plan-devex-review`.
- Memory: `/learn`, `/context-save`, `/context-restore`.
- Safety: `/careful`, `/freeze <dir>`, `/guard`, `/unfreeze`.
- Upkeep: `/gstack-upgrade`; uninstall with `~/.claude/skills/gstack/bin/gstack-uninstall`,
  then delete the `## gstack` sections from your `CLAUDE.md` files.
- Token audit: `~/.claude/skills/gstack/bin/gstack-context-bill`.
- A 2KB "digest" of its rules is available for other agents without installing
  (`agents-digest/gstack-AGENTS.md`).

## Cost (measured in the trial)
- **Always-on:** about 7K tokens of skill descriptions in every session
  ([[2026-09-27-gstack]]). If cached on Opus 5 that's roughly $0.0035 per turn;
  uncached about $0.035 per turn (*inference* from [[2026-09-27-claude-pricing]]).
- **Per skill used:** 3K–51K tokens loaded (for example `/ship` about 51K). On a
  subscription this uses up your usage limit and context window rather than dollars.
- gstack itself is free. Optional extras cost money: `/codex` needs an OpenAI
  Codex login; `/design-shotgun` uses OpenAI image generation
  ([[2026-09-27-gstack]]). Full comparison: [[harness-cost-comparison]].

## Pitfalls & caveats
- **Context load:** chaining `/autoplan` (which reads several review skills) and
  `/ship` can put 100K+ tokens of instructions into one session. Use `/clear`
  between stages *(inference)*.
- **Productivity claims are self-reported** by the author, with a published
  methodology ([[2026-09-27-gstack]]).
- **It runs scripts.** Each skill starts with a shell "preamble"; setup can add hooks
  to `~/.claude/settings.json`. Read what `./setup` prints ([[2026-09-27-gstack]]).
- **Its philosophy is the opposite of [[ponytail|Ponytail]]** ("Boil the Ocean" vs
  [[yagni|YAGNI]]). You chose not to use Ponytail; gstack also includes its own
  reuse ladder (repo → stdlib → native → installed dependency)
  ([[2026-09-27-gstack]]).

## Connections
- [[full-stack-dev]] — your condensed version of it
- [[agent-management-plan]] — how gstack fits your agent operating plan
- [[harness-cost-comparison]] — subscription vs your own harness
- [[agent-harness]] — gstack is a layer on top of one
- [[ai-assisted-development]], [[claude-code]]

## Sources
- [[2026-09-27-gstack]]
- [[2026-09-27-claude-pricing]]
