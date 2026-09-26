#!/usr/bin/env python3
"""Mechanical health check for the wiki (see CLAUDE.md §6.3).

Reports: broken wikilinks, orphan pages, missing/invalid frontmatter,
pages absent from index.md, duplicate filenames, and source slugs in
frontmatter that don't exist. Judgment checks (contradictions, stale
claims) are left to the LLM.

Usage: python3 tools/lint.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SPECIAL = {"index", "log"}
TYPES = {"source", "entity", "concept", "synthesis", "overview"}
REQUIRED = ["title", "type", "created", "updated", "sources", "status"]
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def main():
    pages = {}
    problems = []
    for path in sorted(WIKI.rglob("*.md")):
        slug = path.stem
        if slug in pages:
            problems.append(f"duplicate filename: {path.relative_to(ROOT)} and {pages[slug].relative_to(ROOT)}")
        pages[slug] = path

    inbound = {slug: set() for slug in pages}
    index_links = set()
    for slug, path in pages.items():
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target not in pages:
                problems.append(f"broken link: [[{target}]] in {path.relative_to(ROOT)}")
            elif target != slug:
                inbound[target].add(slug)
                if slug == "index":
                    index_links.add(target)
        if slug in SPECIAL:
            continue
        fm = frontmatter(text)
        if fm is None:
            problems.append(f"missing frontmatter: {path.relative_to(ROOT)}")
            continue
        for key in REQUIRED:
            if key not in fm:
                problems.append(f"missing '{key}': {path.relative_to(ROOT)}")
        if fm.get("type") not in TYPES:
            problems.append(f"bad type '{fm.get('type')}': {path.relative_to(ROOT)}")
        for src in re.findall(r"[\w-]+", fm.get("sources", "").strip("[]")):
            if src not in pages:
                problems.append(f"unknown source slug '{src}' in {path.relative_to(ROOT)}")
        if fm.get("type") == "source" and fm.get("raw"):
            if not (ROOT / fm["raw"]).exists():
                problems.append(f"raw file not found: {fm['raw']} ({path.relative_to(ROOT)})")

    for slug in pages:
        if slug in SPECIAL:
            continue
        if slug != "overview" and not (inbound[slug] - {"index", "log"}):
            problems.append(f"orphan (no inbound links besides index/log): {slug}")
        if slug not in index_links:
            problems.append(f"not listed in index.md: {slug}")

    print(f"{len(pages)} pages checked.")
    if problems:
        print(f"{len(problems)} issue(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("No mechanical issues found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
