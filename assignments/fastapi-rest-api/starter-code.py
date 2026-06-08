from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

class ItemOut(ItemCreate):
    id: int

items: Dict[int, ItemOut] = {}
next_id = 1

@app.get("/items", response_model=list[ItemOut])
def list_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: ItemCreate):
    global next_id
    new_item = ItemOut(id=next_id, **item.dict())
    items[next_id] = new_item
    next_id += 1
    return new_item
