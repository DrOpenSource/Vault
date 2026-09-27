---
title: job-scout
type: resource
resource_kind: app
url: https://github.com/DrOpenSource/job-scout
version: 1.0.1
checked: 2026-09-27
install_status: installed
tags: [careers, job-search, my-tools, playbook]
aliases: [Job Scout, job finder]
created: 2026-09-27
updated: 2026-09-27
sources: [2026-09-27-applypilot, 2026-09-26-resume]
status: active
---

# job-scout — playbook

> **Your personal job finder**, built 2026-09-27 in
> the vault, and moved on 2026-09-27 to its own **private repo**
> [DrOpenSource/job-scout](https://github.com/DrOpenSource/job-scout). It finds **remote,
> preferably part-time** roles that fit an MBBS with 10+ years of clinical and
> leadership work plus AI product experience ([[2026-09-26-resume]]). It takes the
> safe half of [[applypilot|ApplyPilot]]'s idea (find → score) and leaves out
> scraping and auto-submission ([[applypilot-monetization]]).

## What it is
One Python script with no dependencies. It pulls jobs from public job APIs
(Remotive, Remote OK, Himalayas, Jobicy, and company boards on Greenhouse, Lever
and Ashby) and scores each one with rules you can read. It writes
`output/jobs-<date>.md` and `.csv`, marking 🆕 on jobs not seen in a previous
report. **You apply yourself.**

## When to use it / when not
- **Daily or every few days** while you're job hunting. It runs in about a minute
  and caches results for 12 hours.
- **It doesn't cover** LinkedIn, Naukri, Wellfound or AI-training marketplaces
  without public APIs. The README lists those as channels to check by hand.

## Setup
```bash
cd C:\Users\user\Desktop\Dr_Opensource\job-scout   # your local clone of the private repo
git pull                                             # get updates
python3 job_scout.py --check-boards   # once: prune company tokens that don't exist
python3 job_scout.py                  # daily
```
It needs Python 3.9+ and open internet. It couldn't fetch live data from the cloud
build environment, because the network policy blocks job sites.

## How to use it best (your workflow)
1. **First run:** read the top 20 and note wrong rankings. Then tell me in plain
   words, e.g. "score medical writing higher" or "drop anything asking for 5+ years
   of product management", and I'll tune `profile.json`.
2. **Grow the company list:** when you find a health-tech or AI company you like,
   add its Greenhouse/Lever/Ashby token in `sources.json`.
3. **Apply with your own materials:** use your resume plus the positioning in
   [[physician-technologist]]. For a tailored cover letter, paste the job text into
   a chat.
4. **Log what happens:** once a week, paste the week's applications and replies here
   and say "ingest". The vault will learn which roles actually respond.

## Commands / reference
| Command | Does |
|---|---|
| `python3 job_scout.py` | Fetch, score, report |
| `python3 job_scout.py --no-cache` | Ignore the 12-hour cache |
| `python3 job_scout.py --offline jobs.json` | Score a saved list without internet |
| `python3 job_scout.py --check-boards` | Test company board tokens |
| `python3 -m unittest discover -s tests` | 12 offline tests (Windows: `py -m unittest discover -s tests`) |

Scoring rules (in `profile.json`):
- Keywords: clinical ×6, AI/product ×5, strategy/ops ×3
- +15 when clinical and AI/product appear in the same job
- +15 part-time or contract signals
- +10 location open to you
- −35 US-only or other restricted location
- −25 needs a US licence or similar credential
- −20 posted more than 30 days ago

## Pitfalls & caveats
- **Windows:** use `py` instead of `python3`. v1.0.1 fixes a crash when writing the report on Windows (default cp1252 text encoding); all files are now UTF-8, and the CSV opens cleanly in Excel.
- **Parsers are unverified against live APIs.** They were written from each API's
  documented format and tested on sample data. If a source shows 0 jobs or an error
  on your machine, send me the message.
- **Company boards:** 4 confirmed on your machine (2026-09-27): Greenhouse `flatironhealth`, `turing`, `scaleai`; Ashby `openevidence`. The 7 guesses that returned 404 were removed. Add more as you find them.
- **Keyword scoring is blunt.** It can't judge seniority or how good a role is.
  Treat the score as a sorting aid, not a verdict.
- **Scams:** never pay to apply, and check that the recruiter's email domain matches
  the company.
- **Public repo:** `profile.json` has no contact details; keep it that way, or move
  the tool to a private repo (README → "Move it to its own repo later").

## Connections
- [[applypilot-monetization]] — why it's human-in-the-loop, and the product idea it
  tests on you first
- [[physician-technologist]], [[me]]

## Sources
- [[2026-09-27-applypilot]]
- [[2026-09-26-resume]]
