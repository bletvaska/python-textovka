from pydantic import BaseModel

from items.item import Item
from .directions import NORTH, SOUTH, EAST, WEST, UP, DOWN


class Room(BaseModel):
    # fields
    name: str
    description: str
    items: list[Item] = []  # : list
    exits: dict[str, str] = {}

    def act(self, context):
        pass

    def show(self):
        """
        Shows the current room.
        """
        # print description
        print(self.description)

        # print items
        if self.items != []:  # len(current_room.items) > 0
            print('Vidíš:')
            for item in self.items:
                print(f'  {item.name}')
        else:
            print('Nevidíš tu nič zvláštne.')

        # print exits
        if self.exits == {}:
            print('Z tejto miestnosti nevedú žiadne východy.')
        else:
            print('Môžeš ísť:')
            for ex in self.exits:
                print(f'  {ex}')
