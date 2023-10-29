from fastapi.testclient import TestClient
from app.api.api import router

client = TestClient(router)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

    response_data = resp.json()
    assert response_data["status"] == "success"
    assert response_data["message"] == "Template application using FastAPI."


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

    response_data = resp.json()
    assert response_data["status"] == "success"
    assert isinstance(response_data["result"], list)
    assert response_data["message"] == "Application is healthy."
