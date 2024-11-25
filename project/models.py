from sqlalchemy import Column, Integer, String, Float

from database import Base


class CryptoORM(Base):
    __tablename__ = "crypto"

    id = Column(Integer,primary_key=True, index= True)
    token = Column(String, index=True)
    price = Column(Float)



