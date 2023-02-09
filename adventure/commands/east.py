from helpers import get_room_by_name
from rooms.directions import EAST
from .command import Command


class East(Command):
    name = 'vychod'
    description = 'presunie sa do miestnosti na východ od aktuálnej'

    def exec(self, context):
        if EAST in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[EAST], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
