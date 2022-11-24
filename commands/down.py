from dataclasses import dataclass

from directions import DOWN
from helpers import get_room_by_name
from .command import Command


@dataclass
class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        # get current room by its name
        room = get_room_by_name(context.current_room, context.rooms)

        # is there exit going down?
        if DOWN in room.exits:
            context.current_room = room.exits[DOWN]
            room = get_room_by_name(context.current_room, context.rooms)
            room.show()

        else:
            print('Tam sa nedá ísť.')
