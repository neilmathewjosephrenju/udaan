from deep_translator import GoogleTranslator
from langdetect import detect

# Translation service using deep-translator with langdetect logic
def translate_text(text: str, target_language: str) -> str:
    try:
        # Detect source language
        detected_language = detect(text)

        # If the text is already in the target language
        if detected_language == target_language:
            return f"✅ The text is already in the target language ({target_language})."

        # Perform translation
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated

    except Exception as e:
        # Fallback in case of failure
        mock_dict = {
            "ta": "வணக்கம்",
            "hi": "नमस्ते",
            "kn": "ನಮಸ್ಕಾರ",
            "bn": "নমস্কার",
            "fr": "Bonjour"
        }
        fallback = mock_dict.get(target_language, "[unsupported language]")
        return f"{fallback} - {text} [fallback due to: {str(e)}]"
