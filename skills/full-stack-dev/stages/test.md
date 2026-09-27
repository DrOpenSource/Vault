# Stage: test — verify real behavior, fix what breaks, add regression tests

Adapted from gstack `/qa`, extended for Android.

## Steps

1. **Read the test matrix** in the plan and the acceptance criteria in the spec.
2. **Run the automated suite** (verify command) and report the results.
3. **Exercise the real app** against each acceptance criterion:
   - **Web:** run the dev server; use Playwright (or the browser tool available in
     this environment) to click through each flow; check the console for errors;
     test at mobile and desktop widths; check the empty, error and loading states.
   - **Android:** `./gradlew testDebugUnitTest` for JVM tests;
     `./gradlew connectedDebugAndroidTest` on an emulator or device for
     instrumented and UI tests. For manual checks, list the exact steps the user
     should tap through and what they should see.
   - **Clinical:** feed boundary values (just below, at, and just above each
     threshold) and confirm the output and alert against the cited guideline.
4. **For each bug found:** find the root cause (see `debug`), fix it, add a
   regression test that fails without the fix, commit it, and re-verify.
5. **Report-only mode:** if the user says "report only", list the bugs with repro
   steps and change nothing.

## Artifact: `docs/fsd/qa/<date>-<slug>.md`

```markdown
# QA: <slug> — <date>
| Criterion | Result | Evidence (test name / screenshot / steps) |
## Bugs found → fixed (commit) + regression test
## Manual checks for the user (Android)
## Not tested and why
```

## Handoff
"QA: N/M criteria pass, K bugs fixed with tests. Next: `ship`."
