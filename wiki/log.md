# Log

*Append-only. Newest at the bottom. Every entry header: `## [YYYY-MM-DD] <op> | <title>`.*
*Last 5 entries: `grep "^## \[" wiki/log.md | tail -5`*

## [2026-09-26] setup | Vault initialized
- Created schema `CLAUDE.md`, folder structure (`raw/`, `raw/assets/`, `wiki/{sources,entities,concepts,syntheses}`, `templates/`, `tools/`).
- Created `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`, page templates, `tools/lint.py`, `.obsidian/app.json` (attachments → `raw/assets`).

## [2026-09-26] ingest | LLM Wiki: a pattern for personal knowledge bases
- Saved user-pasted idea file to `raw/2026-09-26-llm-wiki-pattern.md`.
- Created source page: [[2026-09-26-llm-wiki-pattern]].
- Created concepts: [[llm-wiki]], [[retrieval-augmented-generation]], [[maintenance-burden]], [[memex]].
- Created entities: [[vannevar-bush]], [[obsidian]], [[qmd]].
- Updated: [[overview]], index. Added 4 Wanted pages (NotebookLM, Dataview, Marp, Tolkien Gateway).
- Discussion step skipped: user asked for a demonstration ingest. Open thread: which domains the vault should focus on.

## [2026-09-26] ingest | Vault focus statement (reflect)
- Saved the user's purpose statement to `raw/2026-09-26-vault-focus.md`; created source page [[2026-09-26-vault-focus]].
- Created: [[me]] (owner profile), [[generalist]], [[ai-product-development]], [[personal-productivity]].
- Updated: [[overview]] (rewritten around the vault's purpose and 4 themes), [[llm-wiki]], index.
- Open threads: current role, specialty, target role, definition of "productive". Proposed a schema tweak for domain tags (pending user approval).

## [2026-09-26] ingest | Resume — Dr. Shubham Kashyap
- Saved uploaded PDF to `raw/2026-09-26-resume.pdf`; created source page [[2026-09-26-resume]]. Phone and email kept out of the wiki.
- Created entities: [[mediq]], [[grow-baby-grow]], [[saathi]], [[athira-health]], [[docbot]], [[stemz-healthcare]], [[n8n]], [[claude-code]].
- Created concepts: [[physician-technologist]], [[ai-assisted-development]].
- Updated: [[me]] (rewritten as a full profile), [[ai-product-development]] (inferred advantages now sourced), [[generalist]], [[overview]], index.
- Discussion step skipped: the user asked directly to add the resume. Push held because the repo is public; resolved by the schema entry below.

## [2026-09-26] schema | Privacy rule for a public repo
- User chose to keep original PDFs out of git: added `raw/*.pdf` to `.gitignore`. The resume PDF is kept local only.
- Added `raw/2026-09-26-resume.md`, a text copy with email and phone removed; [[2026-09-26-resume]] now points to it.
- Updated `CLAUDE.md` §9 Privacy: the repo is public; commit redacted copies; flag personal material before pushing.

## [2026-09-26] schema | Resources section
- At the user's request, added `wiki/resources/` and page type `resource` (a playbook: when to use → setup → how to use it best → commands → pitfalls) to `CLAUDE.md` §2/§4/§7, `templates/resource.md`, `tools/lint.py`, and an index section.

## [2026-09-26] ingest | Ponytail (GitHub repo)
- Cloned github.com/dietrichgebert/ponytail (v4.10.0); saved README and core SKILL.md files verbatim to `raw/2026-09-26-ponytail.md`; created source page [[2026-09-26-ponytail]].
- Created resource playbook [[ponytail]], tailored to the user's workflow, with a clinical-logic safety rule for health apps. Created concept [[yagni]].
- Updated: [[ai-assisted-development]], [[claude-code]], [[overview]], index (Resources section; Caveman added to Wanted pages).
- Discussion step skipped: the user gave a direct instruction. Open: install and trial it on one app, then record the results on [[ponytail]].

## [2026-09-26] revise | Decided not to use Ponytail
- User decision: Ponytail won't be installed. Marked [[ponytail]] with `decision: not using` and a User view note; the page is kept for reference.
- Updated index, [[overview]], [[claude-code]].

## [2026-09-27] ingest | gstack (GitHub repo) + Claude API pricing
- Cloned github.com/garrytan/gstack (v1.91.2.0) and **installed it in the cloud session** (browser skipped). Measured with `gstack-context-bill`: about 7K always-on tokens across 55 skills; 3K–51K per skill used. No hooks added; telemetry off.
- Saved `raw/2026-09-27-gstack.md` (README, digest, ethos excerpt) and `raw/2026-09-27-claude-pricing.md` (price table, caching, four agent approaches). Created source pages [[2026-09-27-gstack]], [[2026-09-27-claude-pricing]].
- Created resource [[gstack]] (trialling), concept [[agent-harness]], syntheses [[agent-management-plan]] and [[harness-cost-comparison]].
- Updated: [[claude-code]], [[ai-assisted-development]], [[yagni]] (contradiction callout: YAGNI vs "Boil the Ocean"), [[ponytail]], [[overview]], index (+3 Wanted pages).
- Discussion step skipped: the user gave a direct instruction. Open: subscription plan prices; the Phase 1 lane choice.

## [2026-09-27] skill | Full-Stack Dev
- User decisions: skip a separate harness for now; condense gstack into their own skill instead of installing all of it.
- Built `skills/full-stack-dev/`: `SKILL.md` (router, 8 always-on rules, clinical safety gate, lane board), 9 stage files, 3 templates, `setup/install.sh` (global/project, idempotent, optional permission-rule merge), `settings.example.json`, `NOTICE.md` (gstack MIT).
- Tested: project install on a scratch repo (re-run safe, settings merged with backup, valid JSON); global install; skill loaded in Claude Code and `status` ran.
- Schema: added `skills/` layer, `resource_kind: skill`, the `skill` operation and log op. Created resource [[full-stack-dev]].
- Updated: [[gstack]] (not installed; condensed), [[agent-management-plan]] (Phase 0/1 now use the skill; gstack install struck through), [[harness-cost-comparison]] (User view: skip harness), [[claude-code]], [[ai-assisted-development]], [[overview]], index.

## [2026-09-27] ingest | ApplyPilot (GitHub repo) + monetization query
- Fast-forwarded `main` to `c28daa6` at the user's request (Full-Stack Dev skill now on `main`).
- Cloned github.com/Pickle-Pixel/ApplyPilot (v0.3.0, AGPL-3.0); saved the README to `raw/2026-09-27-applypilot.md`. Read the launcher and prompt code: bypassPermissions Claude Code sessions, CAPTCHA-solving option, automatic EEO/work-authorization answers.
- Created [[2026-09-27-applypilot]], entity [[applypilot]], synthesis [[applypilot-monetization]]. Verdict: don't resell the auto-apply bot; validate a human-in-the-loop clinician career copilot instead.
- Updated: [[ai-product-development]], [[me]], [[overview]], index.

## [2026-09-27] skill | job-scout (personal job finder)
- User asked for a job finder that works for them: remote, part-time OK, MBBS with 10 years' experience, India, plus AI product experience.
- Built `tools/job-scout/`: stdlib-only Python; public job APIs (Remotive, Remote OK, Himalayas, Jobicy, Greenhouse/Lever/Ashby boards); transparent scoring from `profile.json`; Markdown/CSV report; no auto-apply. `tools/job-scout/output/` is git-ignored.
- Tests: 11 offline tests pass; the live run here skipped every source (network policy 403) and still produced a report. `git subtree split` verified, and the split copy passes its tests standalone.
- Schema: `tools/` now also holds self-contained personal utilities. Created resource [[job-scout]]; updated [[applypilot-monetization]], [[me]], [[overview]], index.
- Open: first live run on the user's machine; check board tokens; tune the profile.

## [2026-09-27] schema | Step-by-step guides in chat
- User preference: always give manual steps as a hand-holding guide in the chat (numbered steps, exact commands, expected output, fixes). Added to `CLAUDE.md` §8 Style.

## [2026-09-27] revise | job-scout Windows fix + confirmed boards
- The user's first run on Windows: 1 test failed with `UnicodeEncodeError` (cp1252 can't encode `≥`/`—`/🆕). Reproduced here under a non-UTF-8 locale.
- Fixed: every file read/write now uses UTF-8 (CSV as `utf-8-sig` for Excel); console output can no longer crash on special characters. Added a guard test (12 tests), which passes under both UTF-8 and non-UTF-8 locales.
- `--check-boards` on the user's machine: 4 boards OK (greenhouse flatironhealth, turing, scaleai; ashby openevidence), 7 removed (404). Updated [[job-scout]] to v1.0.1.

## [2026-09-27] revise | job-scout: first live run
- The user's first live run fetched ~700 jobs: remotive 6×18, remoteok 99, himalayas 60, jobicy 150, greenhouse flatironhealth 27 / turing 34 / scaleai 203, ashby openevidence 10. The live parsers work.
- Jobicy tag `ai` → HTTP 400; removed. The report still crashed because the user hadn't pulled the v1.0.1 Windows fix yet.

## [2026-09-27] revise | job-scout moved to its own private repo
- The user split `tools/job-scout` into the private repo `DrOpenSource/job-scout` with `git subtree split` (history kept; GitHub shows it private, with Python code).
- Removed `tools/job-scout/` and its `.gitignore` entry from the vault; its history remains in the vault's git log. [[job-scout]] now points to the new repo and local folder. Updated `CLAUDE.md` §1 Tools row and index.
- Open: connect `DrOpenSource/job-scout` to future sessions so Claude can keep working on it there.
