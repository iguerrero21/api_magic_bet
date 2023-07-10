from pydantic import BaseModel

"""
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)

    wallet = relationship("Wallet", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
"""


# Pydantic model
class User(BaseModel):
    id: int
    user_id: int
    name: str
    username: str
    email: str

    class Config:
        orm_mode = True
