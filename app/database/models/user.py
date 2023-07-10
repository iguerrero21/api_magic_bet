from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, index=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)

    wallet = relationship("Wallet", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
