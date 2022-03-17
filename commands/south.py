from dataclasses import dataclass

from context import Context
from directions import Directions
from .command import Command
from .helpers import _go


@dataclass
class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh'

    def __post_init__(self):
        self.aliases += ['south', 'j']

    def exec(self, context: Context, arg: str):
        _go(context, Directions.SOUTH)
