from pydantic import BaseModel


class CryptoBase(BaseModel):
    token: str
    price: float


class CryptoResponse(CryptoBase):
    id: int


    class Config:
        from_attributes = True




