from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from services import translate_text
from database import (
    init_db, save_translation, get_stats,
    reset_database, get_all_translations
)
from fastapi.responses import JSONResponse
from datetime import datetime

# Initialize FastAPI app
app = FastAPI()

# Initialize database
init_db()

@app.get("/")
def root():
    return {"message": "Welcome to the Udaan translation backend!"}

# Request Models
class TranslationRequest(BaseModel):
    text: str
    target_language: str

class BulkTranslationRequest(BaseModel):
    items: List[TranslationRequest]

# Translation endpoint (single)
@app.post("/translate")
def translate(req: TranslationRequest):
    if len(req.text) > 1000:
        raise HTTPException(status_code=400, detail="Text exceeds 1000 characters")

    try:
        result = translate_text(req.text, req.target_language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

    save_translation(req.text, req.target_language, result)

    return {"translated_text": result}

# Bulk translation endpoint
@app.post("/translate/bulk")
def bulk_translate(req: BulkTranslationRequest):
    results = []
    for item in req.items:
        try:
            result = translate_text(item.text, item.target_language)
        except Exception as e:
            result = f"[Error translating: {str(e)}]"
        save_translation(item.text, item.target_language, result)
        results.append(result)
    return {"results": results}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Statistics endpoint
@app.get("/stats")
def stats():
    return get_stats()

# Reset logs and DB
@app.delete("/reset")
def reset():
    reset_database()
    return {"message": "Database and log have been reset"}

# ✅ Download logs from DB instead of in-memory list
@app.get("/download-logs")
def download_logs():
    logs = get_all_translations()
    return JSONResponse(content=logs)

# Optional: View logs in frontend
@app.get("/logs")
def view_logs():
    return {"logs": get_all_translations()}
