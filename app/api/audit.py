from fastapi import APIRouter, Depends
from app.database.models.transactions import Transaction as DBTransaction
from app.database import db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/api/audit/{user_id}")
async def get_user_transactions(user_id: int, db: Session = Depends(db.get_db)):
    transactions = db.query(DBTransaction).filter(DBTransaction.user_id == user_id).all()
    return {"transactions": transactions}
