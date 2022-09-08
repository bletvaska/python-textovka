from dataclasses import dataclass

from helpers import get_room_by_name
from world import world
from .command import Command


@dataclass
class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        target_room = context.current_room.down

        # is it possible to go that way?
        if target_room is None:
            print('Tam sa nedá ísť.')
            return

        # let's go
        context.current_room = get_room_by_name(target_room, world)

        # show room
        context.current_room.show()
