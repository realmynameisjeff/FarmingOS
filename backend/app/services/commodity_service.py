from app.models.commodity import Commodity


def get_commodities():
    return [
        Commodity(
            name="Corn",
            symbol="ZC",
            price=4.73,
            change=0.08
        ),
        Commodity(
            name="Soybeans",
            symbol="ZS",
            price=11.82,
            change=-0.12
        ),
        Commodity(
            name="Wheat",
            symbol="ZW",
            price=5.91,
            change=0.03
        )
    ]