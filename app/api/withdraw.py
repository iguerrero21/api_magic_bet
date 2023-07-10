from fastapi import APIRouter, Depends, HTTPException
from app.database.schemas.transactions import Transaction
from app.database.models.user import User as DBUser
from app.database.models.wallet import Wallet as DBWallet
from app.database.models.transactions import Transaction as DBTransaction
from app.database import db
from sqlalchemy.orm import Session
from app.services.conversion_maticusd import convert_to_usd

router = APIRouter()

@router.post("/api/withdraw/{user_id}")
async def withdraw_funds(user_id: int, transaction: Transaction, db: Session = Depends(db.get_db)):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    wallet = db.query(DBWallet).filter(DBWallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=400, detail="Billetera no encontrada")
    
    if wallet.balance - wallet.frozen_balance < transaction.withdraw:
        raise HTTPException(status_code=400, detail="Fondos insuficientes")
    
    wallet.frozen_balance += transaction.withdraw
    
    db.add(DBTransaction(
        user_id=user_id,
        wallet_id=wallet.id,
        action="withdraw",
        amount=transaction.withdraw,
        description="Retiro de fondos"
    ))
    db.commit()
    
    return {"message": "Retiro exitoso"}

@router.post("/api/withdraw-confirm/{user_id}")
async def confirm_withdrawal(user_id: int, db: Session = Depends(db.get_db)):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    wallet = db.query(DBWallet).filter(DBWallet.user_id == user_id).first()
    if not wallet:
        raise HTTPException(status_code=400, detail="Billetera no encontrada")
    
    if wallet.frozen_balance == 0:
        raise HTTPException(status_code=400, detail="No hay fondos congelados para confirmar el retiro")
    
    withdrawal_amount = wallet.frozen_balance
    wallet.balance -= withdrawal_amount
    wallet.frozen_balance = 0
    
    conversion_rate = convert_to_usd("MATIC", "USD")  # Realizar la conversión con la API externa
    
    withdrawed = {
        "USD": withdrawal_amount * conversion_rate,
        "MATIC": withdrawal_amount
    }
    
    db.add(DBTransaction(
        user_id=user_id,
        wallet_id=wallet.id,
        action="withdraw-confirm",
        amount=withdrawal_amount,
        description="Confirmación de retiro de fondos"
    ))
    db.commit()
    
    return {"message": "Retiro exitoso", "withdrawed": withdrawed, "conversion_rate": conversion_rate}
