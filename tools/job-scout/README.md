# job-scout

A personal job finder for a **physician (MBBS, 10+ years) with AI product experience**,
looking for **remote, preferably part-time** work from India.

It reads **public job APIs that are meant to be read by programs**, scores every job
against `profile.json` with rules you can read and change, and writes a ranked report.
**It never applies for you.** You read the report and apply yourself. No scraping of
job boards that forbid it, no CAPTCHA solving, no bot submissions.

## Run it (on your own computer)
Needs Python 3.9+ and nothing else (standard library only).

```bash
cd tools/job-scout            # or wherever this folder lives
python3 job_scout.py          # fetch → score → output/jobs-<date>.md and .csv
python3 job_scout.py --check-boards   # which company board tokens exist (run once)
```

Open `output/jobs-<date>.md` (in Obsidian, VS Code, or any Markdown viewer). Each row
shows the **score**, **why** it matched, **flags** (US-only, licence required,
full-time, stale post) and a link to the original posting. 🆕 marks jobs that weren't
in a previous report. Results and the API cache stay in `output/`, which git ignores.

Run it once a day at most: the sources are free and ask for light use. Responses are
cached for 12 hours.

## Sources
| Source | What | Notes |
|---|---|---|
| Remotive | Remote jobs API, searched for medical / clinical / healthcare / physician / product / AI trainer | Credit Remotive; link back (the report does) |
| Remote OK | Remote jobs API | Credit Remote OK; link back |
| Himalayas | Remote jobs API, with location restrictions | |
| Jobicy | Remote jobs API, by tag | |
| Company boards | Greenhouse, Lever and Ashby public job-board APIs | Add companies in `sources.json` |

**Adding a company:** open its careers page. If the URL looks like
`boards.greenhouse.io/<token>`, `jobs.lever.co/<token>` or `jobs.ashbyhq.com/<token>`,
add `<token>` to that list in `sources.json`. The starter tokens are **unverified
guesses**; run `--check-boards` and delete the ones that fail.

## How scoring works (edit `profile.json`)
| Rule | Effect |
|---|---|
| Keyword groups: clinical domain (×6), AI & product (×5), strategy & ops (×3) | Points per phrase found; title matches count double; capped per group |
| Clinical **and** AI/product in the same job | +15 (your sweet spot) |
| Part-time / contract / freelance / hourly signals | +15 |
| Location open to you (worldwide, India, APAC…) | +10 |
| Location restricted (US only, must reside in…) | −35, flagged |
| Needs a licence you may not hold (US licence, board certified, RN, USMLE…) | −25, flagged |
| Posted more than 30 days ago | −20, flagged |
| Excluded titles (intern, SDR, senior software engineer…) | Dropped |

Only jobs scoring ≥ `min_score` (25) are shown, top 40. Tune the weights and phrases
after your first few runs. That's the fastest way to make it yours.

## Where else to look (not covered by APIs)
*Background knowledge, not verified from a source. Check each company yourself, and
never pay a fee to apply.*
- **Medical expert work for AI companies** (part-time, remote, hourly). Several AI
  data and evaluation companies hire doctors to review or write medical answers for
  AI models (e.g. Mercor, Outlier, Turing, Alignerr, Invisible, micro1). Add their
  Greenhouse/Lever/Ashby tokens here if they use one.
- **Health-tech startups:** Wellfound and YC's "Work at a Startup" let you filter by
  remote and part-time, but have no public API. Check weekly by hand.
- **Medical writing and clinical content:** med-comms agencies, health publishers,
  and freelance platforms.
- **Telemedicine in India:** consult platforms need your state medical council / NMC
  registration and follow the Telemedicine Practice Guidelines.
- **Fractional clinical or product advisor** for health-AI startups: your 12 shipped
  apps and Athira Health roadmap work are the pitch. Use LinkedIn and warm intros.

## Tests
```bash
python3 -m unittest discover -s tests
```
The 11 tests cover every API parser on sample data, the scoring rules (including no
false matches such as "rn" in "learn"), and an offline end-to-end run with
de-duplication. Live API field names were written from each API's documented format
but couldn't be checked from the build environment. If a source returns 0 jobs or
errors on your machine, tell Claude the message and it will adjust the parser.

## Move it to its own repo later
The folder is self-contained (no imports from the rest of the vault). From your
local clone of the vault:

**Option A: keep its git history (recommended)**
```bash
git subtree split --prefix=tools/job-scout -b job-scout-only
# create an empty repo on GitHub (e.g. job-scout, private), then:
git push git@github.com:<you>/job-scout.git job-scout-only:main
git branch -D job-scout-only
```

**Option B: a fresh copy with no history**
```bash
cp -R tools/job-scout ~/code/job-scout && cd ~/code/job-scout
git init && git add . && git commit -m "job-scout: initial import"
```

Afterwards: add `output/` to the new repo's `.gitignore`, and (if you want) remove
the folder from the vault with `git rm -r tools/job-scout`. Keep the vault's playbook
page (`wiki/resources/job-scout.md`) and point it at the new repo. Make the new repo
**private** if you add personal details to `profile.json`.
