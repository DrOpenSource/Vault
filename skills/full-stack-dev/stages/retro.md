# Stage: retro — weekly look back, so the process improves

Adapted from gstack `/retro`.

## Steps
1. **Collect facts** for the period (default: last 7 days):
   - `git log --since="7 days ago" --oneline` per repo or lane
   - PRs merged, releases shipped, reverts
   - bugs found after release (issues, crash reports if available)
   - `docs/fsd/` artifacts created (briefs, specs, plans, reviews, QA)
2. **Measure:** changes shipped · bugs escaped to users · stages skipped · lanes
   run in parallel · where you waited the longest.
3. **Reflect** in three short lists: **keep**, **change**, **try next week**.
4. **Update the lane board** (`docs/fsd/lanes.md`): close finished lanes and open
   next week's.
5. **Vault export:** end with a block the user can paste into their second-brain
   vault and say "ingest" to:

```markdown
---
title: "Retro <YYYY-MM-DD> — <project>"
kind: note
---
<the retro content>
```

## Artifact: `docs/fsd/retros/<date>.md`

## Handoff
"Retro saved. Top change for next week: … Paste the export block into your vault
to ingest it."
