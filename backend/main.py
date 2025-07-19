from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
import os

app = FastAPI()

# Allow cross-origin requests if needed (e.g. frontend fetches from /api)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (Astro build output)
app.mount("/", StaticFiles(directory="dist", html=True), name="static")

# Example API route
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

# Optional fallback: serve Astro's index.html for client-side routing
@app.get("/{full_path:path}")
def spa_fallback(full_path: str):
    index_path = Path("dist/client/index.html")
    if index_path.exists():
        return FileResponse(index_path)
    return {"detail": "Not Found"}
