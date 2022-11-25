from dataclasses import dataclass

from helpers import get_room_by_name, get_current_room, get_item_by_name
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

        # search for item
        room = get_current_room(context)
        item = get_item_by_name(self.param, context.backpack + room.items)

        # was found?
        if item is None:
            print("Taký predmet tu nikde nevidím.")
            return

        # render
        print(item.description)
