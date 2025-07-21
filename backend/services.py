from deep_translator import GoogleTranslator
from langdetect import detect
from utils import log_translation

# Fallback translations for common languages (in case of failure)
MOCK_TRANSLATIONS = {
    "ta": "வணக்கம்",
    "hi": "नमस्ते",
    "kn": "ನಮಸ್ಕಾರ",
    "bn": "নমস্কার",
    "fr": "Bonjour"
}

def translate_text(text: str, target_language: str) -> str:
    """
    Translates the given text into the target language.
    Uses GoogleTranslator with auto-detection, falls back to mock translations on error.
    Logs all translations.

    Args:
        text (str): Text to translate.
        target_language (str): Target language code (e.g., "hi", "ta").

    Returns:
        str: Translated text or fallback with explanation.
    """
    try:
        # Detect source language
        detected_language = detect(text)

        if detected_language == target_language:
            message = f"✅ The text is already in the target language ({target_language})."
            log_translation(text, target_language, message)
            return message

        # Attempt translation
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        log_translation(text, target_language, translated)
        return translated

    except Exception as e:
        # Fallback message if translation fails
        fallback = MOCK_TRANSLATIONS.get(target_language, "[unsupported language]")
        result = f"{fallback} - {text} [fallback: {str(e)}]"
        log_translation(text, target_language, result)
        return result
