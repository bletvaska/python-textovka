from helpers import get_room_by_name
from rooms.directions import SOUTH
from .command import Command


class South(Command):
    name = 'juh'
    description = 'presunie sa do miestnosti na juh od aktuálnej'

    def exec(self, context):
        if SOUTH in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[SOUTH], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
