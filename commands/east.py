from rooms import directions
from helpers import get_room_by_name
from .command import Command


class East(Command):
    name = 'vychod'
    description = 'presunie sa do miestnosti na východ od aktuálnej'

    def exec(self, context):
        # get current room
        room = context.current_room

        # is there exit going down?
        if directions.EAST in room.exits:
            context.current_room = get_room_by_name(room.exits[directions.EAST], context.rooms)
            context.current_room.show()

        else:
            print('Tam sa nedá ísť.')
