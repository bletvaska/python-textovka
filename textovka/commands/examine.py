from helpers import get_item_by_name
from items.features import EXAMINABLE
from .command import Command


class Examine(Command):
    name = 'preskumaj'
    description = 'preskúma zvolený predmet'

    def exec(self, context):
        # when no param was given
        # len(self.param) == 0
        if self.param == '':
            print('Neviem, aký predmet chceš preskúmať.')
            return

        # find item by name
        item = get_item_by_name(self.param, context.current_room.items + context.backpack)
        if item == None:
            print('Taký predmet tu nikde nevidím.')
            return

        # action
        print(item.description)

        # check if item is examinable
        if EXAMINABLE in item.features:
            item.examine(context)
