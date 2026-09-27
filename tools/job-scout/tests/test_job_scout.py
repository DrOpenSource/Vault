"""Offline tests: parsers on sample payloads shaped like each API, plus scoring rules.
Run: python3 -m unittest discover -s tools/job-scout/tests
"""
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import job_scout as js  # noqa: E402

PROFILE = json.loads((Path(js.HERE) / "profile.json").read_text(encoding="utf-8"))
TODAY = date(2026, 9, 27)


def job(title, desc="", location="Worldwide", job_type="", posted="2026-09-20", company="Acme"):
    return js.Job("Test", title, company, f"https://x/{title}", location, job_type, desc, posted)


class ParserTests(unittest.TestCase):
    def test_remotive(self):
        data = {"jobs": [{"title": "Medical Reviewer", "company_name": "A", "url": "u1", "job_type": "contract",
                          "candidate_required_location": "Worldwide", "description": "<p>MBBS &amp; AI</p>",
                          "publication_date": "2026-09-20T10:00:00"}]}
        j = next(js.from_remotive(data))
        self.assertEqual((j.title, j.description, j.posted), ("Medical Reviewer", "MBBS & AI", "2026-09-20"))

    def test_remoteok_skips_legal_notice(self):
        data = [{"legal": "notice"}, {"position": "PM", "company": "B", "url": "u", "tags": ["ai"],
                                      "epoch": 1790000000, "location": "Anywhere"}]
        jobs = list(js.from_remoteok(data))
        self.assertEqual(len(jobs), 1)
        self.assertEqual(jobs[0].job_type, "ai")

    def test_himalayas_location_objects(self):
        data = {"jobs": [{"title": "T", "companyName": "C", "applicationLink": "u",
                          "locationRestrictions": [{"name": "India"}, "APAC"], "pubDate": 1790000000}]}
        self.assertEqual(next(js.from_himalayas(data)).location, "India, APAC")

    def test_boards(self):
        gh = {"jobs": [{"title": "Clinical Lead", "absolute_url": "u", "location": {"name": "Remote"},
                        "content": "&lt;p&gt;hi&lt;/p&gt;", "updated_at": "2026-09-01T00:00:00Z"}]}
        self.assertEqual(next(js.from_greenhouse(gh, "co")).description, "hi")
        lv = [{"text": "Advisor", "hostedUrl": "u", "categories": {"commitment": "Part-time", "location": "Remote"},
               "descriptionPlain": "d", "createdAt": 1790000000000}]
        self.assertEqual(next(js.from_lever(lv, "co")).job_type, "Part-time")
        ab = {"jobs": [{"title": "PM", "location": "India", "isRemote": True, "employmentType": "Contract",
                        "jobUrl": "u", "descriptionPlain": "d", "publishedAt": "2026-09-10T00:00:00Z"}]}
        self.assertEqual(next(js.from_ashby(ab, "co")).location, "India (remote)")


class ScoringTests(unittest.TestCase):
    def s(self, j):
        return js.score_job(j, PROFILE, today=TODAY)

    def test_ideal_job_scores_high(self):
        j = self.s(job("Medical Expert – AI Model Evaluation (Part-time)",
                       "Physicians (MBBS/MD) to review LLM outputs for clinical accuracy. Contract, 10-20 hours per week. Open worldwide.",
                       job_type="contract"))
        self.assertGreaterEqual(j.score, 60)
        self.assertIn("clinical + AI/product overlap", j.reasons)
        self.assertEqual(j.flags, [])

    def test_us_license_is_flagged_and_penalised(self):
        good = self.s(job("Clinical Reviewer", "Physician reviewer, part-time contract."))
        lic = self.s(job("Clinical Reviewer", "Physician reviewer, part-time contract. Must hold active US license, board certified."))
        self.assertLess(lic.score, good.score)
        self.assertTrue(any("licence" in f for f in lic.flags))

    def test_location_restriction(self):
        j = self.s(job("Product Manager, Digital Health", "Healthcare product role.", location="US only"))
        self.assertTrue(any("location restricted" in f for f in j.flags))

    def test_excluded_title(self):
        self.assertEqual(self.s(job("Senior Software Engineer", "clinical AI")).score, -100)

    def test_no_false_substring_hits(self):
        # 'rn' must not match 'learn', 'ai' must not match 'maintain'
        j = self.s(job("Office Assistant", "You will learn to maintain records.", location="Germany"))
        self.assertFalse(any("licence" in f for f in j.flags))
        self.assertLess(j.score, PROFILE["min_score"])

    def test_old_posting_penalised(self):
        fresh = self.s(job("Medical Writer", "clinical content, freelance", posted="2026-09-25"))
        old = self.s(job("Medical Writer", "clinical content, freelance", posted="2026-06-01"))
        self.assertLess(old.score, fresh.score)


class EndToEndOffline(unittest.TestCase):
    def test_offline_run_writes_reports(self):
        jobs = [
            {"source": "T", "title": "Physician AI Trainer (Contract)", "company": "A", "url": "https://a",
             "location": "Worldwide", "job_type": "contract", "description": "MBBS doctors to evaluate LLM answers, hourly."},
            {"source": "T", "title": "Physician AI Trainer (Contract)", "company": "A", "url": "https://a",
             "location": "Worldwide", "job_type": "contract", "description": "duplicate"},
            {"source": "T", "title": "Warehouse Associate", "company": "B", "url": "https://b", "description": ""},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            js.OUT = Path(tmp)
            src = Path(tmp) / "jobs.json"
            src.write_text(json.dumps(jobs), encoding="utf-8")
            self.assertEqual(js.main(["--offline", str(src)]), 0)
            md = next(Path(tmp).glob("jobs-*.md")).read_text(encoding="utf-8")
            self.assertIn("Physician AI Trainer", md)
            self.assertNotIn("Warehouse", md)
            self.assertEqual(md.count("Physician AI Trainer"), 1)   # deduped
            self.assertIn("🆕", md)


class WindowsSafetyTests(unittest.TestCase):
    def test_every_file_io_call_sets_utf8(self):
        """Windows defaults to cp1252; any read/write without encoding= breaks on ≥, —, 🆕."""
        import re
        src = (Path(js.HERE) / "job_scout.py").read_text(encoding="utf-8")
        calls = re.findall(r"\.(?:read_text|write_text|open)\([^\n]*", src)
        missing = [c for c in calls if "encoding=" not in c]
        self.assertEqual(missing, [], f"file I/O without encoding=: {missing}")


if __name__ == "__main__":
    unittest.main()
