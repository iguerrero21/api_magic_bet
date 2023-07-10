from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.models.user import User as DBUser
from app.database.models.wallet import Wallet as DBWallet
from app.database.models.transactions import Transaction as DBTransaction
from app.utils import api_client


def perform_wallet_operation(user_id: int, transaction_amount: float, action: str, db: Session):
    # Verificar la existencia del usuario en la base de usuarios externa
    if not api_client.verify_user_existence(user_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")


    # Verificar la existencia del usuario en la base de datos
    user = db.query(DBUser).filter(DBUser.user_id == user_id).first()
    if not user:
        # Obtener los datos del usuario desde la API externa
        user_data = api_client.get_user_data_from_external_api(user_id)

        # Crear un nuevo usuario en la base de datos
        user = DBUser(user_id=user_data["user_id"], name=user_data["name"], username=user_data["username"], email=user_data["email"])
        db.add(user)
        db.commit()

    # Obtener la billetera del usuario
    wallet = db.query(DBWallet).filter(DBWallet.user_id == user_id).first()
    if not wallet:
        # Crear una nueva billetera con saldo 0 para el usuario
        wallet = DBWallet(user_id=user.id, balance=0)
        db.add(wallet)
        db.commit()

    # Obtener la billetera del usuario
    # wallet = user.wallet
    # Realizar la operación en la billetera
    if action == "credit":
        wallet.balance += transaction_amount
    elif action == "debit":
        if wallet.balance < transaction_amount:
            raise HTTPException(status_code=400, detail="Fondos insuficientes")
        wallet.balance -= transaction_amount

    # Registrar la transacción en la base de datos
    transaction_data = DBTransaction(
        user_id=user_id,
        wallet_id=wallet.id,
        action=action,
        amount=transaction_amount,
        description=""
    )
    db.add(transaction_data)
    db.commit()

    return {"message": "Operación de billetera realizada con éxito"}
