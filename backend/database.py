import sqlite3
import os
from typing import List, Dict

DB_NAME = "translations.db"

def get_connection(db_name: str = DB_NAME):
    return sqlite3.connect(db_name)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS translations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                target_language TEXT NOT NULL,
                translated_text TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def save_translation(text: str, target_language: str, translated_text: str):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
            INSERT INTO translations (text, target_language, translated_text)
            VALUES (?, ?, ?)
        """, (text, target_language, translated_text))
        conn.commit()

def get_stats() -> Dict[str, int]:
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
            SELECT target_language, COUNT(*) FROM translations GROUP BY target_language
        """)
        return {lang: count for lang, count in c.fetchall()}

def get_all_translations() -> List[Dict[str, str]]:
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
            SELECT text, target_language, translated_text, timestamp
            FROM translations ORDER BY timestamp DESC
        """)
        return [
            {
                "text": row[0],
                "target_language": row[1],
                "translated_text": row[2],
                "timestamp": row[3]
            }
            for row in c.fetchall()
        ]

def reset_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    if os.path.exists("translation_log.txt"):  # if logging to file is used
        os.remove("translation_log.txt")
    init_db()
