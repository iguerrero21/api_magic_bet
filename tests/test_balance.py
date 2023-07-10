from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_user_balance():
    response = client.get("/api/balance/1")
    assert response.status_code == 200
    assert response.json() == {"balance": 7000}


def test_get_user_balance_user_not_found():
    response = client.get("/api/balance/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuario no encontrado"}


def test_get_users_balance():
    response = client.get("/api/balance/users")
    assert response.status_code == 200
    assert response.json() == {
        "users_balance": [{"user_id": 1, "balance": 7000}, {"user_id": 2, "balance": 0}]
    }
