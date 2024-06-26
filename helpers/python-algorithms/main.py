from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
