from helpers import get_room_by_name
from rooms.direction import EAST
from .command import Command


class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti na východ od aktuálnej'

    def exec(self, context, param):
        if EAST not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        room_name = context.current_room.exits[EAST]
        context.current_room = get_room_by_name(room_name, context.world)
        context.current_room.show()

        context.history.append(self.name)
