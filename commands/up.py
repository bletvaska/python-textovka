from commands.command import Command
from helpers import get_room_by_name
from rooms import directions


class Up(Command):
    name: str = 'hore'
    description: str = 'presunie sa do miestnosti hore od aktuálnej'

    def exec(self, context):
        if directions.UP not in context.current_room.exits:
            print('Tam sa nedá ísť.')
        else:
            room = context.current_room.exits[directions.UP]
            context.current_room = get_room_by_name(room, context.world)
            context.current_room.show()
