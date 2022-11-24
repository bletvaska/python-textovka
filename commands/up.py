from dataclasses import dataclass

import directions
from helpers import get_room_by_name
from .command import Command


@dataclass
class Up(Command):
    name: str = 'hore'
    description: str = 'presunie sa do miestnosti hore od aktuálnej'

    def exec(self, context):
        # get current room by its name
        room = get_room_by_name(context.current_room, context.rooms)

        # is there exit going down?
        if directions.UP in room.exits:
            context.current_room = room.exits[directions.UP]
            room = get_room_by_name(context.current_room, context.rooms)
            room.show()

        else:
            print('Tam sa nedá ísť.')
