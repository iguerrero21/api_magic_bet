# from fastapi import APIRouter
# from requests import Session
# from app.database.models.user import User as DBUser
# from app.database.models.wallet import Wallet as DBWallet
# from app.database import db
# from fastapi import Depends


# router = APIRouter()

# @router.put("/api/new")
# async def new_user(user_id: int, name: str, username: str, email: str, db: Session = Depends(db.get_db)):
#     user = DBUser(user_id=user_id, name=name, username=username, email=email)
#     db.add(user)
#     db.commit()

#     wallet = DBWallet(user_id=user_id, balance=0)
#     db.add(wallet)
#     db.commit()
#     return {"Message": "Usuario creado"}
