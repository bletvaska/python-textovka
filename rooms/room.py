from pydantic import BaseModel
from rich import print

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

    def act(self, context):
        pass

    def show(self):
        print(self.description)
        print()

        if len(self.items) != 0:  # self.items != []
            print('Vidíš:')
            for item in self.items:
                print(f'* [bold magenta]{item.name}[/bold magenta]')
        else:
            print('Nevidíš tu nič zvláštne.')
