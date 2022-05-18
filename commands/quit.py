from dataclasses import dataclass

import states
from context import Context


@dataclass
class Quit:
    name: str = 'koniec'
    description: str = 'ukončí hru'

    def exec(self, line, context: Context):
        print('Naozaj chceš skončiť? (a/n)')
        line = input('>> ').lower().strip()
        if line in ('a', 'ano', 'y', 'yes'):
            print('Dakujem, ze si si zahral tuto fantasticku hru. Príď aj nabudúce.')
            context.game_state = states.QUIT
