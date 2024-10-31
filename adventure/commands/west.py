from helpers import get_room_by_name
from rooms.direction import WEST
from .command import Command


class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context, param):
        if WEST not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        room_name = context.current_room.exits[WEST]
        context.current_room = get_room_by_name(room_name, context.world)
        context.current_room.show()
