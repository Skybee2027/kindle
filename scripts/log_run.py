#!/usr/bin/env python3
"""Append one line to reports/run-log.json so the owner can see what each robot did.

Usage: python3 scripts/log_run.py <robot> <status> "<book folder or -->" "<short detail>"
Status must be one of: done, approved, idle, stopped, blocked, failed, skipped.
Run from the repository root. Commit reports/run-log.json with the robot's other changes.
"""
import datetime
import json
import os
import sys
from zoneinfo import ZoneInfo

PATH = "reports/run-log.json"
STATUSES = {"done", "approved", "idle", "stopped", "blocked", "failed", "skipped"}


def main():
    if len(sys.argv) != 5:
        print(__doc__, file=sys.stderr)
        return 2
    robot, status, book, detail = sys.argv[1:5]
    if status not in STATUSES:
        print(f"status must be one of {sorted(STATUSES)}", file=sys.stderr)
        return 2
    entries = []
    if os.path.exists(PATH):
        with open(PATH, encoding="utf-8") as f:
            entries = json.load(f)
    # New York local time, so the daylight-saving change is handled.
    now = datetime.datetime.now(ZoneInfo("America/New_York"))
    entries.append({
        "at": now.strftime("%Y-%m-%d %H:%M"),
        "robot": robot,
        "status": status,
        "book": "" if book == "-" else book,
        "detail": detail,
    })
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"logged {robot}: {status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
