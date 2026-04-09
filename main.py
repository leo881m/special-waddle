from fastapi import fastAPI
import random

app = fastapi.FastAPI()


@app.get("/")
async def read_root() -> object:
    return {"Hello": "World"}


@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "numeroAleatorio": random.randint(0, 1000)}