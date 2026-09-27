---
title: "Plan: managing my Claude agents better"
type: synthesis
question: How should I set up and manage my Claude coding agents so they are more productive and easier to control?
tags: [agents, productivity, claude-code, plan]
aliases: [Agent operating plan, Agent management plan]
created: 2026-09-27
updated: 2026-09-27
sources: [2026-09-27-gstack, 2026-09-27-claude-pricing, 2026-09-26-resume]
status: active
---

# Plan: managing my Claude agents better

**Question:** How should I set up and manage my Claude coding agents so they are more
productive and easier to control?

## Answer
Give every agent the **same process** ([[gstack]]'s sprint), **one lane each**, and
**grow the number of lanes only as fast as you can review their output**. Run it all
on [[claude-code|Claude Code]] with your subscription; don't build a separate harness
([[harness-cost-comparison]]). Log weekly retros here in the vault so the system
learns *(inference, built on [[2026-09-27-gstack]])*.

## The plan

### Phase 0: Set up (this week)
1. Install your **[[full-stack-dev|Full-Stack Dev]]** skill (`skills/full-stack-dev/setup/install.sh --global`,
   then `--project <repo> --with-settings` per app). It replaces installing all of
   gstack. ~~Install gstack locally with prefixed commands~~ — superseded by your decision
   of 2026-09-27.
2. Add a standard block to each app's `CLAUDE.md`:
   - **What the app is**, its users, and its clinical guideline sources.
   - **Fixed clinical rules** (thresholds, alerts, dosing), each needing a test.
   - **Verify command** (e.g. `./gradlew test` or `npm test`), which agents must pass
     before finishing.
   - **Out of scope:** "no new dependencies or features beyond the spec without
     asking."
3. The installer creates a **lane board** in each project (`docs/fsd/lanes.md`);
   `/full-stack-dev status` prints it. Keep the cross-project summary below.

### Phase 1: One lane, full process (weeks 1–2)
Pick **one app** (suggestion: [[saathi|Saathi]], since it's a web app and every
gstack skill works on it). Run every change through:
`/full-stack-dev think` or `spec` → `plan` → `build` → `review` → `test` → `ship`.
Run `/full-stack-dev retro` on Friday and paste its export block here to ingest it.
**Measure:** changes shipped, bugs found after release, and how often you hit
subscription limits.

### Phase 2: Parallel lanes (weeks 3–4)
- Add a **second, then a third lane**, one app or feature each, in separate git
  worktrees or separate cloud sessions. gstack's author runs 10–15, but only with a
  strict process ([[2026-09-27-gstack]]). **Your limit is your review time, not the
  agents.**
- A lane runs by itself until it needs a *decision*. You review at the plan gate
  (after `/autoplan`) and the ship gate (after `/review`), not in between.

### Phase 3: Automate the routine (month 2)
- Recurring checks (dependency updates, weekly retro summaries) go to scheduled
  Claude Code sessions or [[n8n]], which you already know
  ([[2026-09-26-resume]]).
- Consider API or Managed Agents **only** for agents inside your products
  ([[harness-cost-comparison]]).

## Operating rules
| Rule | Why |
|---|---|
| **No spec, no build.** Every lane starts from `/spec` or an approved plan | Agents drift without a target *(inference)* |
| **Limit open lanes to what you can review** (start at 3) | Parallel output you can't review becomes risk *(inference)* |
| **Two human gates:** plan and ship | You decide scope and release; agents do the rest ([[2026-09-27-gstack]]) |
| **Ask-before rules on destructive commands** (`--with-settings`) | Skill rule 7 plus Claude Code permission rules; adapted from gstack's `/careful` ([[2026-09-27-gstack]]) |
| **`/clear` between stages** | The `docs/fsd/` artifacts carry context forward; a fresh context keeps quality up *(inference)* |
| **Right-size effort:** high for planning and review, lower for routine edits | Effort trades thoroughness against tokens and limits ([[2026-09-27-claude-pricing]]) |
| **Friday `/retro` → vault** | Your agent workflow improves from evidence, not memory |

## Lane board
*Update this table as lanes open and close.*

| Lane | App / feature | Stage | Next human decision | Opened |
|---|---|---|---|---|
| 1 | *(pick: Saathi suggested)* | — | Choose the first change | — |
| 2 | — | — | — | — |
| 3 | — | — | — | — |

## Caveats
- This is a starting plan built from one source (gstack) and your resume; adjust it
  after the first two retros.
- Browser-based QA doesn't cover native Android; your Android apps need your
  existing device or emulator testing ([[gstack]]).

## Tooling
- [[full-stack-dev]] — the skill that puts this plan into practice

## Sources
- [[2026-09-27-gstack]]
- [[2026-09-27-claude-pricing]]
- [[2026-09-26-resume]]
