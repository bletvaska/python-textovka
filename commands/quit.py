from dataclasses import dataclass

import states
from context import Context
from .command import Command


@dataclass
class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def __post_init__(self):
        self.aliases += ['quit', 'bye', 'q', 'ukoncit', 'skoncit']

    def exec(self, context: Context, arg: str):
        context.state = states.QUIT
