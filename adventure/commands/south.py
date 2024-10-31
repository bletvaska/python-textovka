from helpers import get_room_by_name
from rooms.direction import SOUTH
from .command import Command


class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh od aktuálnej'

    def exec(self, context, param):
        if SOUTH not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        room_name = context.current_room.exits[SOUTH]
        context.current_room = get_room_by_name(room_name, context.world)
        context.current_room.show()

        context.history.append(self.name)
