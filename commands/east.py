from dataclasses import dataclass

from .command import Command
from .helpers import _go


@dataclass
class East(Command):
    name: str = 'vychod'
    description: str = 'presunie sa do miestnosti na východ'

    def exec(self, context: dict, arg: str):
        _go(context, 'east')
