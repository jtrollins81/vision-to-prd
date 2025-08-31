from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_prd_endpoint():
    payload = {
        "vision": "An AI that helps non-coders build products.",
        "goals": "Provide scaffolding, generate code, test, and deploy.",
        "target_audience": "Entrepreneurs and visionaries."
    }
    response = client.post("/prd/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "Product Requirements Document" in data["content"]
