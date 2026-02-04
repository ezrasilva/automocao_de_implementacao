from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Minha API de Engenharia de Software")

# Endpoint de saúde exigido para o Smoke Test posterior [cite: 333, 560]
@app.get("/health")
def health():
    return {"status": "ok"}

# Tarefa 2: Implementar GET /sum 
@app.get("/sum")
def sum_values(a: int, b: int):
    return {"result": a + b}