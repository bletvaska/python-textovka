from dataclasses import dataclass

from helpers import get_room_by_name
from world import world
from .command import Command


@dataclass
class Up(Command):
    name: str = 'hore'
    description: str = 'presunie sa do miestnosti hore od aktuálnej'

    def exec(self, context):
        target_room = context.current_room.up

        # is it possible to go up?
        if target_room is None:
            print('Tam sa nedá ísť.')
            return

        # lets move
        context.current_room = get_room_by_name(target_room, world)
        context.current_room.show()
