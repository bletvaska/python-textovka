from dataclasses import dataclass

from context import Context
from utils import get_item_by_name
from .command import Command


@dataclass
class Drop(Command):
    name: str = 'poloz'
    description: str = 'položí predmet z batohu do aktuálnej miestnosti'

    def exec(self, context: Context, arg: str):
        item_name = arg
        backpack = context.backpack['items']
        room = context.room

        # is there name given?
        if item_name == '':
            print('Neviem čo chceš položiť.')
            return

        # if no such item available
        item = get_item_by_name(item_name, backpack)
        if item is None:
            print('Taký predmet u seba nemáš.')
            return

        # update history
        context.history.append(f'POLOZ {item_name}')

        # remove item from backpack
        backpack.remove(item)

        # drop item in the room
        room['items'].append(item)

        # print out
        print(f'Predmet {item["name"]} si položil do miestnosti.')