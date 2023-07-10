from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Float)
    frozen_balance = Column(Float, default=0)

    user = relationship("User", back_populates="wallet")
    transactions = relationship("Transaction", back_populates="wallet")
