#!/usr/bin/env python3
"""job-scout: find remote (preferably part-time) jobs that fit your profile.

Reads only public job APIs meant for programmatic use, scores every job against
profile.json with transparent keyword rules, and writes a ranked report. It never
applies for you: you read the report and apply yourself.

Usage:
  python3 job_scout.py                  # fetch, score, write output/jobs-<date>.md + .csv
  python3 job_scout.py --offline FILE   # score jobs from a saved JSON file (no network)
  python3 job_scout.py --check-boards   # test which company board tokens exist
  python3 job_scout.py --no-cache       # ignore cached API responses
Python 3.9+, standard library only.
"""
import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "output"
CACHE = OUT / "cache"


@dataclass
class Job:
    source: str
    title: str
    company: str
    url: str
    location: str = ""
    job_type: str = ""
    description: str = ""
    posted: str = ""          # ISO date if known
    salary: str = ""
    score: int = 0
    reasons: list = field(default_factory=list)
    flags: list = field(default_factory=list)

    @property
    def key(self):
        return self.url or f"{self.company}|{self.title}"


# ── fetching ────────────────────────────────────────────────────────────────

def strip_html(text):
    text = html.unescape(text or "")
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def to_iso(value):
    """Best-effort date normaliser: epoch seconds/ms or ISO-ish strings -> YYYY-MM-DD."""
    if value in (None, ""):
        return ""
    try:
        if isinstance(value, (int, float)) or str(value).isdigit():
            v = float(value)
            v = v / 1000 if v > 1e11 else v
            return datetime.fromtimestamp(v, tz=timezone.utc).date().isoformat()
        return str(value)[:10]
    except (ValueError, OSError):
        return ""


def fetch_json(url, ua, use_cache, cache_hours):
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE / (re.sub(r"[^A-Za-z0-9]+", "_", url)[:150] + ".json")
    if use_cache and cache_file.exists() and time.time() - cache_file.stat().st_mtime < cache_hours * 3600:
        return json.loads(cache_file.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8", "replace"))
    cache_file.write_text(json.dumps(data), encoding="utf-8")
    return data


def from_remotive(data):
    for j in data.get("jobs", []):
        yield Job("Remotive", j.get("title", ""), j.get("company_name", ""), j.get("url", ""),
                  j.get("candidate_required_location", ""), j.get("job_type", ""),
                  strip_html(j.get("description", "")), to_iso(j.get("publication_date")), j.get("salary", ""))


def from_remoteok(data):
    for j in data if isinstance(data, list) else []:
        if not isinstance(j, dict) or "position" not in j:   # first element is the legal notice
            continue
        sal = ""
        if j.get("salary_min"):
            sal = f"{j.get('salary_min')}-{j.get('salary_max', '')}"
        yield Job("RemoteOK", j.get("position", ""), j.get("company", ""), j.get("url", ""),
                  j.get("location", ""), " ".join(j.get("tags", []) or []),
                  strip_html(j.get("description", "")), to_iso(j.get("epoch") or j.get("date")), sal)


def from_himalayas(data):
    for j in data.get("jobs", []):
        loc = j.get("locationRestrictions") or []
        loc = ", ".join(x if isinstance(x, str) else x.get("name", "") for x in loc) or "Worldwide"
        yield Job("Himalayas", j.get("title", ""), j.get("companyName", ""),
                  j.get("applicationLink") or j.get("guid") or j.get("url", ""), loc,
                  j.get("employmentType", ""), strip_html(j.get("description") or j.get("excerpt", "")),
                  to_iso(j.get("pubDate")), "")


def from_jobicy(data):
    for j in data.get("jobs", []):
        jt = j.get("jobType", "")
        yield Job("Jobicy", j.get("jobTitle", ""), j.get("companyName", ""), j.get("url", ""),
                  j.get("jobGeo", ""), ", ".join(jt) if isinstance(jt, list) else str(jt),
                  strip_html(j.get("jobDescription") or j.get("jobExcerpt", "")), to_iso(j.get("pubDate")), "")


def from_greenhouse(data, company):
    for j in data.get("jobs", []):
        yield Job("Greenhouse", j.get("title", ""), company, j.get("absolute_url", ""),
                  (j.get("location") or {}).get("name", ""), "",
                  strip_html(j.get("content", "")), to_iso(j.get("updated_at")), "")


def from_lever(data, company):
    for j in data if isinstance(data, list) else []:
        cat = j.get("categories") or {}
        yield Job("Lever", j.get("text", ""), company, j.get("hostedUrl", ""),
                  f"{cat.get('location', '')} {j.get('workplaceType', '')}".strip(), cat.get("commitment", ""),
                  j.get("descriptionPlain") or strip_html(j.get("description", "")), to_iso(j.get("createdAt")), "")


def from_ashby(data, company):
    for j in data.get("jobs", []):
        loc = j.get("location", "") + (" (remote)" if j.get("isRemote") else "")
        yield Job("Ashby", j.get("title", ""), company, j.get("jobUrl", ""), loc, j.get("employmentType", ""),
                  j.get("descriptionPlain") or strip_html(j.get("descriptionHtml", "")),
                  to_iso(j.get("publishedAt")), "")


def board_url(kind, token):
    t = urllib.parse.quote(token)
    return {
        "greenhouse": f"https://boards-api.greenhouse.io/v1/boards/{t}/jobs?content=true",
        "lever": f"https://api.lever.co/v0/postings/{t}?mode=json",
        "ashby": f"https://api.ashbyhq.com/posting-api/job-board/{t}",
    }[kind]


def collect(sources, use_cache=True):
    ua, hours = sources["user_agent"], sources.get("cache_hours", 12)
    agg = sources.get("aggregators", {})
    tasks = []   # (label, url, parser)
    if agg.get("remotive", {}).get("enabled"):
        for q in agg["remotive"].get("searches", []):
            tasks.append((f"remotive:{q}", "https://remotive.com/api/remote-jobs?search=" + urllib.parse.quote(q),
                          from_remotive))
    if agg.get("remoteok", {}).get("enabled"):
        tasks.append(("remoteok", "https://remoteok.com/api", from_remoteok))
    if agg.get("himalayas", {}).get("enabled"):
        for page in range(agg["himalayas"].get("pages", 1)):
            tasks.append((f"himalayas:p{page}", f"https://himalayas.app/jobs/api?limit=20&offset={page * 20}",
                          from_himalayas))
    if agg.get("jobicy", {}).get("enabled"):
        for tag in agg["jobicy"].get("tags", []):
            tasks.append((f"jobicy:{tag}", "https://jobicy.com/api/v2/remote-jobs?count=50&tag=" + urllib.parse.quote(tag),
                          from_jobicy))
    parsers = {"greenhouse": from_greenhouse, "lever": from_lever, "ashby": from_ashby}
    for kind, tokens in sources.get("company_boards", {}).items():
        for token in tokens:
            tasks.append((f"{kind}:{token}", board_url(kind, token),
                          lambda d, p=parsers[kind], c=token: p(d, c)))

    jobs, errors = [], []
    for label, url, parser in tasks:
        try:
            got = list(parser(fetch_json(url, ua, use_cache, hours)))
            jobs.extend(got)
            print(f"  {label:<28} {len(got):>4} jobs", file=sys.stderr)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, OSError) as e:
            errors.append(f"{label}: {e}")
            print(f"  {label:<28} skipped ({e})", file=sys.stderr)
    return jobs, errors


