from dataclasses import dataclass

from helpers import get_current_room
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

        # if item is in room
        room = get_current_room(context)
        for item in room.items:
            if item.name == self.param:
                # is item movable?
                if MOVABLE not in item.features:
                    print('Tento predmet sa nedá zobrať.')
                    return

                # take item
                room.items.remove(item)
                context.backpack.append(item)

                print(f'Do batohu si si vložil {item.name}.')
                return

        print('Taký predmet tu nikde nevidím.')
