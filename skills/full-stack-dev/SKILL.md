---
name: full-stack-dev
description: >
  Full-Stack Dev: a spec-first sprint for building and shipping web and mobile
  apps with AI agents — think, spec, plan, build, review, test, ship, debug,
  retro — with a clinical-safety gate for health apps. Use when starting a
  feature or new app, writing a spec, reviewing a plan or diff, testing,
  releasing, debugging a bug, or running a weekly retro. Invoke with a stage
  name (e.g. "/full-stack-dev review") or describe the task and the right stage
  is chosen. Not for non-code work (docs-only, research, notes).
argument-hint: "[think|spec|plan|build|review|test|ship|debug|retro|status]"
---

# Full-Stack Dev

A compact engineering process for one builder directing AI agents. It is
distilled from Garry Tan's gstack (MIT; see `NOTICE.md`) and adapted for a
physician-builder who ships web and Android apps, some of them clinical.

## How to use this skill

1. **Pick the stage.** If the user named one (argument), use it. Otherwise infer
   it from the request with the table below and say which stage you chose in one
   line.
2. **Read that stage's file** from this skill's directory:
   `stages/<stage>.md`. Follow it fully. Do not work from memory.
3. **Write the stage's artifact** under `docs/fsd/` in the project (create the
   folder if missing). Each stage reads the previous stage's artifact, so work
   carries forward between sessions and agents.
4. **End with the handoff line** the stage file specifies: what was produced,
   and the next stage.

| Stage | Use when | Artifact |
|---|---|---|
| `think` | New idea or unclear problem | `docs/fsd/briefs/<slug>.md` |
| `spec` | Idea is clear; need a buildable spec | `docs/fsd/specs/<slug>.md` |
| `plan` | Spec exists; need architecture, tests and scope checked before code | `docs/fsd/plans/<slug>.md` |
| `build` | Plan approved; implement it | code + tests |
| `review` | Diff ready; before merge | `docs/fsd/reviews/<date>-<slug>.md` |
| `test` | Verify behavior end to end (web or Android) | `docs/fsd/qa/<date>-<slug>.md` |
| `ship` | Reviewed and tested; release it | PR / release notes |
| `debug` | Bug, crash, "it was working yesterday" | root-cause note in `docs/fsd/debug/` |
| `retro` | Weekly, or after a release | `docs/fsd/retros/<date>.md` |
| `status` | "Where are we?" | Print the lane board (below); no file |

Small, obvious changes (typo, copy tweak, one-line fix) skip straight to
`build` then `review`. Say so.

## Always-on rules (every stage)

1. **Read before you decide.** Read the code the change touches and trace the
   real flow before choosing an approach. Never guess at a file, field or API
   that you can check.
2. **Reuse ladder.** Before writing new code, stop at the first rung that holds:
   (a) something already in this repo → (b) the language's standard library →
   (c) a native platform feature → (d) an already-installed dependency. Never
   add a dependency for what a few lines cover. Then build the complete version
   of what remains.
3. **Complete within scope, strict about scope.** Inside the agreed scope, do
   the whole job: tests, edge cases, error paths. Outside it, add nothing;
   propose it as a follow-up instead.
4. **Root cause, not symptom.** A bug fix goes where every caller benefits.
5. **The user decides.** Recommend one option with the reason; ask before
   changing the user's stated direction, scope, or any clinical rule.
6. **Verify before "done".** Run the project's verify command (from
   `CLAUDE.md`, see `templates/project-CLAUDE.md`). If none exists, say so and
   propose one. Never report success without showing the result.
7. **Destructive commands need a yes.** `rm -rf` outside build/cache folders,
   `git push --force`, `git reset --hard`, dropping tables, deleting cloud
   resources: stop and ask first, every time.
8. **Plain voice.** Direct and concrete: name the file, command and
   user-visible effect. Short paragraphs. End with what to do next.

## Clinical safety gate (health apps)

If the project's `CLAUDE.md` has a `## Clinical rules` section, or the code
touches dosing, thresholds, vitals, growth centiles, danger signs, triage or
alerts:

- Those rules are **fixed requirements**. Never simplify, reinterpret or "clean
  up" them without the user's explicit approval.
- Every clinical rule needs **a test that cites its guideline source** (for
  example `// WHO growth standard, weight-for-age, z < -2`).
- Units, rounding and boundary values (`<` vs `<=`) are checked explicitly in
  `plan`, `review` and `test`.
- User-facing clinical text must not diagnose or prescribe unless the spec says
  so, and must include the app's standard disclaimer if one exists.
- Flag anything clinically uncertain as **NEEDS CLINICAL REVIEW** for the user.
  Don't decide it yourself.

## Lane board (parallel agents)

When the user runs several agents at once, each works one **lane** (one app or
feature, its own branch or worktree). `docs/fsd/lanes.md` tracks them; see
`templates/lanes.md`. On `status`, print the board. When a stage finishes, update
that lane's row: stage, next human decision, date.

## Context hygiene

Stage files are loaded one at a time on purpose. After a stage finishes and its
artifact is written, suggest `/clear` before the next stage; the artifact carries
the context forward.
