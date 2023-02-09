from pydantic import BaseModel

from items.item import Item
from .directions import NORTH, SOUTH, EAST, WEST, UP, DOWN


class Room(BaseModel):
    # fields
    name: str
    description: str
    items: list[Item] = []  # : list
    exits = {
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: None
    }

    def act(self, context):
        pass

    def show(self):
        """
        Shows the current room.
        """
        print(self.description)
        if self.items != []:  # len(current_room.items) > 0
            print('Vidíš:')
            for item in self.items:
                print(f'  {item.name}')
        else:
            print('Nevidíš tu nič zvláštne.')
