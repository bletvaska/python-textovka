from dataclasses import dataclass

from helpers import get_item_by_name
from items.features import MOVABLE
from .command import Command


@dataclass
class Take(Command):
    name: str = 'vezmi'
    description: str = 'vezme predmet z miestnosti a vloží ho do batohu'

    def exec(self, context):
        # is there a name of item given?
        if self.parameter == '':
            print('Neviem čo chceš vziať.')
            return

            # search for item by name
        item = get_item_by_name(self.parameter, context.current_room.items)

        # wat item found?
        if item is None:
            print('Taký predmet tu nikde nevidím.')
            return

        # is item movable?
        if MOVABLE not in item.features:
            print('Tento predmet sa nedá zobrať.')
            return

        # action
        # remove item from room
        context.current_room.items.remove(item)

        # insert item to backpack
        context.backpack.append(item)

        # render
        print(f'Do batohu si vložil predmet {item.name}.')
