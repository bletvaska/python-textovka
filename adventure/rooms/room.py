from typing import TYPE_CHECKING

from pydantic import BaseModel
from rich import print

if TYPE_CHECKING:
    from adventure.game_context import GameContext
from . import directions
from adventure.items.item import Item


class Room(BaseModel):
    name: str
    description: str
    items: list[Item] = []
    exits: dict[str, str] = {}

    def act(self, context: 'GameContext'):
        pass

    def show(self):
        # room name and description
        # print(f'Nachádzaš sa v miestnosti {self.name}.\n')
        print(f'{self.description}\n')

        # items
        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'  [bold magenta]{item}[/bold magenta]')

        print()

        # exits
        if len(self.exits) == 0:
            print('Z tejto miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti:')
            if directions.DOWN in self.exits:
                print(f'  [bold yellow]dolu[/bold yellow]')
            if directions.UP in self.exits:
                print(f'  [bold yellow]hore[/bold yellow]')
            if directions.EAST in self.exits:
                print(f'  [bold yellow]východ[/bold yellow]')
            if directions.WEST in self.exits:
                print(f'  [bold yellow]západ[/bold yellow]')
            if directions.SOUTH in self.exits:
                print(f'  [bold yellow]juh[/bold yellow]')
            if directions.NORTH in self.exits:
                print(f'  [bold yellow]sever[/bold yellow]')

        print()
