# Stage: debug — no fix without a root cause

Adapted from gstack `/investigate`. **Iron law: no fixes without investigating
the root cause first.**

## Steps
1. **Reproduce.** Get exact steps, input, environment and the error text or stack
   trace. Write a failing test or a repro script if you can.
2. **Freeze scope.** Edit only files in the module under investigation until the
   cause is known.
3. **Trace the data flow** from input to failure. Read, don't skim. Check recent
   changes with `git log -p -- <files>` or `git bisect` for "it was working
   yesterday".
4. **Hypothesize → test**, one hypothesis at a time. Record each: what you
   expected, what happened.
5. **Fix at the root**, in the shared function every caller routes through (grep
   the callers first).
6. **Prove it:** the failing test now passes; run the full verify command.
7. **Three strikes:** after 3 failed fix attempts, stop. Summarize what you know
   and ask the user before trying more.

## Artifact: `docs/fsd/debug/<date>-<slug>.md`
Symptom · repro · root cause · fix (commit) · regression test · how to prevent it.

## Handoff
"Root cause: … Fixed in <commit> with regression test <name>. Next: `review`."
