from fastapi import FastAPI

app = FastAPI(
    title="FarmingOS API",
    description="Agriculture intelligence platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "FarmingOS API is running",
        "status": "online"
    }