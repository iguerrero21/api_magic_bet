from fastapi import APIRouter, Depends, HTTPException
from app.database import db
from app.database.models.user import User as DBUser
from app.database.models.wallet import Wallet as DBWallet
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/api/balance/{user_id}")
async def get_user_balance(user_id: int, db: Session = Depends(db.get_db)):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    wallet = db.query(DBWallet).filter(DBWallet.user_id == user_id).first()
    if not wallet:
        return {"message": "No transactions"}
    
    return {"balance": wallet.balance}

@router.get("/api/balance/users")
async def get_users_balance(db: Session = Depends(db.get_db)):
    users = db.query(DBUser).all()
    if not users:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    
    users_balance = []
    for user in users:
        wallet = db.query(DBWallet).filter(DBWallet.user_id == user.id).first()
        if not wallet:
            continue
        users_balance.append({"user_id": user.id, "balance": wallet.balance})
    
    return {"users_balance": users_balance}
