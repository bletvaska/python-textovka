from dataclasses import dataclass

import states
from .command import Command


@dataclass
class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, context):
        choice = input('Naozaj chceš skončiť? (a/n) ').lower().lstrip().rstrip()
        if choice == 'a':
            context.game_state = states.QUIT
