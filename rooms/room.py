from pydantic import BaseModel
from rich import print

from items.item import Item
from rooms.directions import DOWN, UP, WEST, EAST, SOUTH, NORTH


class Room(BaseModel):
    """
    Generic room model
    """
    # fields
    name: str
    description: str
    items: list[Item] = []
    exits: dict = {}

    def act(self, context):
        pass

    def show(self):
        print(self.description)
        print()

        # show items available in room
        if len(self.items) != 0:  # self.items != []
            print('Vidíš:')
            for item in self.items:
                print(f'* [bold magenta]{item.name}[/bold magenta]')
        else:
            print('Nevidíš tu nič zvláštne.')
        print()

        # show exits from room
        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            directions = []

            if NORTH in self.exits:
                directions.append('sever')
            if SOUTH in self.exits:
                directions.append('juh')
            if EAST in self.exits:
                directions.append('východ')
            if WEST in self.exits:
                directions.append('západ')
            if UP in self.exits:
                directions.append('hore')
            if DOWN in self.exits:
                directions.append('dolu')

            print('Možné východy z miestnosti:')
            for direction in directions:
                print(f'* [bold yellow]{direction}[/bold yellow]')
