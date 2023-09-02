from fastapi import FastAPI

from functions.eq_latest import earthquake_latest

app = FastAPI()


@app.get("/")
async def main():
    return "Hello world"


@app.get("/latest")
async def eq_latest():
    data = await earthquake_latest()

    return data