# ── scoring ─────────────────────────────────────────────────────────────────

def has(text, phrase):
    """Whole-word-ish match so 'ai ' doesn't hit 'maintain' and 'rn' doesn't hit 'learn'."""
    p = phrase.strip()
    return re.search(r"(?<![a-z0-9])" + re.escape(p) + r"(?![a-z0-9])", text) is not None


def score_job(job, profile, today=None):
    today = today or datetime.now(timezone.utc).date()
    title = f" {job.title.lower()} "
    body = f" {job.description.lower()} "
    meta = f" {job.location.lower()} {job.job_type.lower()} "
    everything = title + body + meta
    score, reasons, flags = 0, [], []

    if any(has(title, x) for x in profile.get("exclude_title", [])):
        job.score, job.flags = -100, ["excluded title"]
        return job

    for group, spec in profile["keywords"].items():
        hits = [p for p in spec["phrases"] if has(everything, p)]
        title_hits = [p for p in hits if has(title, p)]
        if hits:
            pts = min(spec["weight"] * (len(hits) + len(title_hits)), spec["weight"] * 6)
            score += pts
            shown = ", ".join(sorted(set(p.strip() for p in (title_hits or hits)))[:4])
            reasons.append(f"{group.replace('_', ' ')}: {shown}")

    # both worlds in one job is the sweet spot for a physician-builder
    groups_hit = {r.split(":")[0] for r in reasons}
    if {"clinical domain", "ai and product"} <= groups_hit:
        score += 15
        reasons.append("clinical + AI/product overlap")

    want = profile.get("want", {})
    pt_hits = [p for p in profile.get("part_time_signals", []) if has(everything, p)]
    if pt_hits:
        score += 15 if want.get("part_time_preferred") else 5
        reasons.append("part-time/contract: " + ", ".join(pt_hits[:3]))
    elif re.search(r"full[- ]?time", meta):
        if not want.get("full_time_ok", True):
            score -= 30
        flags.append("full-time")

    loc_text = meta + body[:1500]
    if any(has(loc_text, x) for x in profile.get("location_good", [])):
        score += 10
        reasons.append("location open to you")
    bad = [x for x in profile.get("location_bad", []) if has(loc_text, x)]
    if bad:
        score -= 35
        flags.append("location restricted: " + bad[0])

    lic = [x.strip(" ,") for x in profile.get("license_flags", []) if has(everything, x)]
    if lic:
        score -= 25
        flags.append("needs licence/credential: " + ", ".join(sorted(set(lic))[:3]))

    if job.posted:
        try:
            age = (today - datetime.fromisoformat(job.posted).date()).days
            if age > profile.get("max_age_days", 30):
                score -= 20
                flags.append(f"posted {age} days ago")
        except ValueError:
            pass

    job.score, job.reasons, job.flags = score, reasons, flags
    return job


