from rich import print

from helpers import get_room_by_name
from rooms.directions import EAST
from .command import Command


class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti východne od aktuálnej'

    def exec(self, context):
        if EAST not in context.current_room.exits:
            print('[bold red]Tam sa nedá ísť.[/bold red]')
            return

        context.history.append(self.name)

        name = context.current_room.exits[EAST]
        context.current_room = get_room_by_name(name, context.world)
        context.current_room.show()
