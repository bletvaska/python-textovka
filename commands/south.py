from dataclasses import dataclass

from .command import Command
from .helpers import _go


@dataclass
class South(Command):
    name: str = 'juh'
    description: str = 'presunie sa do miestnosti na juh'

    def exec(self, context: dict, arg: str):
        _go(context, 'south')
