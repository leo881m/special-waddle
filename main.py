import fastapi
from fastapi import FastAPI

app = fastapi.FastAPI()

@app.get("/")
def read_root() -> object:
    return {"Hello": "World"}
