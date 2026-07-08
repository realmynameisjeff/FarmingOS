from sqlalchemy import Column, Integer, String, Float
from app.database.base import Base


class MarketPrice(Base):

    __tablename__ = "market_prices"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    ticker = Column(
        String
    )

    price = Column(
        Float
    )

    change = Column(
        Float
    )