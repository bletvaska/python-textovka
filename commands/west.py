from dataclasses import dataclass

from helpers import get_room_by_name
from world import rooms
from .command import Command


@dataclass
class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context):
        target_room = context.current_room.west

        # is it possible to go west?
        if target_room is None:
            print('Tam sa nedá ísť.')
            return

        # lets move to west
        room = get_room_by_name(target_room, rooms)
        context.current_room = room
        room.show()
