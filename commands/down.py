from dataclasses import dataclass

from rooms import directions
from helpers import get_current_room
from .command import Command


@dataclass
class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        # get current room by its name
        room = get_current_room(context)

        # is there exit going down?
        if directions.DOWN in room.exits:
            context.current_room = room.exits[directions.DOWN]
            room = get_current_room(context)
            room.show()

        else:
            print('Tam sa nedá ísť.')
