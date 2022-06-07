from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_room_by_name


@dataclass
class West(Command):
    name: str = 'zapad'
    description: str = 'prejde do miestnosti na západ od aktuálnej'

    def exec(self, context: Context, name):
        # check if it is possible to move to west
        if context.current_room.west is None:
            print('Tam sa nedá ísť.')
            return

        # go west
        context.current_room = get_room_by_name(context.current_room.west, context.world)
        context.current_room.show()
