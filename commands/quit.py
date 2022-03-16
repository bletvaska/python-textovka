from dataclasses import dataclass

import states
from context import Context
from .command import Command


@dataclass
class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, context: Context, arg: str):
        context.state = states.QUIT
