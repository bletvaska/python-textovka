from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_room_by_name


@dataclass
class North(Command):
    name: str = 'sever'
    description: str = 'prejde do miestnosti na sever od aktuálnej'

    def exec(self, context: Context, name):
        # check if it is possible to move to north
        if context.current_room.north is None:
            print('Tam sa nedá ísť.')
            return

        # go north
        context.current_room = get_room_by_name(context.current_room.north, context.world)
        context.current_room.show()
