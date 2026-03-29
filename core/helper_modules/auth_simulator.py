# student_name: Jejo J
# roll_number: 727823tucy019
# project_name: Credential Stuffing Simulator
# date: 2026-03-29

"""
auth_simulator.py
-----------------
Core authentication simulation module.
Simulates a dummy login system with account locking.
All credentials are fictional and hardcoded for academic demonstration.
"""

from datetime import datetime

# ─── Dummy User Database ──────────────────────────────────────────────────────
# Fictional credentials for simulation ONLY. Not real accounts.
USER_DB = {
    "alice": "password123",
    "bob": "securepass!",
    "charlie": "ch4rlie_rocks",
    "diana": "D1@naSecure",
    "eve": "ev3pass",
    "frank": "frank2026",
    "grace": "Gr@ce_safe",
    "henry": "henry_pass99",
}

MAX_ATTEMPTS = 3  # Lock after this many failures per account


class AuthSimulator:
    def __init__(self, log_path="logs.txt"):
        self.failed_attempts: dict[str, int] = {}   # username -> fail count
        self.locked_accounts: set[str] = set()
        self.log_path = log_path
        self._log_entries: list[str] = []

    # ── Internal helpers ─────────────────────────────────────────────────────

    def _log(self, username: str, password: str, status: str):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{ts}] username={username!r:15s} password={password!r:20s} status={status}"
        self._log_entries.append(entry)
        print(f"  {entry}")

    def _flush_log(self):
        with open(self.log_path, "a", encoding="utf-8") as fh:
            for entry in self._log_entries:
                fh.write(entry + "\n")
        self._log_entries.clear()

    # ── Core login simulation ────────────────────────────────────────────────

    def attempt_login(self, username: str, password: str) -> str:
        """
        Try to log in with given credentials.

        Returns one of:
            SUCCESS        – credentials matched
            FAILED         – wrong password (not yet locked)
            LOCKED         – account locked after MAX_ATTEMPTS failures
            INVALID FORMAT – username or password is empty/malformed
        """
        # Validate format
        username = username.strip()
        password = password.strip()
        if not username or not password:
            status = "INVALID FORMAT"
            self._log(username or "(empty)", password or "(empty)", status)
            self._flush_log()
            return status

        # Already locked?
        if username in self.locked_accounts:
            status = "LOCKED"
            self._log(username, password, status)
            self._flush_log()
            return status

        # Check credentials
        if USER_DB.get(username) == password:
            # Reset fail counter on success
            self.failed_attempts.pop(username, None)
            status = "SUCCESS"
        else:
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            if self.failed_attempts[username] >= MAX_ATTEMPTS:
                self.locked_accounts.add(username)
                status = "LOCKED"
            else:
                status = "FAILED"

        self._log(username, password, status)
        self._flush_log()
        return status

    def run_bulk(self, credential_pairs: list[tuple[str, str]]) -> list[dict]:
        """Run many credential pairs and return a list of result dicts."""
        results = []
        for username, password in credential_pairs:
            status = self.attempt_login(username, password)
            results.append({"username": username, "password": password, "status": status})
        return results

    def reset(self):
        """Clear state between test cases."""
        self.failed_attempts.clear()
        self.locked_accounts.clear()
        self._log_entries.clear()
