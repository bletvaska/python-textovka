from helpers import get_item_by_name
from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print('Neviem, čo chceš preskúmať.')
            return

        # search for item
        item = get_item_by_name(self.param, context.backpack + context.current_room.items)

        # not found
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return
        
        # render
        print(item.description)
