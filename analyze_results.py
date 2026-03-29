# student_name: Jejo J
# roll_number: 727823tucy019
# project_name: Credential Stuffing Simulator
# date: 2026-03-29

"""
analyze_results.py
------------------
Pipeline Step 3 — Parse log files and print summary statistics.
"""

import os
import re
from datetime import datetime
from collections import defaultdict

ROLL = "727823tucy019"
LOG_DIR = "logs"
LOG_FILES = ["tc1_logs.txt", "tc2_logs.txt", "tc3_logs.txt", "webapp_logs.txt"]


def parse_log_file(path: str) -> list[dict]:
    entries = []
    pattern = re.compile(
        r"\[(?P<ts>[^\]]+)\] username=(?P<user>\S+)\s+password=(?P<pwd>\S+)\s+status=(?P<status>.+)"
    )
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                m = pattern.search(line)
                if m:
                    entries.append({
                        "timestamp": m.group("ts"),
                        "username": m.group("user").strip("'"),
                        "password": m.group("pwd").strip("'"),
                        "status": m.group("status").strip(),
                    })
    except FileNotFoundError:
        pass
    return entries


def print_report(label: str, entries: list[dict]):
    if not entries:
        print(f"  (no entries in {label})")
        return

    counts = defaultdict(int)
    locked_users = set()
    for e in entries:
        counts[e["status"]] += 1
        if e["status"] == "LOCKED":
            locked_users.add(e["username"])

    total = len(entries)
    success = counts["SUCCESS"]
    failed = counts["FAILED"]
    locked = counts["LOCKED"]
    invalid = counts["INVALID FORMAT"]
    rate = (success / total * 100) if total else 0

    print(f"  Total attempts      : {total}")
    print(f"  ✅ Successful logins : {success}")
    print(f"  ❌ Failed logins     : {failed}")
    print(f"  🔒 Locked attempts   : {locked}")
    print(f"  ⚠️  Invalid format    : {invalid}")
    print(f"  📈 Success rate      : {rate:.1f}%")
    if locked_users:
        print(f"  🚫 Locked accounts   : {', '.join(sorted(locked_users))}")


def main():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Roll No: {ROLL} | Timestamp: {ts}")
    print("\n[ANALYSIS] Credential Stuffing Simulator — Results Analysis")
    print("=" * 65)

    all_entries = []
    for fname in LOG_FILES:
        path = os.path.join(LOG_DIR, fname)
        entries = parse_log_file(path)
        if entries:
            label = fname.replace("_logs.txt", "").upper()
            print(f"\n  ── {label} ({path}) ──")
            print_report(label, entries)
            all_entries.extend(entries)

    if all_entries:
        print("\n  ── COMBINED TOTAL ──")
        print_report("ALL LOGS", all_entries)

    print("\n[ANALYSIS] Done. ✅")


if __name__ == "__main__":
    main()
