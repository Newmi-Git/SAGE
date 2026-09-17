import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "sage.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS command_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            command_text TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS action_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            tool_name TEXT NOT NULL,
            params TEXT,
            risk_level TEXT,
            result TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS llm_decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            command_text TEXT NOT NULL,
            matched INTEGER NOT NULL,
            tool_name TEXT,
            arguments TEXT,
            raw_response TEXT
        )
    """)

    conn.commit()
    conn.close()

def log_command(command_text: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO command_history (timestamp, command_text) VALUES (?, ?)",
        (datetime.now().isoformat(), command_text)
    )
    conn.commit()
    conn.close()

def log_action(tool_name: str, params: dict, risk_level: str, result: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO action_log (timestamp, tool_name, params, risk_level, result) VALUES (?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), tool_name, str(params), risk_level, str(result))
    )
    conn.commit()
    conn.close()

def log_llm_decision(command_text: str, decision: dict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO llm_decisions
           (timestamp, command_text, matched, tool_name, arguments, raw_response)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            datetime.now().isoformat(),
            command_text,
            int(decision.get("matched", False)),
            decision.get("tool_name"),
            str(decision.get("arguments")),
            decision.get("raw_response")
        )
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")