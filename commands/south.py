from dataclasses import dataclass

from rooms import directions
from helpers import get_room_by_name
from .command import Command


@dataclass
class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh od aktuálnej'

    def exec(self, context):
        # get current room
        room = context.current_room

        # is there exit going down?
        if directions.SOUTH in room.exits:
            context.current_room = get_room_by_name(room.exits[directions.SOUTH], context.rooms)
            context.current_room.show()

        else:
            print('Tam sa nedá ísť.')
