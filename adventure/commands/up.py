from rich import print

from helpers import get_room_by_name
from rooms.directions import UP
from .command import Command


class Up(Command):
    name: str = 'hore'
    description: str = 'presunie sa do miestnosti hore od aktuálnej'

    def exec(self, context):
        if UP not in context.current_room.exits:
            print('[bold red]Tam sa nedá ísť.[/bold red]')
            return

        context.history.append(self.name)

        name = context.current_room.exits[UP]
        context.current_room = get_room_by_name(name, context.world)
        context.current_room.show()
