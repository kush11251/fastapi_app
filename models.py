from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

class Item(BaseModel):
    id: int
    name: str