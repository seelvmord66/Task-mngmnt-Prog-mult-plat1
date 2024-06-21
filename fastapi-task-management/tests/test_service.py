from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/api/tasks/", json={"title": "Test Task", "description": "Test Description", "status": "Pendente"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_list_tasks():
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
