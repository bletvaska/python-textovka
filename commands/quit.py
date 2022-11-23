from dataclasses import dataclass

from states import STATE_QUIT
from .command import Command


@dataclass
class Quit(Command):
    # fields
    name: str = 'koniec'
    description: str = 'ukončí hru'

    # methods
    def exec(self, backpack, commands):
        choice = input('Naozaj chceš ukončiť hru? (y/n) ').lstrip().rstrip().lower()
        if choice in ('y', 'yes', 'a', 'ano'):
            game_state = STATE_QUIT
