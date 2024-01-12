from commands.command import Command
from helpers import get_room_by_name
from rooms import directions


class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        if directions.DOWN not in context.current_room.exits:
            print('Tam sa nedá ísť.')
        else:
            room = context.current_room.exits[directions.DOWN]
            context.current_room = get_room_by_name(room, context.world)
            context.current_room.show()
