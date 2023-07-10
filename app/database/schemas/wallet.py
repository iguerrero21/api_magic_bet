from pydantic import BaseModel

'''
class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Float)
    frozen_balance = Column(Float)

    user = relationship("User", back_populates="wallet")
    transactions = relationship("Transaction", back_populates="wallet")
'''

# Pydantic model
class Wallet(BaseModel):
    user_id: int
    balance: float
    frozen_balance: float

    class Config:
        orm_mode = True
