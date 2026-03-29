# student_name: Jejo J
# roll_number: 727823tucy019
# project_name: Credential Stuffing Simulator
# date: 2026-03-29

"""
webapp/app.py
-------------
Flask web interface for the Credential Stuffing Simulator.
"""

import sys
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

# ✅ FIX 1: Correct path setup (points to project root)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

# ✅ FIX 2: Updated import (code → core)
from core.helper_modules.auth_simulator import AuthSimulator

app = Flask(__name__)

# ✅ Ensure logs directory exists at project root
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.get_json()

    raw = data.get("credentials", "").strip()
    if not raw:
        return jsonify({"error": "No credentials provided."}), 400

    # ✅ FIX 3: Proper absolute log path
    log_file_path = os.path.join(LOG_DIR, "webapp_logs.txt")

    sim = AuthSimulator(log_path=log_file_path)

    pairs = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue

        parts = line.split(",", 1)

        if len(parts) == 2:
            pairs.append((parts[0].strip(), parts[1].strip()))
        else:
            pairs.append((line, ""))  # INVALID FORMAT case

    results = sim.run_bulk(pairs)

    return jsonify({
        "results": results,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "roll": "727823tucy019",
    })


if __name__ == "__main__":
    print(f"Roll No: 727823tucy019 | Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # ✅ FIX 4: safer run (avoid debug crash if anything weird)
    app.run(debug=False, port=5000)
