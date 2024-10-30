from helpers import get_item_by_name
from .command import Command


class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context, param):
        if param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        item = get_item_by_name(param, context.current_room.items + context.backpack)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # action
        print(item.description)
