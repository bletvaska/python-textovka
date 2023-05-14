from helpers import get_room_by_name
from rooms import directions
from .command import Command


class East(Command):
    name = 'vychod'
    description = 'presunie sa do miestnosti na východ od aktuálnej'

    def exec(self, context):
        # check if it is possible to go desired direction
        if directions.EAST not in context.current_room.exits:
            print('Tam sa nedá ísť.')
            return

        # get room by name
        name = context.current_room.exits[directions.EAST]
        room = get_room_by_name(name, context.world)

        # change current room
        context.current_room = room

        # look around in current room
        context.current_room.show()
