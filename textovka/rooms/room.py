from rich import print
from pydantic import BaseModel

from rooms.directions import DOWN, UP, NORTH, SOUTH, EAST, WEST


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: dict = {}

    def act(self, context):
        pass

    def show(self):
        # print description
        print(self.description)

        # list items
        if len(self.items) == 0:
            print('Nevidíš tu nič zaujímavé.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'  [bold magenta]{item.name}[/bold magenta]')

        # list exits
        if self.exits == {}:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            dirs = []
            if DOWN in self.exits:
                dirs.append('dolu')
            if UP in self.exits:
                dirs.append('hore')
            if NORTH in self.exits:
                dirs.append('sever')
            if SOUTH in self.exits:
                dirs.append('juh')
            if EAST in self.exits:
                dirs.append('východ')
            if WEST in self.exits:
                dirs.append('západ')

            # render
            print('Možné východy z miestnosti:')
            for d in dirs:
                print(f'  [bold yellow]{d}[/bold yellow]')
