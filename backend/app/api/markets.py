from fastapi import APIRouter
from app.services.market_service import get_markets


router = APIRouter()


@router.get("/markets")
def markets():

    return {
        "markets": get_markets()
    }