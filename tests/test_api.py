from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_prd_endpoint():
    response = client.post("/generate_prd", json={"vision": "Build a note-taking app"})
    assert response.status_code == 200
    data = response.json()
    assert "vision" in data
    assert data["vision"] == "Build a note-taking app"
    assert "prd" in data
