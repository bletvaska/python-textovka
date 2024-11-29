from rich import print

from helpers import get_room_by_name
from rooms.directions import DOWN
from .command import Command


class Down(Command):
    name: str = 'dolu'
    description: str = 'presunie sa do miestnosti dolu od aktuálnej'

    def exec(self, context):
        if DOWN not in context.current_room.exits:
            print('[bold red]Tam sa nedá ísť.[/bold red]')
            return

        context.history.append(self.name)

        name = context.current_room.exits[DOWN]
        context.current_room = get_room_by_name(name, context.world)
        context.current_room.show()
