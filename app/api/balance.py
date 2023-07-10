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
    
    wallet = user.wallet
    if not wallet:
        return {"message": "No transactions"}
    
    return {"balance": wallet.balance}
