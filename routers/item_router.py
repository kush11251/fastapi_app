from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str

@router.get("/items")
def get_items():
    return [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]