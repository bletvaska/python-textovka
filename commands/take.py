from dataclasses import dataclass

from context import Context
from helpers import get_item_by_name
from items.features import MOVABLE


@dataclass
class Take:
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží si ho do batohu'

    def exec(self, context: Context):
        # init
        backpack = context.backpack
        room = context.current_room
        name = self.param

        # if no item was entered...
        if name == '':
            print('Neviem, co chceš zobrať.')
            return

        # is the item in room?
        item = get_item_by_name(name, room.items)

        if item is None:
            print('Taký predmet tu nevidím.')
            return

        # is it movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # vezmi item
        # vezmi item z miestnosti
        room.items.remove(item)

        # add item to backpack items
        backpack.append(item)

        # render
        print(f'Predmet {item.name} si si vložil do batohu.')
