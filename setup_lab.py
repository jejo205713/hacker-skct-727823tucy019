# student_name: Jejo J
# roll_number: 727823tucy019
# project_name: Credential Stuffing Simulator
# date: 2026-03-29

"""
setup_lab.py
------------
Pipeline Step 1 — Environment setup.
Creates required directories and verifies dependencies.
"""

import os
import sys
from datetime import datetime

ROLL = "727823tucy019"


def main():
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Roll No: {ROLL} | Timestamp: {ts}")
    print("\n[SETUP] Initializing Credential Stuffing Simulator lab environment...")

    # Create directories
    dirs = ["logs", "screenshots", "code/helper_modules"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"  ✔ Directory ensured: {d}/")

    # Check Python version
    py_ver = sys.version_info
    if py_ver < (3, 8):
        print(f"  ✗ Python 3.8+ required. Found: {py_ver.major}.{py_ver.minor}")
        sys.exit(1)
    print(f"  ✔ Python {py_ver.major}.{py_ver.minor}.{py_ver.micro} — OK")

    # Check Flask
    try:
        import flask
        print(f"  ✔ Flask {flask.__version__} — OK")
    except ImportError:
        print("  ✗ Flask not found. Run: pip install flask")
        sys.exit(1)

    # Create a sample credential file for CLI reference
    sample_creds = """\
# Sample credential list for Credential Stuffing Simulator
# Format: username,password (one per line)
alice,password123
bob,wrongpass
charlie,ch4rlie_rocks
diana,badpassword
alice,wrongagain
alice,lastchance
alice,password123
"""
    with open("sample_credentials.txt", "w") as f:
        f.write(sample_creds)
    print("  ✔ sample_credentials.txt created")

    print("\n[SETUP] Lab environment ready. ✅")


if __name__ == "__main__":
    main()
