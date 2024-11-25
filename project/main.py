from fastapi import FastAPI,Depends
from typing import  List
from sqlalchemy.orm import Session
import requests

from project.models import Base, CryptoORM
from database import engine, session_local
from project.schemas import  CryptoResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_crypto/", response_model=CryptoResponse)
async def create_crypto(symbol: str, db: Session = Depends(get_db)) -> CryptoResponse:
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': symbol})
    db_crypto = CryptoORM(token = response.json()["symbol"], price = float(response.json()["price"]))
    db.add(db_crypto)
    db.commit()
    db.refresh(db_crypto)

    return db_crypto


@app.get("/all_crypto/", response_model=List[CryptoResponse])
async def get_all_crypto(db: Session = Depends(get_db)):
    return db.query(CryptoORM).all()







