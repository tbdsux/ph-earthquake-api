from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import data, latest

api_app = FastAPI()

# Setup CORS
api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_app.include_router(latest.router)
api_app.include_router(data.router)


@api_app.get("/")
async def main():
    return "PHIVOLCS LATEST EARTHQUAKE INFORMATION (earthquake.phivolcs.dost.gov.ph) ... scraper"


app = FastAPI()
app.mount("/api", api_app)
