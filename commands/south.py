from commands.command import Command
from helpers import get_room_by_name
from rooms import directions


class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh od aktuálnej'

    def exec(self, context):
        if directions.SOUTH not in context.current_room.exits:
            print('Tam sa nedá ísť.')
        else:
            room = context.current_room.exits[directions.SOUTH]
            context.current_room = get_room_by_name(room, context.world)
            context.current_room.show()
