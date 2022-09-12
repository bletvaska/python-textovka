from dataclasses import dataclass

from helpers import get_item_by_name
from items.features import EXAMINABLE
from .command import Command


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'preskúma zvolený predmet'

    def exec(self, context):
        # name of item was given?
        if self.parameter == '':  # len(item_name) == 0
            print('Neviem, aký predmet chceš preskúmať.')
            return

        # is there a such item in room or backpack?
        item = get_item_by_name(self.parameter, context.current_room.items + context.backpack)
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # show description
        print(item.description)

        # is item examinable?
        if EXAMINABLE in item.features:
            item.examine(context)
