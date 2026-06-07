import sqlite3
import os

# database path
DB_PATH = "database/interview.db"

def init_db():
    """
    Create SQLite database if doesen't exist
    """

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Table to store interview results
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   score TEXT,
                   feedback TEXT
                   )
                   """
    )

    conn.commit()
    conn.close

def save_interview(name, score, feedback):
    """
    save interview results into database
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews (name, score, feedback)
    VALUES (?, ?, ?)
    """, (name, score, feedback))

    conn.commit()
    conn.close()
