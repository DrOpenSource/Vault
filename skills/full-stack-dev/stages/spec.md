# Stage: spec — a precise spec an agent can build from

Goal: turn a brief or a clear request into a spec that is complete enough that
another agent could build it without asking questions. Adapted from gstack
`/spec`.

## Steps

1. **Why.** Read the brief if one exists (`docs/fsd/briefs/`). Otherwise ask for
   the problem and the user in two sentences.
2. **Scope.** List what is **in** and, just as important, what is **out**.
   Confirm both with the user.
3. **Technical grounding, which means reading code.** Before writing the technical
   section, read the files the change will touch: entry points, data models,
   existing helpers (reuse ladder). Record the real file paths.
4. **Draft** using the template below. Every requirement must be testable: write
   acceptance criteria as Given / When / Then.
5. **Self-check gate.** Score the draft 0–10 on: unambiguous, testable, scoped,
   grounded in real code, and clinical rules explicit (health apps). Below 7 on
   any of these: fix it or ask the user, then re-score.
6. **Save and confirm.** Show the user the in/out scope and the acceptance
   criteria; get a "yes" before `plan`.

Never put secrets, API keys, patient data or real personal data into a spec.

## Artifact: `docs/fsd/specs/<slug>.md` (use `templates/spec.md`)

## Handoff
"Spec saved to `docs/fsd/specs/<slug>.md` (score N/10). Next: `plan`."
