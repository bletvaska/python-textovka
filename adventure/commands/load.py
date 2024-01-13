import json

from adventure.game_context import GameContext
from .command import Command


class Load(Command):
    name: str = 'nacitaj'
    description: str = 'načíta stav hry zo súboru'

    def exec(self, context) -> None:
        # if no filename was entered
        filename = self.param
        if filename == '':
            print("Nezadal si názov súboru.")
            return

        with open(filename, 'r') as file:
            # load saved game
            data = json.load(file)
            new_context = GameContext(**data)

            # update context
            context.backpack = new_context.backpack
            context.rooms = new_context.rooms
            context.current_room = new_context.current_room

        # render
        context.current_room.show()
        print('Pozícia bola úspešne načítaná.')
