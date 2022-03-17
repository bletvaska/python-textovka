from dataclasses import dataclass

from context import Context
from directions import Directions
from .command import Command
from .helpers import _go


@dataclass
class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti na západ'

    def __post_init__(self):
        self.aliases += ['west', 'z']

    def exec(self, context: Context, arg: str):
        _go(context, Directions.WEST)
