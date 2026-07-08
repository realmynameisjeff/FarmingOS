from pydantic import BaseModel


class Market(BaseModel):
    name: str
    ticker: str
    price: float
    change: float