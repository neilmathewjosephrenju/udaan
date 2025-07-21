import streamlit as st
import requests

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
    "Arabic": "ar"
}

# Translation input
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
                "target_language": language_options[target_lang],
                "source_language": language_options[source_lang]
            }
        )
        if response.status_code == 200:
            st.success("Translation:")
            st.write(response.json()["translated_text"])
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

# Divider
st.markdown("---")

# Reset button
if st.button("Reset Logs & DB"):
    response = requests.delete("http://backend:8000/reset")
    if response.status_code == 200:
        st.success("Translation logs and database reset.")
    else:
        st.error("Failed to reset data.")

# Health & Stats
with st.expander("🔍 Health Check"):
    try:
        res = requests.get("http://backend:8000/health")
        st.write(res.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Health check failed: {e}")

with st.expander("📊 Translation Stats"):
    try:
        res = requests.get("http://backend:8000/stats")
        st.write(res.json())
    except requests.exceptions.RequestException as e:
        st.error(f"Stats fetch failed: {e}")
