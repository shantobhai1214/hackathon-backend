from fastapi.testclient import TestClient

from app.main import app


def test_ping_endpoint():
    client = TestClient(app)
    response = client.get("/api/v1/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert isinstance(data["uptime"], int)
    assert isinstance(data["timestamp"], int)
