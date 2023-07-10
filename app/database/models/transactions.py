from sqlalchemy import Column, DateTime, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base
from datetime import datetime


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), index=True)
    wallet_id = Column(Integer, ForeignKey('wallets.user_id'), index=True)
    action = Column(String)
    amount = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    wallet = relationship("Wallet", back_populates="transactions")
