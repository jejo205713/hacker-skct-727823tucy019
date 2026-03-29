# student_name: Jejo J
# roll_number: 727823tucy019
# project_name: Credential Stuffing Simulator
# date: 2026-03-29

"""
tool_main.py
------------
CLI entry-point for the Credential Stuffing Simulator.

Runs three test cases:
    TC-1  Mixed success + failure
    TC-2  All invalid / wrong credentials
    TC-3  Account lock scenario (same user, 3 bad attempts then good)

Each test case appends to its own log file AND to the master logs.txt.
"""

import sys
import os
from datetime import datetime

# Allow running from project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from code.helper_modules.auth_simulator import AuthSimulator

ROLL = "727823tucy019"


def header(title: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nRoll No: {ROLL} | Timestamp: {ts}")
    print("=" * 65)
    print(f"  {title}")
    print("=" * 65)


def run_test_case(tc_num: int, label: str, pairs: list[tuple[str, str]], log_file: str):
    header(f"TEST CASE {tc_num}: {label}")
    sim = AuthSimulator(log_path=log_file)

    # Also mirror logs to master logs.txt
    sim._log_entries  # just reference; we override log_path per TC

    results = []
    for user, pwd in pairs:
        status = sim.attempt_login(user, pwd)
        results.append((user, pwd, status))

    print(f"\n  Summary for TC-{tc_num}:")
    success = sum(1 for _, _, s in results if s == "SUCCESS")
    failed  = sum(1 for _, _, s in results if s == "FAILED")
    locked  = sum(1 for _, _, s in results if s == "LOCKED")
    invalid = sum(1 for _, _, s in results if s == "INVALID FORMAT")
    print(f"    Total : {len(results)}")
    print(f"    ✅ SUCCESS        : {success}")
    print(f"    ❌ FAILED         : {failed}")
    print(f"    🔒 LOCKED         : {locked}")
    print(f"    ⚠️  INVALID FORMAT : {invalid}")

    return results


def main():
    os.makedirs("logs", exist_ok=True)

    # ── Test Case 1: Mixed success + failure ─────────────────────────────────
    tc1_pairs = [
        ("alice",   "password123"),    # ✅ correct
        ("bob",     "wrongpass"),      # ❌ wrong
        ("charlie", "ch4rlie_rocks"),  # ✅ correct
        ("diana",   "badpassword"),    # ❌ wrong
        ("eve",     "ev3pass"),        # ✅ correct
        ("frank",   "wrong123"),       # ❌ wrong
        ("grace",   "Gr@ce_safe"),     # ✅ correct
        ("henry",   "nope"),           # ❌ wrong
    ]
    run_test_case(1, "Mixed Success + Failure", tc1_pairs, "logs/tc1_logs.txt")

    # ── Test Case 2: All invalid credentials ─────────────────────────────────
    tc2_pairs = [
        ("alice",    "notherpassword"),
        ("bob",      "12345"),
        ("charlie",  "wrongwrongwrong"),
        ("diana",    "hunter2"),
        ("eve",      "qwerty"),
        ("",         "somepass"),           # empty username → INVALID FORMAT
        ("frank",    ""),                   # empty password → INVALID FORMAT
        ("unknown",  "doesntexist"),        # user not in DB
    ]
    run_test_case(2, "All Invalid / Wrong Credentials", tc2_pairs, "logs/tc2_logs.txt")

    # ── Test Case 3: Account lock scenario ───────────────────────────────────
    tc3_pairs = [
        ("alice", "wrong1"),     # ❌ attempt 1
        ("alice", "wrong2"),     # ❌ attempt 2
        ("alice", "wrong3"),     # 🔒 locks on 3rd failure
        ("alice", "password123"),# 🔒 still locked even with correct pwd
        ("bob",   "wrong1"),     # ❌ bob attempt 1
        ("bob",   "securepass!"),# ✅ bob succeeds before lock
    ]
    run_test_case(3, "Account Lock Scenario", tc3_pairs, "logs/tc3_logs.txt")

    print("\n" + "=" * 65)
    print("  All test cases complete. Logs saved to logs/ directory.")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
