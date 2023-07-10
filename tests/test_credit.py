from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_credit_wallet():
    # Datos de prueba
    user_id = 1
    amount = 100

    # Llamada al endpoint credit_wallet
    response = client.post(f"/api/credit/{user_id}", json={"amount": amount})

    # Verificar el código de respuesta y el mensaje de éxito
    assert response.status_code == 200
    assert response.json() == {"message": "Operación de billetera realizada con éxito"}


def test_credit_wallet_negative_amount():
    # Datos de prueba
    user_id = 1
    amount = -500  # Cantidad negativa

    # Llamada al endpoint credit_wallet
    response = client.post(f"/api/credit/{user_id}", json={"amount": amount})

    # Verificar el código de respuesta y el mensaje de error
    assert response.status_code == 400
    assert response.json() == {"detail": "El monto debe ser mayor o igual a 1"}
