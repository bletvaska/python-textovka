from rich import print

from helpers import get_room_by_name
from rooms.directions import SOUTH
from .command import Command


class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti južne od aktuálnej'

    def exec(self, context):
        if SOUTH not in context.current_room.exits:
            print('[bold red]Tam sa nedá ísť.[/bold red]')
            return

        name = context.current_room.exits[SOUTH]
        context.current_room = get_room_by_name(name, context.world)
        context.current_room.show()
