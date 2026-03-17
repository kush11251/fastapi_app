from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str

@router.get("/users")
def get_users():
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]