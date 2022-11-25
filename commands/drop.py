from dataclasses import dataclass

from helpers import get_current_room, get_item_by_name
from .command import Command


@dataclass
class Drop(Command):
    name: str = 'poloz'
    description: str = 'vyberie zvolený predmet z batohu a položí ho do aktuálnej miestnosti'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš položiť.")
            return

        # search for item in room
        room = get_current_room(context)
        item = get_item_by_name(self.param, context.backpack)

        # was item found?
        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # drop item
        context.backpack.remove(item)
        room.items.append(item)

        # render
        print(f'Do miestnosti si položil {item.name}.')
