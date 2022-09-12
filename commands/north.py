from dataclasses import dataclass

from helpers import get_room_by_name
from world import world
from .command import Command


@dataclass
class North(Command):
    name: str = 'sever'
    description: str = 'presunie sa do miestnosti na sever od aktuálnej'

    def exec(self, context):
        target_room = context.current_room.north

        # is it possible to go north?
        if target_room is None:
            print('Tam sa nedá ísť.')
            return

        # lets move to north
        room = get_room_by_name(target_room, world)
        context.current_room = room
        room.show()
