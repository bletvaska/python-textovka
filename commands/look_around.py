from dataclasses import dataclass

from context import Context
from utils import show_room
from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis miestnosti, v ktorej sa hráč nachádza'

    def exec(self, context: Context, arg: str):
        show_room(context.room)
