from rich import print

from helpers import get_room_by_name
from rooms.directions import WEST
from .command import Command


class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti západne od aktuálnej'

    def exec(self, context):
        if WEST not in context.current_room.exits:
            print('[bold red]Tam sa nedá ísť.[/bold red]')
            return

        name = context.current_room.exits[WEST]
        context.current_room = get_room_by_name(name, context.world)
        context.current_room.show()
