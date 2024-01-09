from pydantic import BaseModel


class Room(BaseModel):
    """
    Generic room model
    """
    # fields
    name: str
    description: str
    items: list[str] = []
    exits: list = []
