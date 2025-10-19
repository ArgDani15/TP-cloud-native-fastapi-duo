from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_create_and_list_users():
 r = client.post("/users", json={"name": "Ada", "email": "ada@example.com"})
 assert r.status_code in (201, 409)
 r = client.get("/users")
 assert r.status_code == 200
 assert isinstance(r.json(), list)
