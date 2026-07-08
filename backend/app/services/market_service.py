from app.models.market import Market


def get_markets():

    return [
        Market(
            name="Corn",
            ticker="ZC",
            price=4.73,
            change=0.08
        ),
        Market(
            name="Soybeans",
            ticker="ZS",
            price=11.82,
            change=-0.12
        ),
        Market(
            name="Wheat",
            ticker="ZW",
            price=5.91,
            change=0.03
        )
    ]