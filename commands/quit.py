from dataclasses import dataclass

import states
from .command import Command


@dataclass
class Quit(Command):
    name: str = 'koniec'
    description: str = 'ukončí rozohratú hru'

    def exec(self, game_state):
        confirm = input('Naozaj chceš skončiť? (ano/nie) ').strip().lower()
        if confirm in ('ano', 'áno', 'a', 'yes', 'y'):
            game_state = states.QUIT
            print('Ďakujem, že si si zahral túto fantastickú hru.')
        else:
            print('Tak nabudúce dávaj pozor na to, čo si skutočne želáš.')