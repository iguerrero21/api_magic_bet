from pydantic import BaseModel
from datetime import datetime

'''
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    action = Column(String)
    amount = Column(Float)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    wallet = relationship("Wallet", back_populates="transactions")
'''

# Pydantic models
class Transaction(BaseModel):
    user_id: int
    wallet_id: int
    action: str
    amount: float
    description: str
    timestamp: datetime

    class Config:
        orm_mode = True


class CreditTransaction(BaseModel):
    amount: float

class DebitTransaction(BaseModel):
    amount: float

class WithdrawTransaction(BaseModel):
    amount: float