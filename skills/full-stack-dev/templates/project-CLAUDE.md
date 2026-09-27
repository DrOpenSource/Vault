<!-- full-stack-dev: start -->
## Full-Stack Dev

This project uses the `full-stack-dev` skill. Stages: think → spec → plan →
build → review → test → ship (+ debug, retro, status). Artifacts live in
`docs/fsd/`.

### Project
- **What it is:** <one line — e.g. "Antenatal care companion web app">
- **Users:** <who, specifically>
- **Stack:** <e.g. Kotlin + Jetpack Compose / Next.js + Postgres>
- **Default branch:** main

### Verify command (agents must pass this before saying "done")
```
<e.g. ./gradlew testDebugUnitTest lint   |   npm test && npm run lint && npm run build>
```

### Out of scope unless asked
- No new dependencies without justification in the plan.
- No features beyond the approved spec.
- No changes to signing, CI secrets or production config.

### Clinical rules
<!-- Delete this section for non-health projects. One line per rule, with its source. -->
- <e.g. Danger sign: BP ≥ 140/90 at ≥ 20 weeks → show urgent-care alert (source: <guideline, year>)>
- <e.g. Weight-for-age z-score < -2 → "underweight" flag (WHO Child Growth Standards)>
- Every rule above needs a unit test that cites its source. Never change a rule
  without explicit approval.
<!-- full-stack-dev: end -->
