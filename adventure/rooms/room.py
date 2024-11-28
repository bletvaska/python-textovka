from typing import TYPE_CHECKING
from pydantic import BaseModel
from rich import print

if TYPE_CHECKING:
    from game_context import GameContext
from items.item import Item


class Room(BaseModel):
    """
    Game room representation.
    """
    name: str
    description: str
    exits: dict = {}
    items: list[Item] = []

    def act(self, context: 'GameContext'):
        pass

    def show(self):
        print(self.description)

        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'* [bold magenta]{item.name}[/bold magenta]')

        if len(self.exits) == 0:
            print('Z miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti:')
            for exit in self.exits:
                print(f'* [bold yellow]{exit}[/bold yellow]')
