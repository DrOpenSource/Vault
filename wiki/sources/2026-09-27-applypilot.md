---
title: "ApplyPilot (GitHub repo)"
type: source
kind: other
raw: raw/2026-09-27-applypilot.md
author: Pickle-Pixel (Henry Muhiar)
published: 2026-03-08
url: https://github.com/Pickle-Pixel/ApplyPilot
tags: [ai-product, agents, careers, monetization]
aliases: []
created: 2026-09-27
updated: 2026-09-27
sources: []
status: active
---

# ApplyPilot (GitHub repo)

> [raw source](../../raw/2026-09-27-applypilot.md) · Pickle-Pixel · code repo,
> v0.3.0, **AGPL-3.0**, about 9.6K lines of Python. Entity: [[applypilot]].
> Analysis: [[applypilot-monetization]].

## TL;DR
An open-source, **fully autonomous job-application pipeline**: it discovers jobs
on 5 boards plus about 78 employer sites, scores them against your resume with an
LLM, rewrites your resume and cover letter per job, then **submits applications
for you** by driving Chrome through headless [[claude-code|Claude Code]] sessions.
Its headline: "Applied to 1,000 jobs in 2 days."

## Key takeaways
1. **Six stages:** discover → enrich → score → tailor → cover letter →
   auto-apply. Stages 1–5 work alone, with you submitting by hand.
2. **Discovery scrapes** Indeed, LinkedIn, Glassdoor, ZipRecruiter and Google Jobs
   (via the JobSpy library), 48 Workday portals and 30 career sites.
3. **Auto-apply runs Claude Code in the background** with `--permission-mode
   bypassPermissions` for each job, and uses a browser-automation (Playwright)
   server to fill forms, upload documents, answer screening questions and submit
   (from reading `apply/launcher.py`).
4. **Optional CAPTCHA solving** through a paid third-party service (CapSolver).
5. **It fills legally significant fields automatically:** work authorization,
   sponsorship, salary, and voluntary equal-opportunity (EEO) answers, all taken
   from your profile (from reading `apply/prompt.py`).
6. **License is AGPL-3.0:** commercial use is allowed, but anyone who runs a
   *modified* version as a network service must publish its source under the same
   license.
7. **The name is already contested.** The README warns that applypilot.app and
   useapplypilot.com are unrelated products using the same name.

## Notable claims
- "Applied to 1,000 jobs in 2 days. Fully autonomous. Open source."
- Tailoring "reorganizes but never fabricates." This is an instruction to the LLM,
  not something the code guarantees *(inference)*.
- Gemini's free tier is "enough" for scoring and tailoring.

## Entities & concepts touched
- [[applypilot]], [[claude-code]], [[agent-harness]] (it uses Claude Code as its
  browser agent), [[ai-product-development]]

## Open questions
- What do job boards' terms say about scraping and automated applications?
  Check each platform's current user agreement.
- What does one auto-applied job actually cost in model tokens? Not measured.
- How do employers respond to mass AI applications (filters, bans)?
