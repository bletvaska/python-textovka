from helpers import get_room_by_name
from rooms import directions
from .command import Command


class Down(Command):
    name = 'dolu'
    description = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        # check if it is possible to go desired direction
        if directions.DOWN not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        # get room by name
        name = context.current_room.exits[directions.DOWN]
        room = get_room_by_name(name, context.world)

        # change current room
        context.current_room = room

        # look around in current room
        context.current_room.show()
