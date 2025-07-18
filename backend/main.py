from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = Path(__file__).parent / "sample_data" / "articles.json"

@app.get("/api/articles/today")
def get_articles():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/api/tags")
def get_tags():
    return ["AI", "NLP", "Policy", "Research"]