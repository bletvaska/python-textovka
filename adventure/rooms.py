from pydantic import BaseModel


class Room(BaseModel):
    # fields
    name: str
    description: str
    items = []  # : list
    exits = []  #: list

