from rich import print

from helpers import get_room_by_name
from rooms.directions import NORTH
from .command import Command


class North(Command):
    name: str = 'sever'
    description: str = 'presunie sa do miestnosti severne od aktuálnej'

    def exec(self, context):
        if NORTH not in context.current_room.exits:
            print('[bold red]Tam sa nedá ísť.[/bold red]')
            return

        name = context.current_room.exits[NORTH]
        context.current_room = get_room_by_name(name, context.world)
        context.current_room.show()
