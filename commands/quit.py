from dataclasses import dataclass
from typing import List

import states
from context import Context
from .command import Command


@dataclass
class Quit(Command):
    name: str ='koniec'
    # aliases: List[str]
    description: str = 'ukončí rozohratú hru'

    def exec(self, context: Context):
        line = input('Naozaj chceš skončiť? (a/n) ').strip().lower()
        if line in ('a', 'ano', 'y', 'yes'):
            context.game_state = states.QUIT
        else:
            print('Tak hráme ďalej...')
