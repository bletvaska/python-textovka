from dataclasses import dataclass

from context import Context
from directions import Directions
from .command import Command
from .helpers import _go


@dataclass
class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti na východ'

    def __post_init__(self):
        self.aliases += ['east', 'v']

    def exec(self, context: Context, arg: str):
        _go(context, Directions.EAST)
