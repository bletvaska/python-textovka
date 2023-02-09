from helpers import get_room_by_name
from rooms.directions import NORTH
from .command import Command


class North(Command):
    name = 'sever'
    description = 'presunie sa do miestnosti na sever od aktuálnej'

    def exec(self, context):
        if NORTH in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[NORTH], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
