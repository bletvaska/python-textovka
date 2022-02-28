from dataclasses import dataclass
from typing import List

from helpers import show_room
from .command import Command
from context import Context


@dataclass
class West(Command):
    name: str = 'zapad'
    # aliases: List[str]
    description: str = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context: Context, param: str):
        room_name = context.room['exits']['west']

        # je na zapad prechod?
        if room_name is None:
            print('Tam sa nedá ísť.')
            return

        # prejdem na zapad
        context.room = context.world[room_name]
        show_room(context.room)

        # append to history
        context.history.append(self.name)
