# Credential Stuffing Simulator

**Student:** Jejo J  
**Roll No:** 727823tucy019  
**Institution:** Sri Krishna College of Technology (SKCT)  
**Project:** Academic cybersecurity simulation — controlled environment only

---

## Overview

A fully self-contained **credential stuffing simulation** for academic study.
The tool demonstrates how credential stuffing attacks work in principle,
using a **dummy in-memory user database** — no real systems are targeted.

Key capabilities:
- Simulates login attempts against a fictional user DB
- Returns `SUCCESS / FAILED / LOCKED / INVALID FORMAT`
- Locks accounts after 3 consecutive failed attempts
- Logs every attempt with timestamps
- Flask web interface for interactive simulation
- CLI tool with 3 built-in test cases
- Analysis script that parses logs and prints statistics

---

## Screenshots

| Home Page | Results | Simulator |
|-----------|---------|-----------|
| [![Home Page](https://github.com/jejo205713/hacker-skct-727823tucy019/blob/main/screenshots/Home-page.png)](https://github.com/jejo205713/hacker-skct-727823tucy019/blob/main/screenshots/Home-page.png) | [![Results](https://github.com/jejo205713/hacker-skct-727823tucy019/blob/main/screenshots/Results.png)](https://github.com/jejo205713/hacker-skct-727823tucy019/blob/main/screenshots/Results.png) | [![Simulator](https://github.com/jejo205713/hacker-skct-727823tucy019/blob/main/screenshots/cred-stuff-simulator.png)](https://github.com/jejo205713/hacker-skct-727823tucy019/blob/main/screenshots/cred-stuff-simulator.png) |

---

## Project Structure

```
SKCT_727823tucy019_CredentialStuffingSimulator/
├── code/
│   ├── tool_main.py              ← CLI entry point (3 test cases)
│   └── helper_modules/
│       └── auth_simulator.py     ← Core auth simulation logic
├── webapp/
│   ├── app.py                    ← Flask app
│   ├── templates/index.html      ← Web UI
│   └── static/style.css          ← Stylesheet
├── setup_lab.py                  ← Pipeline step 1
├── run_tool.py                   ← Pipeline step 2
├── analyze_results.py            ← Pipeline step 3
├── pipeline_727823tucy019.yml    ← Pipeline definition
├── notebooks/demo.ipynb          ← Jupyter demo
├── screenshots/                  ← UI screenshots
├── requirements.txt
├── README.md
└── submission_form.txt
```

---

## Setup

```bash
# 1. Clone / unzip
cd SKCT_727823tucy019_CredentialStuffingSimulator

# 2. Install dependencies
pip install -r requirements.txt
```

---

## Running the Full Pipeline

```bash
python setup_lab.py && python run_tool.py && python analyze_results.py
```

Or equivalently:

```bash
# Step 1 — Environment setup
python setup_lab.py

# Step 2 — Run all test cases (CLI)
python run_tool.py

# Step 3 — Analyze logs
python analyze_results.py
```

---

## Running the CLI Tool Directly

```bash
python code/tool_main.py
```

This runs three test cases:
- **TC-1** — Mixed success + failure
- **TC-2** — All invalid credentials
- **TC-3** — Account lock scenario

Logs are saved to `logs/tc1_logs.txt`, `tc2_logs.txt`, `tc3_logs.txt`.

---

## Running the Flask Web App

```bash
cd webapp
python app.py
```

Then open `http://localhost:5000` in your browser.

Enter `username,password` pairs (one per line) and click **Run Simulation**.

---

## Dummy User Database

| Username | Password        |
|----------|-----------------|
| alice    | password123     |
| bob      | securepass!     |
| charlie  | ch4rlie_rocks   |
| diana    | D1@naSecure     |
| eve      | ev3pass         |
| frank    | frank2026       |
| grace    | Gr@ce_safe      |
| henry    | henry_pass99    |

---

## Disclaimer

This project is **strictly for academic purposes**.
It does not target, interact with, or affect any real system.
All data is fictional and hardcoded.
