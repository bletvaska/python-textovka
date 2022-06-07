from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_item_by_name
from items.features import MOVABLE


@dataclass
class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context: Context, name: str):
        # check if there is something to take
        if name == '':
            print('Neviem, čo chceš zobrať.')
            return

        # check if item is in room
        item = get_item_by_name(name, context.current_room.items)
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # if item is not MOVABLE
        if MOVABLE not in item.features:
            print(f'Tento predmet sa nedá zobrať.')
            return

        # take item
        context.current_room.items.remove(item)
        context.backpack.append(item)
        print(f'Do batohu si si vložil predmet {name}.')
