# Stage: build — implement the approved plan

## Steps

1. **Load the plan** (`docs/fsd/plans/<slug>.md`). If there is no approved plan and
   the change isn't trivial, stop and suggest `spec` or `plan` first.
2. **Work on a branch** (or a worktree for a parallel lane). Never build directly on
   the default branch.
3. **Follow the build order** in small steps. For each step:
   - Write or update the test first where practical, especially for clinical rules.
   - Implement using the reuse ladder.
   - Run the verify command. Fix before moving on.
   - Commit with a clear message (one logical change per commit).
4. **Stay in scope.** If you find something outside the plan (a bug nearby, a
   refactor idea), note it under "Follow-ups" and don't do it now.
5. **Mark deliberate shortcuts** with a comment naming the limit and when to
   revisit: `// fsd: in-memory cache, move to DB if >1k users`.
6. **Finish** only when the verify command passes. Show the output.

## Platform notes
- **Web (JS/TS):** prefer native HTML/CSS features (`<input type="date">`,
  `<dialog>`, CSS grid) over libraries.
- **Android (Kotlin):** prefer Jetpack/AndroidX components already in the project;
  keep clinical logic in pure Kotlin classes (no Android dependencies) so it's
  unit-testable on the JVM.
- **Health Connect / sensors:** handle missing permissions, stale data and unit
  conversions explicitly; real devices drift, so leave calibration hooks.

## Handoff
"Built on branch `<branch>`: N commits, verify passing (`<command>`). Follow-ups:
… Next: `review`."
