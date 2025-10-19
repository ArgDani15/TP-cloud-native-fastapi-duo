from fastapi.testclient import TestClient
from app.main import app
import app.clients as clients

client = TestClient(app)

def test_create_and_list_orders(monkeypatch):
    monkeypatch.setattr(clients, "user_exists", lambda user_id: True)

    r = client.post("/orders", json={"user_id": 1, "item": "Book", "qty": 2})
    assert r.status_code == 201
    data = r.json()
    assert data["item"] == "Book"

    r2 = client.get("/orders")
    assert r2.status_code == 200
    assert any(o["item"] == "Book" for o in r2.json())
