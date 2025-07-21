import streamlit as st
import requests
import json
import matplotlib.pyplot as plt  # ✅ For graph

st.set_page_config(page_title="Udaan Translator", layout="centered")
st.title("🌐 Project Udaan - Translator")

# Language options
language_options = {
    "Auto-detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Bengali": "bn",
    "French": "fr",
    "Arabic": "ar",
    "Spanish": "es",
    "German": "de",
    "Chinese (Simplified)": "zh",
    "Russian": "ru",
    "Japanese": "ja",
    "Italian": "it",
    "Portuguese": "pt",
    "Malayalam": "ml",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu"
}

# Input
text = st.text_area("Enter text to translate", max_chars=1000)
source_lang = st.selectbox("Select source language", list(language_options.keys()), index=0)
target_lang = st.selectbox("Select target language", list(language_options.keys()), index=1)

if st.button("Translate"):
    if not text:
        st.warning("Please enter text to translate.")
    elif language_options[target_lang] == "auto":
        st.warning("Please select a valid target language (not auto).")
    else:
        response = requests.post(
            "http://backend:8000/translate",
            json={
                "text": text,
                "target_language": language_options[target_lang]
                # removed source_language
            }
        )
        if response.status_code == 200:
            st.success("Translation:")
            st.write(response.json()["translated_text"])
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

# 📥 Download logs as JSON
with st.expander("📥 Download Logs"):
    if st.button("Download Translation Logs (JSON)"):
        try:
            res = requests.get("http://backend:8000/download-logs")
            if res.status_code == 200:
                json_data = json.dumps(res.json(), indent=2)
                st.download_button(
                    label="Click to download logs as JSON",
                    data=json_data,
                    file_name="translation_logs.json",
                    mime="application/json"
                )
            else:
                st.error("Failed to download logs.")
        except requests.exceptions.RequestException as e:
            st.error(f"Download failed: {e}")

# Divider
st.markdown("---")

# 🔄 Reset button
if st.button("Reset Logs & DB"):
    response = requests.delete("http://backend:8000/reset")
    if response.status_code == 200:
        st.success("Translation logs and database reset.")
    else:
        st.error("Failed to reset data.")

# 🔍 Health check
with st.expander("🔍 Health Check"):
    try:
        res = requests.get("http://backend:8000/health")
        st.write(res.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Health check failed: {e}")

# 📊 Translation stats
with st.expander("📊 Translation Stats"):
    try:
        res = requests.get("http://backend:8000/stats")
        data = res.json()
        if not data:
            st.info("No stats to display yet.")
        else:
            languages = list(data.keys())
            counts = list(data.values())

            fig, ax = plt.subplots()
            bars = ax.bar(
                languages,
                counts,
                color=plt.cm.viridis([i / len(languages) for i in range(len(languages))])
            )
            ax.set_xlabel("Target Language Code")
            ax.set_ylabel("Number of Translations")
            ax.set_title("Number of Translations per Language")

            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1, f'{int(height)}',
                        ha='center', va='bottom')

            st.pyplot(fig)

            with st.expander("📋 Raw Stats Data"):
                st.json(data)

    except requests.exceptions.RequestException as e:
        st.error(f"Stats fetch failed: {e}")
