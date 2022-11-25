from dataclasses import dataclass

from rooms import directions
from helpers import get_room_by_name
from .command import Command


@dataclass
class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh od aktuálnej'

    def exec(self, context):
        # get current room by its name
        room = get_room_by_name(context.current_room, context.rooms)

        # is there exit going down?
        if directions.SOUTH in room.exits:
            context.current_room = room.exits[directions.SOUTH]
            room = get_room_by_name(context.current_room, context.rooms)
            room.show(context)

        else:
            print('Tam sa nedá ísť.')
