# Stage: plan — review scope, architecture and tests before code

Goal: a reviewed implementation plan. Condenses gstack's CEO, eng and design
plan reviews (`/autoplan`) into one pass. Only **taste decisions** go to the user.

## Steps

1. **Read the spec** (`docs/fsd/specs/<slug>.md`) and the code it names.
2. **Scope challenge (product lens).** Pick one mode and say why:
   - *Reduce:* cut to the smallest version that meets the acceptance criteria.
   - *Hold:* the scope is right.
   - *Expand:* only if a small addition makes the result much better for the user.
     This needs the user's approval.
3. **Architecture (engineering lens).**
   - Data flow and state: show it as a short ASCII or Mermaid diagram.
   - Files to change or create, with the reason for each.
   - Reuse ladder: what existing code, stdlib or platform feature covers each part.
   - Failure modes: network loss, bad input, empty states, permissions, offline
     (mobile), concurrent edits.
   - Security: auth, input validation at trust boundaries, secrets, and any LLM
     output treated as untrusted (validate before storing or acting on it).
   - Reversibility: feature flag or easy rollback for risky changes.
4. **UX lens (if there's a UI).** Rate 0–10: clarity, hierarchy, empty/error/loading
   states, accessibility (contrast, labels, touch targets). For anything below 7,
   say what a 10 looks like and change the plan to get there.
5. **Test plan.** A matrix of each acceptance criterion against unit, integration
   and end-to-end tests. Every clinical rule gets a unit test with its guideline
   cited, including boundary values.
6. **Decisions.** Resolve mechanical questions yourself using the always-on rules.
   List only genuine taste or product decisions for the user, each with your
   recommendation.
7. **Get approval** before `build`.

## Artifact: `docs/fsd/plans/<slug>.md`

```markdown
# Plan: <name>   (spec: docs/fsd/specs/<slug>.md)
## Scope mode: reduce | hold | expand — why
## Architecture (diagram + files to touch)
## Reuse (what existing code/stdlib/platform covers)
## Failure modes & security
## UX notes (if UI)
## Test matrix
## Clinical rules touched (health apps) → tests
## Decisions for the user (with recommendations)
## Build order (small, verifiable steps)
```

## Handoff
"Plan saved. N decisions need you: … Once approved, next: `build`."
