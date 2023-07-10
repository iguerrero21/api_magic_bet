from fastapi import APIRouter, Depends, HTTPException
from requests import Session
from app.database.schemas.transactions import DebitTransaction
from app.services.wallet_operations import perform_wallet_operation
from app.database import db


router = APIRouter()

@router.post("/api/debit/{user_id}")
async def debit_wallet(user_id: int, transaction: DebitTransaction, session: Session= Depends(db.get_db)):
    if transaction.amount < 1:
        raise HTTPException(status_code=400, detail="El monto debe ser mayor o igual a 1")
    
    return perform_wallet_operation(user_id, transaction.amount, action="debit", db = session)
