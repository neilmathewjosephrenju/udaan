from datetime import datetime
from pathlib import Path

# Log file path (same folder as script unless overridden)
LOG_FILE = Path("translation_log.txt")

def log_translation(text: str, target_language: str, result: str):
    """
    Logs the translation activity to a file with a timestamp.

    Args:
        text (str): The original input text.
        target_language (str): The target language code (e.g., "hi", "fr").
        result (str): The translated result or fallback.
    """
    timestamp = datetime.now().isoformat()
    log_entry = f"{timestamp} | {target_language} | {text} → {result}\n"

    try:
        # Ensure the parent directory exists
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

        # Append the log entry
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(log_entry)

    except Exception as e:
        print(f"⚠️ Failed to write log entry: {e}")
