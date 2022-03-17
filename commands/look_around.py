from dataclasses import dataclass

from context import Context
from .command import Command


@dataclass
class LookAround(Command):
    name: str = 'rozhliadni sa'
    description: str = 'vypíše opis miestnosti, v ktorej sa hráč nachádza'

    def __post_init__(self):
        self.aliases += ['look around']

    def exec(self, context: Context, arg: str):
        context.room.show()
