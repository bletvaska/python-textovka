from rooms import directions
from helpers import get_room_by_name
from .command import Command


class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context):
        # get current room
        room = context.current_room

        # is there exit going down?
        if directions.WEST in room.exits:
            context.current_room = get_room_by_name(room.exits[directions.WEST], context)
            context.current_room.show()
            context.history.append(self.name)

        else:
            print('Tam sa nedá ísť.')
