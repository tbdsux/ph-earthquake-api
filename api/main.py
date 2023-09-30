from fastapi import FastAPI

from api.routers import latest

app = FastAPI()

app.include_router(latest.router)


@app.get("/")
async def main():
    return "Hello world"
