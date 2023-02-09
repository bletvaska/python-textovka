from helpers import get_room_by_name
from rooms.directions import DOWN
from .command import Command


class Down(Command):
    name = 'dolu'
    description = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        if DOWN in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[DOWN], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
