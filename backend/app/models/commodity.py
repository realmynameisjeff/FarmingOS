from pydantic import BaseModel


class Commodity(BaseModel):
    name: str
    symbol: str
    price: float
    change: float