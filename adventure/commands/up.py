from helpers import get_room_by_name
from rooms.directions import UP
from .command import Command


class Up(Command):
    name = 'hore'
    description = 'presunie sa do miestnosti hore od aktuálnej'

    def exec(self, context):
        if UP in context.current_room.exits:
            context.current_room = get_room_by_name(context.current_room.exits[UP], context.world)
            context.current_room.show()
        else:
            print('Tam sa nedá ísť.')
