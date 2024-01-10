from pydantic import BaseModel

from items.item import Item


class Room(BaseModel):
    """
    Generic room model
    """
    # fields
    name: str
    description: str
    items: list[Item] = []
    exits: list = []

    def show(self):
        print(self.description)
        print('Vidíš:')
        for item in self.items:
            print(item.name)
