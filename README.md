# Vault — an LLM-maintained second brain

You curate sources and ask questions. The LLM agent writes and maintains the wiki.
The full rules are in [`CLAUDE.md`](CLAUDE.md).

- `raw/` — your source documents (never edited by the agent)
- `wiki/` — the agent's pages. Start at [`wiki/index.md`](wiki/index.md) or [`wiki/overview.md`](wiki/overview.md)
- `wiki/log.md` — timeline of every ingest, query, and lint

## Daily use
| You say | The agent does |
|---|---|
| "Ingest `raw/<file>`", or paste text/a URL and say "ingest" | Summarizes it, discusses takeaways, updates 5–15 pages, the index, and the log |
| Any question | Answers from the wiki with citations; asks whether to file substantive answers into `wiki/syntheses/` |
| "Lint" | Runs `tools/lint.py` and checks for contradictions, gaps, and missing pages |
| "Change the schema so…" | Updates `CLAUDE.md` and migrates pages |

Open this folder as a vault in Obsidian to browse the pages and the graph view.
