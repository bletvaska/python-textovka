import json

from context import Context
from .command import Command


class Load(Command):
    name = 'nahraj'
    description = 'nahrá uložený stav hry zo súboru'

    def exec(self, context):
        with open('save.json', 'r') as file:
            data = json.load(file)
            saved_context = Context(**data)

            # update existing context with loaded values
            context.backpack = saved_context.backpack
            context.current_room = saved_context.current_room
            context.world = saved_context.world

            # render
            context.current_room.show()

        print('Pozícia bola úspešne nahraná.')
