from pydantic import BaseModel


class Room(BaseModel):
    """
    Game room representation.
    """
    name: str
    description: str
    exits: list = []
    items: list = []
