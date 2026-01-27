
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

# 1) Crear usuario válido
r = client.post("/usuarios", json={
    "username": "ana_01",
    "email": "ana@email.com",
    "password": "Password123",
    "edad": 25,
    "newsletter": True
})
assert r.status_code == 201, r.text
user = r.json()