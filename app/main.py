from fastapi import FastAPI

from app.routers import data, latest

app = FastAPI()

app.include_router(latest.router)
app.include_router(data.router)


@app.get("/")
async def main():
    return "PHIVOLCS LATEST EARTHQUAKE INFORMATION (earthquake.phivolcs.dost.gov.ph) ... scraper"
