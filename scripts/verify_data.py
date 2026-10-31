#!/usr/bin/env python3
"""Verify benchmark JSON/CSV consistency locally, without GitHub Actions."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "data" / "runs.json"
CSV_PATH = ROOT / "data" / "runs.csv"
VALID_STATUSES = {"success", "failure", "partial", "blocked", "stalled"}
FIELDS = (
    "run_id", "date", "project", "model", "effort", "run_type",
    "comparison_group", "task_summary", "quota_before_pct",
    "quota_after_pct", "quota_used_points", "quota_approx",
    "duration_seconds", "status", "quality_result", "expected_items",
    "found_items", "false_positives", "commit_sha", "prompt_capture",
    "response_capture", "notes",
)


def column(run: dict, field: str):
    if field == "quality_result":
        return (run.get("quality") or {}).get("summary")
    if field == "notes":
        return " | ".join(run.get("notes") or [])
    if field in {"expected_items", "found_items", "false_positives"}:
        return (run.get("quality") or {}).get(field)
    return run.get(field)


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def render_csv(runs: list[dict]) -> str:
    buff = io.StringIO(newline="")
    writer = csv.writer(buff, lineterminator="\n")
    writer.writerow(FIELDS)
    for run in runs:
        writer.writerow([as_text(column(run, field)) for field in FIELDS])
    return buff.getvalue()


def verify(runs: list[dict]) -> None:
    seen = set()
    for n, run in enumerate(runs, start=1):
        key = run.get("run_id")
        if key != f"GP-{n:03d}" or key in seen:
            raise ValueError(f"Run ID absent, duplicate or out of sequence at row {n}: {key}")
        seen.add(key)
        if run.get("status") not in VALID_STATUSES:
            raise ValueError(f"{key}: unrecognized status {run.get('status')!r}")
        if not run.get("project") or not run.get("model") or not run.get("effort"):
            raise ValueError(f"{key}: project/model/effort missing")
        if not isinstance(run.get("duration_seconds"), (int, float)) or run["duration_seconds"] < 0:
            raise ValueError(f"{key}: invalid duration")
        quota = run.get("quota_used_points")
        if quota is not None and (not isinstance(quota, (int, float)) or quota < 0):
            raise ValueError(f"{key}: invalid visible quota")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-csv", action="store_true", help="Regenerate CSV from JSON")
    args = parser.parse_args()
    runs = json.loads(JSON_PATH.read_text(encoding="utf-8"))["runs"]
    verify(runs)
    expected = render_csv(runs)
    if args.write_csv:
        CSV_PATH.write_text(expected, encoding="utf-8", newline="")
        print(f"CSV regenerated: {len(runs)} runs")
    elif CSV_PATH.read_text(encoding="utf-8") != expected:
        print("FAIL: data/runs.csv differs from canonical data/runs.json")
        return 1

    statuses = Counter(r["status"] for r in runs)
    print(f"PASS: {len(runs)} unique runs, JSON/CSV consistent")
    print("Statuses:", ", ".join(f"{k}={statuses[k]}" for k in sorted(statuses)))
    for (model, effort) in sorted({(r["model"], r["effort"]) for r in runs}):
        group = [r for r in runs if (r["model"], r["effort"]) == (model, effort)]
        ok = [r for r in group if r["status"] == "success"]
        quotas = [r["quota_used_points"] for r in ok if isinstance(r.get("quota_used_points"), (int, float))]
        times = [r["duration_seconds"] for r in ok if isinstance(r.get("duration_seconds"), (int, float))]
        median_quota = str(statistics.median(quotas)) if quotas else "N/D"
        median_seconds = str(statistics.median(times)) if times else "N/D"
        print(f"  {model} / {effort}: {len(ok)}/{len(group)} delivered,"
              f" quota median={median_quota}, time median={median_seconds}s")
    print("Real-world validation rate: N/D (not reliably structured in the historical JSON)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
