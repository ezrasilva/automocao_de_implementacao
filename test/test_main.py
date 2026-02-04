from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Teste para o endpoint de saúde [cite: 344]
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Tarefa 3: Criar teste para /sum [cite: 568]
def test_sum():
    response = client.get("/sum?a=5&b=10")
    assert response.status_code == 200
    assert response.json() == {"result": 15}