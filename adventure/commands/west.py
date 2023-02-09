from helpers import get_room_by_name
from rooms.directions import WEST
from .command import Command


class West(Command):
    name = 'zapad'
    description = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context):
        if WEST in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[WEST], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
