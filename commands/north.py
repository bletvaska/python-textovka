from dataclasses import dataclass

from context import Context
from directions import Directions
from .command import Command
from .helpers import _go


@dataclass
class North(Command):
    name: str = 'sever'
    description: str = 'presunie sa do miestnosti na sever'

    def __post_init__(self):
        self.aliases += ['north', 's']

    def exec(self, context: Context, arg: str):
        _go(context, Directions.NORTH)
