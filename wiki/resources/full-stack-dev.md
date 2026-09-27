---
title: Full-Stack Dev (skill)
type: resource
resource_kind: skill
url: skills/full-stack-dev/
version: 1.0.0
checked: 2026-09-27
install_status: trialling
tags: [ai-coding, agents, claude-code, playbook, my-skills]
aliases: [full-stack-dev, FSD, /full-stack-dev]
created: 2026-09-27
updated: 2026-09-27
sources: [2026-09-27-gstack]
status: active
---

# Full-Stack Dev — playbook

> **Your own Claude Code skill**, kept in this vault at
> [`skills/full-stack-dev/`](../../skills/full-stack-dev/SKILL.md). It's a condensed
> adaptation of [[gstack]]'s sprint for one builder directing AI agents, with a
> clinical safety gate for health apps. MIT attribution is in `NOTICE.md`
> ([[2026-09-27-gstack]]).

## What it is
**One** skill with nine stages, loaded one at a time:

```
think → spec → plan → build → review → test → ship      (+ debug, retro, status)
/full-stack-dev think   …   /full-stack-dev ship
```

Each stage writes an artifact to the project's `docs/fsd/` folder (brief, spec,
plan, review, QA report, retro), and the next stage reads it. So work carries
across sessions and across parallel agents without re-explaining.

**Why a condensed version instead of full gstack** *(inference; token numbers from
[[2026-09-27-gstack]])*:

| | gstack | Full-Stack Dev |
|---|---|---|
| Skills in the always-on list | 55 (~7K tokens) | 1 (~160 tokens) |
| Loaded per use | 3K–51K tokens per skill | ~1.3K (main file) + ~0.3–0.6K (one stage file), measured |
| Needs Bun, a browser build, hooks | Yes | No: plain Markdown plus one shell installer |
| Android coverage | Web and iOS focus | Web **and** Android (Gradle, emulator) |
| Clinical rules | — | Built-in safety gate and a `## Clinical rules` block |

## When to use it / when not
- **Use it for** any feature, bug or release in your apps ([[mediq|MediQ]],
  [[grow-baby-grow|Grow Baby Grow]], [[saathi|Saathi]], new projects).
- **Skip stages** for trivial changes: go straight to `build` → `review`.
- **Not for** this vault. The vault runs on its own schema (`CLAUDE.md`).

## Setup
From a local clone of this vault:

```bash
# 1) Available in every project (copy). Add --link to symlink so `git pull` in the vault updates it.
skills/full-stack-dev/setup/install.sh --global

# 2) Once per project: adds the CLAUDE.md block, docs/fsd/lanes.md,
#    and (optional) "ask before destructive commands" permission rules.
skills/full-stack-dev/setup/install.sh --project ~/code/saathi --with-settings
```

Then open the project's `CLAUDE.md` and fill in the placeholders: **verify command**
and **clinical rules** (one line per rule, with its guideline source). Restart
Claude Code if `/full-stack-dev` doesn't appear straight away.

The installer is safe to re-run. It never overwrites a folder it didn't create,
adds the CLAUDE.md block only once, and backs up `.claude/settings.json` before
merging new rules into it. Tested 2026-09-27 on a scratch repo and as a global
install; the skill loaded in Claude Code.

## How to use it best (your workflow)
| Situation | Run |
|---|---|
| New app or feature idea | `/full-stack-dev think` (forcing questions, plus Q7: clinical basis and worst-case harm) |
| Idea is clear | `/full-stack-dev spec`, then `/full-stack-dev plan` → approve the decisions it lists |
| Build | `/full-stack-dev build` (branch, test-first for clinical rules, verify after each step) |
| Before merging | `/full-stack-dev review` → `/full-stack-dev test` |
| Release | `/full-stack-dev ship` (Android: versionCode, signed bundle checklist; it never touches signing keys) |
| Something broke | `/full-stack-dev debug` (root cause first, stops after 3 failed fixes) |
| Friday | `/full-stack-dev retro` → paste its export block here and say "ingest" |
| Several agents at once | One lane per agent in `docs/fsd/lanes.md`; `/full-stack-dev status` shows the board |

Use `/clear` between stages; the artifacts carry the context forward. This follows
your [[agent-management-plan]].

## Commands / reference
Files in `skills/full-stack-dev/`:
- `SKILL.md`: router, always-on rules, clinical safety gate, lane board
- `stages/*.md`: think, spec, plan, build, review, test, ship, debug, retro
- `templates/`: `project-CLAUDE.md`, `spec.md`, `lanes.md`
- `setup/install.sh`, `setup/settings.example.json` (ask-before rules for
  `rm -rf`, force-push, `reset --hard`, and similar; blocks reading `.env` and
  keystores)
- `NOTICE.md`: gstack MIT attribution

To change the skill, ask me here ("update Full-Stack Dev so…"). I'll edit
`skills/full-stack-dev/`, bump `version` above and log it.

## Pitfalls & caveats
- **It's instructions, not enforcement.** The agent can still skip a stage; the
  permission rules in `settings.example.json` are the only hard guard.
- **Keep secrets out of specs and artifacts.** `docs/fsd/` gets committed with
  your code.
- **The clinical gate relies on you listing the rules.** An empty
  `## Clinical rules` section means the agent only catches clinical code by
  keyword.
- **Symlink install (`--link`)** keeps it in sync with the vault but breaks if you
  move the vault. The discovery test passed with the copy install; the symlink
  variant wasn't separately confirmed.

## Connections
- [[gstack]] — the source it was condensed from
- [[agent-management-plan]] — the plan it puts into practice
- [[ai-assisted-development]], [[claude-code]], [[physician-technologist]]

## Sources
- [[2026-09-27-gstack]]
