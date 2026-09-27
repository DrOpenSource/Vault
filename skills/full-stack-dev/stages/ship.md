# Stage: ship — release safely

Adapted from gstack `/ship`.

## Pre-flight (stop if any fails)
- On a feature branch, not the default branch.
- `review` done with no open critical items; `test` report exists or tests cover
  the change.
- Clinical rules touched → each has a passing test that cites its guideline.
- No secrets in the diff (`git diff origin/<base>...HEAD | grep -iE
  "api[_-]?key|secret|token|password"` and review any hits).

## Steps
1. **Sync:** fetch and merge (or rebase, per the repo's convention) the base branch,
   then re-run the verify command.
2. **Coverage check:** list the changed files that have no test touching them.
   Add tests or state why not.
3. **Version and notes:** bump the version as the project does it (web:
   `package.json`; Android: `versionCode` + `versionName` in `build.gradle(.kts)`).
   Add a CHANGELOG entry in user-facing language.
4. **Docs:** update README or other docs the change made stale.
5. **Push and open a PR** with: summary, link to the spec and plan, test evidence,
   and risks and rollback.
6. **Android release (only when the user asks):** build the signed bundle
   (`./gradlew bundleRelease`) and give the user the upload checklist for Play
   Console: staged rollout %, release notes, and data-safety form changes if any.
   Never handle signing keys yourself.

## Handoff
"PR opened: <link>. Version <x>. Rollback: <how>. Next: `retro` at week's end."
