from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_debit_wallet():
    # Datos de prueba
    user_id = 1
    amount = 50

    # Llamada al endpoint debit_wallet
    response = client.post(f"/api/debit/{user_id}", json={"amount": amount})

    # Verificar el código de respuesta y el mensaje de éxito
    assert response.status_code == 200
    assert response.json() == {"message": "Operación de billetera realizada con éxito"}


def test_debit_wallet_user_not_found():
    # Datos de prueba
    user_id = 999  # Usuario no existente
    amount = 50

    # Llamada al endpoint debit_wallet
    response = client.post(f"/api/debit/{user_id}", json={"amount": amount})

    # Verificar el código de respuesta y el mensaje de error
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuario no encontrado"}


def test_debit_wallet_invalid_amount():
    # Datos de prueba
    user_id = 1
    amount = -200  # Cantidad inválida

    # Llamada al endpoint debit_wallet
    response = client.post(f"/api/debit/{user_id}", json={"amount": amount})

    # Verificar el código de respuesta y el mensaje de error
    assert response.status_code == 400
    assert response.json() == {"detail": "El monto debe ser mayor o igual a 1"}
