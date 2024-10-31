from helpers import get_room_by_name
from rooms.direction import UP
from .command import Command


class Up(Command):
    name: str = 'hore'
    description: str = 'presunie sa do miestnosti hore od aktuálnej'

    def exec(self, context, param):
        if UP not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        room_name = context.current_room.exits[UP]
        context.current_room = get_room_by_name(room_name, context.world)
        context.current_room.show()

        context.history.append(self.name)
