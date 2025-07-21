# database.py

import sqlite3
import os 

DB_NAME = "translations.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
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
    conn.close()

def save_translation(text: str, target_language: str, translated_text: str):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO translations (text, target_language, translated_text)
        VALUES (?, ?, ?)
    """, (text, target_language, translated_text))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT target_language, COUNT(*) as count FROM translations GROUP BY target_language
    """)
    results = c.fetchall()
    conn.close()
    return {lang: count for lang, count in results}


def reset_database():
    if os.path.exists("translations.db"):
        os.remove("translations.db")
    if os.path.exists("translation_log.txt"):
        os.remove("translation_log.txt")
    init_db() 