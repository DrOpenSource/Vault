# Stage: think — is this worth building, and what exactly is it?

Goal: turn an idea into a sharp problem statement before any spec or code.
Adapted from gstack `/office-hours`.

## Steps

1. **Restate the idea** in one sentence and ask the user to confirm or correct it.
2. **Ask the forcing questions one at a time.** Use the ones that fit the stage:
   - Pre-product → Q1, Q2, Q3
   - Has users → Q2, Q4, Q5
   - Pure engineering/infra → Q2, Q4

   Push on each answer until it is specific and evidence-based. Skip a question
   if an earlier answer already covered it.

   - **Q1 Demand:** "What's the strongest evidence someone actually wants this —
     would be upset if it disappeared tomorrow?" Red flag: "people say it's
     interesting", waitlists.
   - **Q2 Status quo:** "What do users do today to solve this, even badly? What
     does that cost them?" Red flag: "nothing exists".
   - **Q3 Specific person:** "Name the actual person who needs this most. Their
     role, and what happens to them if it isn't solved?" Red flag: categories
     ("clinicians", "parents").
   - **Q4 Narrowest wedge:** "What's the smallest version someone would use or pay
     for this week?" Red flag: "we need the full platform first".
   - **Q5 Observation:** "Have you watched someone use it without helping? What
     surprised you?"
   - **Q6 Future-fit:** "In 3 years, does this become more essential or less?"

   **Health products add Q7:** "What clinical guideline or evidence does this rest
   on, and what's the worst harm if the app is wrong?"
3. **Challenge the framing once.** If the answers describe something different from
   the stated idea, say so ("You said X; what you described is Y") and let the user
   choose.
4. **Offer 2–3 approaches** with rough effort (human-days vs AI-assisted hours)
   and recommend one: usually the narrowest wedge that proves demand.

## Artifact: `docs/fsd/briefs/<slug>.md`

```markdown
# Brief: <name>
Date: <YYYY-MM-DD>
## Problem (one paragraph, in the user's words where possible)
## Who it's for (a specific person)
## Evidence of demand
## Status quo and its cost
## Narrowest wedge
## Clinical basis and worst-case harm (health products)
## Approaches considered → recommendation
## Open questions
```

## Handoff
"Brief saved to `docs/fsd/briefs/<slug>.md`. Next: `spec`."
