from app.database.models.user import User as DBUser
from app.database import db


def new_user(user_id: int, name: str, username: str, email: str):
    user = DBUser(user_id=user_id, name=name, username=username, email=email)
    db.add(user)
    db.commit()
    return user
