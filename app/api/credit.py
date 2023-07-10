from fastapi import APIRouter
from app.database.schemas.transactions import CreditTransaction
from app.services.wallet_operations import perform_wallet_operation

router = APIRouter()

@router.post("/api/credit/{user_id}")
async def credit_wallet(user_id: int, transaction: CreditTransaction):
    return perform_wallet_operation(user_id, transaction.amount, action="credit")
