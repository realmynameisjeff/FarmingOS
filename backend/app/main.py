from fastapi import FastAPI
from app.api import commodities, markets


app = FastAPI(
    title="FarmingOS API",
    description="Agriculture intelligence platform",
    version="0.1.0"
)


app.include_router(
    commodities.router,
    prefix="/api"
)


app.include_router(
    markets.router,
    prefix="/api"
)

@app.get("/")
def root():
    return {
        "message": "FarmingOS API is running",
        "status": "online"
    }
