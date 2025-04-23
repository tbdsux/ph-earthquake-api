from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import data, latest

app = FastAPI()

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(latest.router)
app.include_router(data.router)


@app.get("/")
async def main():
    return "PHIVOLCS LATEST EARTHQUAKE INFORMATION (earthquake.phivolcs.dost.gov.ph) ... scraper"
