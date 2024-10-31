from helpers import get_room_by_name
from rooms.direction import NORTH
from .command import Command


class North(Command):
    name: str = 'sever'
    description: str = 'presunie sa do miestnosti na sever od aktuálnej'

    def exec(self, context, param):
        if NORTH not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        room_name = context.current_room.exits[NORTH]
        context.current_room = get_room_by_name(room_name, context.world)
        context.current_room.show()
