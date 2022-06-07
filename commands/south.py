from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_room_by_name


@dataclass
class South(Command):
    name: str = 'juh'
    description: str = 'prejde do miestnosti na juh od aktuálnej'

    def exec(self, context: Context, name):
        # check if it is possible to move to south
        if context.current_room.south is None:
            print('Tam sa nedá ísť.')
            return

        # go south
        context.current_room = get_room_by_name(context.current_room.south, context.world)
        context.current_room.show()
