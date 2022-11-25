from dataclasses import dataclass

from helpers import get_room_by_name
from .command import Command


@dataclass
class Examine(Command):
    name: str = 'preskumaj'
    description: str = 'zobrazí informácie o zvolenom predmete'

    def exec(self, context):
        # if no item was entered
        if self.param == '':
            print("Neviem, čo chceš preskúmať.")
            return

        # if item is in backpack
        for item in context.backpack:
            if item.name == self.param:
                print(item.description)
                return

        # if item is in room
        room = get_room_by_name(context.current_room, context.rooms)
        for item in room.items:
            if item.name == self.param:
                print(item.description)
                return

        # no such item found
        print("Taký predmet tu nikde nevidím.")
