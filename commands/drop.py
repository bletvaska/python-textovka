from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_item_by_name
from items.features import MOVABLE


@dataclass
class Drop(Command):
    name: str = 'poloz'
    description: str = 'položí predmet z batohu do aktuálnej miestnosti'

    def exec(self, context: Context, name: str):
        # check if there is something to drop
        if name == '':
            print('Neviem, čo chceš položiť.')
            return

        # check if item is in backpack
        item = get_item_by_name(name, context.backpack)
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # drop item
        context.current_room.items.append(item)
        context.backpack.remove(item)
        print(f'Do miestnosti si položil predmet {name}.')