def dedupe(jobs):
    seen, out = set(), []
    for j in jobs:
        k = (re.sub(r"\W+", "", j.company.lower()), re.sub(r"\W+", "", j.title.lower()))
        if j.key in seen or k in seen:
            continue
        seen.update({j.key, k})
        out.append(j)
    return out


# ── output ──────────────────────────────────────────────────────────────────

def write_reports(jobs, profile, errors, stamp):
    OUT.mkdir(exist_ok=True)
    seen_file = OUT / "seen.json"
    seen = set(json.loads(seen_file.read_text(encoding="utf-8"))) if seen_file.exists() else set()

    ranked = sorted((j for j in jobs if j.score >= profile.get("min_score", 25)),
                    key=lambda j: j.score, reverse=True)[: profile.get("top_n", 40)]

    md = [f"# Job scout — {stamp}", "",
          f"{len(jobs)} jobs scanned · {len(ranked)} shown (score ≥ {profile.get('min_score', 25)}) · "
          f"🆕 = not in a previous report", "",
          "| # | Score | Job | Company | Type | Location | Why | Flags | Source |",
          "|---|---|---|---|---|---|---|---|---|"]
    for i, j in enumerate(ranked, 1):
        new = "🆕 " if j.key not in seen else ""
        cell = lambda s: (s or "").replace("|", "/").replace("\n", " ")[:80]
        md.append(f"| {i} | {j.score} | {new}[{cell(j.title)}]({j.url}) | {cell(j.company)} | {cell(j.job_type)} | "
                  f"{cell(j.location)} | {cell('; '.join(j.reasons))} | {cell('; '.join(j.flags))} | {j.source} |")
    md += ["", "Sources: Remotive (remotive.com), Remote OK (remoteok.com), Himalayas (himalayas.app), "
           "Jobicy (jobicy.com), and company boards on Greenhouse, Lever and Ashby. Every link goes to the original posting.",
           "", "**Before applying:** read the full posting; check the location, licence and time-zone requirements; "
           "never pay a fee to apply."]
    if errors:
        md += ["", "<details><summary>Sources skipped this run</summary>", ""] + [f"- {e}" for e in errors] + ["", "</details>"]

    md_path, csv_path = OUT / f"jobs-{stamp}.md", OUT / f"jobs-{stamp}.csv"
    md_path.write_text("\n".join(md) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["score", "title", "company", "type", "location", "posted", "reasons", "flags", "source", "url"])
        for j in ranked:
            w.writerow([j.score, j.title, j.company, j.job_type, j.location, j.posted,
                        "; ".join(j.reasons), "; ".join(j.flags), j.source, j.url])
    seen_file.write_text(json.dumps(sorted(seen | {j.key for j in ranked})), encoding="utf-8")
    return md_path, csv_path, ranked


# ── CLI ─────────────────────────────────────────────────────────────────────

def check_boards(sources):
    ua = sources["user_agent"]
    for kind, tokens in sources.get("company_boards", {}).items():
        for token in tokens:
            try:
                fetch_json(board_url(kind, token), ua, use_cache=False, cache_hours=0)
                print(f"OK      {kind}:{token}")
            except Exception as e:  # report every failure, keep going
                print(f"FAILED  {kind}:{token}  ({e})")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", default=HERE / "profile.json", type=Path)
    ap.add_argument("--sources", default=HERE / "sources.json", type=Path)
    ap.add_argument("--offline", type=Path, help="JSON list of jobs (fields as in Job) to score without network")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--check-boards", action="store_true")
    args = ap.parse_args(argv)
    for stream in (sys.stdout, sys.stderr):   # Windows consoles default to cp1252
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="replace")

    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    sources = json.loads(args.sources.read_text(encoding="utf-8"))
    if args.check_boards:
        check_boards(sources)
        return 0

    if args.offline:
        raw = json.loads(args.offline.read_text(encoding="utf-8"))
        jobs, errors = [Job(**{k: v for k, v in r.items() if k in Job.__dataclass_fields__}) for r in raw], []
    else:
        print("Fetching jobs…", file=sys.stderr)
        jobs, errors = collect(sources, use_cache=not args.no_cache)

    jobs = [score_job(j, profile) for j in dedupe(jobs)]
    stamp = datetime.now().strftime("%Y-%m-%d")
    md_path, csv_path, ranked = write_reports(jobs, profile, errors, stamp)
    print(f"\n{len(ranked)} matches → {md_path} (and .csv)")
    for j in ranked[:10]:
        print(f"  {j.score:>4}  {j.title[:60]} — {j.company[:30]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
