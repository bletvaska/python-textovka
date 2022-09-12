from dataclasses import dataclass

from helpers import get_room_by_name
from world import rooms
from .command import Command


@dataclass
class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti na východ od aktuálnej'

    def exec(self, context):
        target_room = context.current_room.east

        # is it possible to go east?
        if target_room is None:
            print('Tam sa nedá ísť.')
            return

        # lets move to east
        room = get_room_by_name(target_room, rooms)
        context.current_room = room
        room.show()
