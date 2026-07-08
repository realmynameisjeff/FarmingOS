from fastapi import APIRouter
from app.services.commodity_service import get_commodities


router = APIRouter()


@router.get("/commodities")
def commodities():
    return get_commodities()