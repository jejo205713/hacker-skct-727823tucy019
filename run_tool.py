# student_name: Jejo J
# roll_number: 727823tucy019
# project_name: Credential Stuffing Simulator
# date: 2026-03-29

"""
run_tool.py
-----------
Pipeline Step 2 — Execute the credential stuffing simulation.
Calls tool_main.py which runs all three test cases.
"""

import subprocess
import sys
from datetime import datetime

ROLL = "727823tucy019"


def main():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Roll No: {ROLL} | Timestamp: {ts}")
    print("\n[RUN] Launching Credential Stuffing Simulator…")

    result = subprocess.run(
        [sys.executable, "code/tool_main.py"],
        capture_output=False,
    )

    if result.returncode == 0:
        print("\n[RUN] Simulation complete. ✅")
    else:
        print(f"\n[RUN] Simulation exited with code {result.returncode}. ❌")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
