from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from adventure.game_context import GameContext
from . import directions


class Room(BaseModel):
    name: str
    description: str
    items: list = []
    exits: dict = {}

    def act(self, context: 'GameContext'):
        pass

    def show(self):
        # room name and description
        print(f'Nachádzaš sa v miestnosti {self.name}.\n')
        print(f'{self.description}\n')

        # items
        if len(self.items) == 0:
            print('Nevidíš tu nič zvláštne.')
        else:
            print('Vidíš:')
            for item in self.items:
                print(f'* {item.name}')

        print()

        # exits
        if len(self.exits) == 0:
            print('Z tejto miestnosti nevedú žiadne východy.')
        else:
            print('Možné východy z miestnosti:')
            if directions.DOWN in self.exits:
                print(f'* dolu')
            if directions.UP in self.exits:
                print(f'* hore')
            if directions.EAST in self.exits:
                print(f'* východ')
            if directions.WEST in self.exits:
                print(f'* západ')
            if directions.SOUTH in self.exits:
                print(f'* juh')
            if directions.NORTH in self.exits:
                print(f'* sever')

        print()
