from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_orders_empty():
 r = client.get("/orders")
 assert r.status_code == 200
 assert isinstance(r.json(), list)
