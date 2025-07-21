# utils.py

import datetime

def log_translation(text: str, target_language: str, result: str):
    with open("translation.log", "a", encoding="utf-8") as f:
        log_entry = f"{datetime.datetime.now()} | {target_language} | {text} → {result}\n"
        f.write(log_entry)
