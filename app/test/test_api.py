from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Application root."}


def test_status():
    resp = client.get("/status")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Application status."}
