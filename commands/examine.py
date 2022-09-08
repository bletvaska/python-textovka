from dataclasses import dataclass

from helpers import get_item_by_name
from .command import Command


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'preskúma zvolený predmet'

    def exec(self, context):
        if self.parameter == '':  # len(item_name) == 0
            print('Neviem, aký predmet chceš preskúmať.')
        else:
            item = get_item_by_name(self.parameter, context.current_room.items + context.backpack)
            if item is None:
                print('Taký predmet pri sebe nemáš.')
            else:
                print(item.description)
