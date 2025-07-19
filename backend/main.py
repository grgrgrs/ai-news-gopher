from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/articles")
def get_articles():
    return {"articles": [{"title": "Sample Article", "score": 0.9}]}

@app.get("/api/graph-data")
def get_graph_data():
    return {"nodes": [], "edges": []}