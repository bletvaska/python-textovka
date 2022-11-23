from dataclasses import dataclass

from states import STATE_QUIT
from .command import Command


@dataclass
class Quit(Command):
    # fields
    name: str = 'koniec'
    description: str = 'ukončí hru'

    # methods
    def exec(self, context):
        choice = input('Naozaj chceš ukončiť hru? (a/n) ').lstrip().rstrip().lower()
        if choice in ('y', 'yes', 'a', 'ano'):
            context.game_state = STATE_QUIT
