from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_room_by_name


@dataclass
class East(Command):
    name: str = 'vychod'
    description: str = 'prejde do miestnosti na východ od aktuálnej'

    def exec(self, context: Context, name):
        # check if it is possible to move to east
        if context.current_room.east is None:
            print('Tam sa nedá ísť.')
            return

        # go east
        context.current_room = get_room_by_name(context.current_room.east, context.world)
        context.current_room.show()
