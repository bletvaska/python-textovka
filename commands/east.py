from commands.command import Command
from helpers import get_room_by_name
from rooms import directions


class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti na vychod od aktuálnej'

    def exec(self, context):
        if directions.EAST not in context.current_room.exits:
            print('Tam sa nedá ísť.')
        else:
            room = context.current_room.exits[directions.EAST]
            context.current_room = get_room_by_name(room, context.world)
            context.current_room.show()
