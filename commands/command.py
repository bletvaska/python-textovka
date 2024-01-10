from pydantic import BaseModel

from items.item import Item
from rooms.room import Room


class Command(BaseModel):
    """
    Generic command of the game.
    """
    # fields
    name: str
    description: str
    param: str = None

    # methods
    def exec(self, room: Room, backpack: list[Item]) -> str:
        raise NotImplementedError('This method was not yet implemented.')
