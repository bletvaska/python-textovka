from dataclasses import dataclass

from helpers import get_current_room
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
                print(item.description)
                return

        print('Taký predmet tu nikde nevidím.')
