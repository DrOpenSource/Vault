---
title: Ponytail
type: resource
resource_kind: plugin
url: https://github.com/dietrichgebert/ponytail
version: v4.10.0
checked: 2026-09-26
install_status: not-installed
decision: not using (2026-09-26)
tags: [ai-coding, tools, ai-product, playbook]
aliases: [ponytail plugin, lazy senior dev, /ponytail]
created: 2026-09-26
updated: 2026-09-26
sources: [2026-09-26-ponytail]
status: active
---

# Ponytail — playbook

> [!note] User view
> **Decided not to use it (2026-09-26).** This page is kept for reference in case
> the question of AI agents over-building code comes up again.

> A plugin/skill that makes your AI coding agent build **the least code that
> actually works**, without cutting safety. [GitHub](https://github.com/dietrichgebert/ponytail)
> · v4.10.0 · MIT · works with 20 agents, including [[claude-code|Claude Code]] and
> Antigravity ([[2026-09-26-ponytail]]).

## What it is
A ruleset that runs inside your coding agent as a "lazy senior dev". Before writing
code, the agent climbs a **ladder** and stops at the first rung that works
([[2026-09-26-ponytail]]):

```
1. Does this need to exist?   → no: skip it (YAGNI)
2. Already in this codebase?  → reuse it
3. Stdlib does it?            → use it
4. Native platform feature?   → use it (<input type="date"> over a picker library)
5. Installed dependency?      → use it; never add one for a few lines
6. One line?                  → one line
7. Only then: the minimum that works
```

It **never** cuts input validation at trust boundaries, error handling that prevents
data loss, security, accessibility, or anything you explicitly asked for. It also
never skips reading and understanding the code first ([[2026-09-26-ponytail]]). See
[[yagni]].

**Claimed impact** (the author's own benchmark, 12 tasks on a FastAPI + React repo,
Haiku 4.5, n=4): about 54% less code (up to 94% where agents over-build), about 20%
cheaper, about 27% faster, and every safety guard kept ([[2026-09-26-ponytail]]).

## When to use it / when not
**Use it when:**
- Building features with AI agents, which tend to over-build: extra libraries,
  wrapper components, abstractions "for later". This fits your solo
  [[ai-assisted-development|AI-assisted building]] workflow directly *(inference)*.
- Cleaning up an existing app that has picked up bloat.
- Choosing libraries or dependencies.

**Don't use it for:**
- Non-coding work: prose, summaries, research, **maintaining this vault**. The skill
  excludes these itself ([[2026-09-26-ponytail]]).
- Terse chat. Ponytail governs *what gets built*, not *how the agent talks*. The
  author suggests pairing it with a separate plugin called Caveman for terse replies
  ([[2026-09-26-ponytail]]).

## Setup
**Claude Code.** Send these as **two separate prompts** ([[2026-09-26-ponytail]]):
```
/plugin marketplace add DietrichGebert/ponytail
```
```
/plugin install ponytail@ponytail
```
**Antigravity CLI:** `agy plugin install https://github.com/DietrichGebert/ponytail`

**Requirement:** `node` must be on your PATH for the always-on hooks. Without it, the
skills still work but won't switch on automatically ([[2026-09-26-ponytail]]).

**Default level:** `full`. Change it with `PONYTAIL_DEFAULT_MODE=lite|full|ultra|off`
or `~/.config/ponytail/config.json` ([[2026-09-26-ponytail]]).

## How to use it best (your workflow)
*These recommendations are tailored to how you build (solo, spec-first, health apps).
They are my suggestions, marked (inference) unless cited.*

| Stage of your lifecycle | Use | Why |
|---|---|---|
| **Spec writing** | Add "native and stdlib first, no new dependencies without justification" to your agent-ready specs | Ponytail enforces this during the build; stating it in the spec aligns the two *(inference)* |
| **Exploring or learning** | `/ponytail lite` | Builds what you ask, then names the lazier option in one line, so *you* decide and learn the trade-off ([[2026-09-26-ponytail]]) |
| **Normal feature build** | `full` (default) | Enforces the ladder; shortest diff ([[2026-09-26-ponytail]]) |
| **Before each release** | `/ponytail-review` on the diff | One line per finding plus `net: -N lines possible` ([[2026-09-26-ponytail]]) |
| **Cleaning up existing apps** | `/ponytail-audit` once per app, starting with the largest | Repo-wide list of what to cut, biggest first; applies nothing, so you choose ([[2026-09-26-ponytail]]) |
| **Refactoring an old codebase** | `/ponytail ultra` | Deletes before adding and challenges requirements ([[2026-09-26-ponytail]]) |
| **Monthly** | `/ponytail-debt` | Collects every `ponytail:` shortcut comment into a list, flagging any with no trigger to revisit ([[2026-09-26-ponytail]]) |

> [!warning] Clinical safety rule for health apps
> Ponytail's never-lazy list covers validation, security, data loss and accessibility.
> It does **not** mention clinical logic by name *(inference from
> [[2026-09-26-ponytail]])*. For [[mediq|MediQ]], [[grow-baby-grow|Grow Baby Grow]],
> [[saathi|Saathi]] and future health apps, add a line like this to the project's
> `CLAUDE.md`/`AGENTS.md`:
> *"Clinical logic is explicitly requested and never simplified: guideline
> thresholds, danger-sign alerts, growth centiles, unit conversions and dosing each
> keep a runnable check."*
> Ponytail treats explicitly requested behaviour as off-limits, and its own rule
> requires one runnable check for non-trivial logic ([[2026-09-26-ponytail]]).

**Other habits that work well** *(inference)*:
- Treat review and audit output as a **to-do list, not an auto-fix**. Check each cut
  against the spec before deleting.
- Run your normal correctness and security review **as well**. Ponytail's
  review/audit covers over-engineering only ([[2026-09-26-ponytail]]).
- Try a before/after on one feature: build it once without ponytail and once with
  `full`, and compare the diff sizes. That gives you your own evidence instead of
  relying on the author's benchmark.

## Commands / reference
| Command | What it does |
|---|---|
| `/ponytail [lite\|full\|ultra\|off]` | Set the level; with no argument, show the current level |
| `/ponytail-review` | Review the current diff for over-engineering and list what to delete |
| `/ponytail-audit` | The same, across the whole repo, ranked by size of cut |
| `/ponytail-debt` | List every `ponytail:` shortcut comment |
| `/ponytail-gain` | Show the benchmark scoreboard |
| `/ponytail-help` | Quick reference |
| "stop ponytail" / "normal mode" | Turn it off for the session |

Review tags: `delete:` · `stdlib:` · `native:` · `yagni:` · `shrink:`
([[2026-09-26-ponytail]]).

Shortcut comment convention: `# ponytail: <ceiling>, <upgrade path>`, e.g.
`# ponytail: global lock, per-account locks if throughput matters`
([[2026-09-26-ponytail]]).

**Uninstall:** run `node scripts/uninstall.js` **first** to remove leftover state
files, **then** `/plugin remove ponytail` ([[2026-09-26-ponytail]]).

## Pitfalls & caveats
- **Benchmark limits:** it is self-reported, used one model (Haiku 4.5) and n=4. The
  author says larger models may narrow or widen the gap, and that the safety tests
  show whether known guards are kept, not that the code is secure
  ([[2026-09-26-ponytail]]).
- **Reasoning models can cost more.** On a terse reasoning model, deliberating over
  the rungs can *raise* cost; the author saw this on GPT-5.5 ([[2026-09-26-ponytail]]).
- **It runs third-party code.** The plugin installs Node.js lifecycle hooks, which
  run on every prompt. Look through `hooks/` before installing on a machine that
  holds patient or sensitive data *(inference)*.
- **Subagents** get the ruleset too by default. To limit it, set
  `PONYTAIL_SUBAGENT_MATCHER` ([[2026-09-26-ponytail]]).
- **"Less code" is not the goal in itself.** The author says the rule is "write only
  what the task needs", not "fewest tokens" ([[2026-09-26-ponytail]]).

## Connections
- [[yagni]] — the principle behind the first rung
- [[ai-assisted-development]] — guards against AI agents over-building
- [[claude-code]] — main host; installs as a plugin
- [[gstack]] — alternative skill pack with the opposite philosophy ("Boil the Ocean")
- [[physician-technologist]] — the clinical safety rule above is where your
  clinical judgement comes in

## Sources
- [[2026-09-26-ponytail]]
