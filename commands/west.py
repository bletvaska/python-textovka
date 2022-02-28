from dataclasses import dataclass
from typing import List

from .command import Command
from context import Context


@dataclass
class West(Command):
    name: str = 'zapad'
    # aliases: List[str]
    description: str = 'presunie sa do miestnosti na západ od aktuálnej'

    def exec(self, context: Context, param: str):
        raise NotImplementedError('Command was not yet implemented.')

