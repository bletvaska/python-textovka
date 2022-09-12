from dataclasses import dataclass

from helpers import get_room_by_name
from world import rooms
from .command import Command


@dataclass
class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh od aktuálnej'

    def exec(self, context):
        target_room = context.current_room.south

        # is it possible to go south?
        if target_room is None:
            print('Tam sa nedá ísť.')
            return

        # lets move to south
        room = get_room_by_name(target_room, rooms)
        context.current_room = room
        room.show()
