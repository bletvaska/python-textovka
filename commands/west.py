from dataclasses import dataclass

from context import Context
from .command import Command
from .helpers import _go


@dataclass
class West(Command):
    name: str = 'zapad'
    description: str = 'presunie sa do miestnosti na západ'

    def exec(self, context: Context, arg: str):
        _go(context, 'west')
