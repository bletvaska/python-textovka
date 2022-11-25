from dataclasses import dataclass

from helpers import get_current_room, get_item_by_name
from items.features import MOVABLE
from .command import Command


@dataclass
class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš zobrať.")
            return

        # search for item in room
        room = get_current_room(context)
        item = get_item_by_name(self.param, room.items)

        # was item found?
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # take item
        room.items.remove(item)
        context.backpack.append(item)

        # render
        print(f'Do batohu si si vložil {item.name}.')
