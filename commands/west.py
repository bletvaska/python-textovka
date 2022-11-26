from dataclasses import dataclass

from rooms import directions
from helpers import get_current_room
from .command import Command


@dataclass
class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context):
        # get current room by its name
        room = get_current_room(context)

        # is there exit going down?
        if directions.WEST in room.exits:
            context.current_room = room.exits[directions.WEST]
            room = get_current_room(context)
            room.show()

        else:
            print('Tam sa nedá ísť.')
