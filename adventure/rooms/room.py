from pydantic import BaseModel


class Room(BaseModel):
    name: str
    description: str
    exits: list = []
    items: list = []
