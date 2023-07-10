from fastapi import APIRouter
from app.database.schemas.transactions import DebitTransaction
from app.services.wallet_operations import perform_wallet_operation

router = APIRouter()

@router.post("/api/debit/{user_id}")
async def debit_wallet(user_id: int, transaction: DebitTransaction):
    return perform_wallet_operation(user_id, transaction.amount, action="debit")
