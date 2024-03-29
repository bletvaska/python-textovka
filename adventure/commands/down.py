from adventure.rooms import directions
from adventure.helpers import get_room_by_name
from .command import Command


class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        # get current room
        room = context.current_room

        # is there exit going down?
        if directions.DOWN in room.exits:
            context.current_room = get_room_by_name(room.exits[directions.DOWN], context)
            context.current_room.show()
            context.history.append(self.name)

        else:
            print('Tam sa nedá ísť.')
