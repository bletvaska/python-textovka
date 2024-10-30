from typing import TYPE_CHECKING

from rooms.direction import TR_TABLE

if TYPE_CHECKING:
    from game_context import GameContext

from pydantic import BaseModel
from rich import print

from items.item import Item


class Room(BaseModel):
    name: str
    description: str
    items: list[Item] = []
    exits: dict = {}

    def act(self, context: 'GameContext'):
        pass

    def show(self):
        # render description
        print(self.description)

        # render items
        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš: ')
            for item in self.items:
                print(f'  * [bold magenta]{item.name}[/bold magenta]')

        # render exits
        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti: ')
            for ex in self.exits:
                print(f'* [bold yellow]{TR_TABLE[ex]}[/bold yellow]')
                # if ex == DOWN:
                #     print(f'* [bold yellow]dolu[/bold yellow]')
                # elif ex == UP:
                #     print(f'* [bold yellow]hore[/bold yellow]')
                # elif ex == NORTH:
                #     print(f'* [bold yellow]sever[/bold yellow]')
                # elif ex == SOUTH:
                #     print(f'* [bold yellow]juh[/bold yellow]')
                # elif ex == WEST:
                #     print(f'* [bold yellow]západ[/bold yellow]')
                # elif ex == EAST:
                #     print(f'* [bold yellow]východ[/bold yellow]')
