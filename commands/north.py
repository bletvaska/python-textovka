from dataclasses import dataclass
from typing import List

from helpers import show_room
from .command import Command
from context import Context


@dataclass
class North(Command):
    name: str = 'sever'
    # aliases: List[str]
    description: str = 'presunie sa do miestnosti na sever od aktuálnej'

    def exec(self, context: Context, param: str):
        room_name = context.room['exits']['north']

        # je na sever prechod?
        if room_name is None:
            print('Tam sa nedá ísť.')
            return

        # prejdem na sever
        context.room = context.world[room_name]
        show_room(context.room)

        # append to history
        context.history.append(self.name)