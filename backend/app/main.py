from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.corrector import FrenchSpellCorrector

app = FastAPI(
    title="French Spell Corrector API",
    description="Automatic French spelling and grammar correction using NLP",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

corrector = FrenchSpellCorrector()

class TextInput(BaseModel):
    text: str


@app.post("/correct")
def correct_text(payload: TextInput):
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    return corrector.correct_text(payload.text)

@app.on_event("shutdown")
def shutdown_event():
    corrector.close()