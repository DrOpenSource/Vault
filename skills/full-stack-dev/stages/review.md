# Stage: review — find what CI misses, fix the obvious, ask about the rest

Adapted from gstack `/review` and its pre-landing checklist.

## Steps

1. **Get the diff** against the base branch: `git diff origin/<base>...HEAD`
   (fetch first). Read the plan and spec too.
2. **Scope drift check.** Compare the diff with the plan: flag anything built that
   wasn't planned, and anything planned that's missing.
3. **Pass 1: critical** (read code outside the diff where needed):
   - **Data safety:** string-built SQL, check-then-write races, find-or-create
     without a unique index, bypassed validations.
   - **Trust boundaries:** unvalidated user input; LLM output stored, fetched or
     executed without validation; unsafe HTML rendering; shell commands built
     from strings.
   - **Secrets:** keys or tokens in code, logs or config.
   - **Completeness:** a new enum, status or type value that isn't handled by
     every consumer (grep the siblings and read each match).
   - **Clinical (health apps):** thresholds, units, rounding and boundary operators
     match the cited guideline; every clinical rule has a test; alert text is
     accurate and non-diagnostic.
4. **Pass 2: informational.** Error and empty states, accessibility, performance
   traps (N+1 queries, re-renders, main-thread work on Android), dead code,
   unrequested abstractions, tests that don't actually assert behavior.
5. **Fix first.** Apply obvious mechanical fixes yourself and commit them. Batch
   genuinely ambiguous items into one question for the user.
6. **Calibrate.** Report only issues you verified in the code. For each one, cite
   `file:line`. No "looks good overall" filler.

## Artifact: `docs/fsd/reviews/<date>-<slug>.md`

```
Review: N issues (X critical, Y informational)
AUTO-FIXED:
- [file:line] problem → fix
NEEDS INPUT:
- [file:line] problem — recommended fix
SCOPE: on plan | drift: …
```

## Handoff
"Review done: N fixed, M need you. Next: `test` (or `ship` if tests already cover
it)."
