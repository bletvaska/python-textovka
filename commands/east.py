from dataclasses import dataclass
from typing import List

from helpers import show_room
from .command import Command
from context import Context


@dataclass
class East(Command):
    name: str = 'vychod'
    # aliases: List[str]
    description: str = 'presunie sa do miestnosti na vychod od aktuálnej'

    def exec(self, context: Context, param: str):
        room_name = context.room['exits']['east']

        # je na vychod prechod?
        if room_name is None:
            print('Tam sa nedá ísť.')
            return

        # prejdem na vychod
        context.room = context.world[room_name]
        show_room(context.room)

        # append to history
        context.history.append(self.name)
