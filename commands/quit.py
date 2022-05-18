from dataclasses import dataclass

import states


@dataclass
class Quit:
    name: str = 'koniec'
    description: str = 'skončenie programu'

    def exec(self, game_state):
        print('Naozaj chceš skončiť? (a/n)')
        line = input('>> ').lower().strip()
        if line in ('a', 'ano', 'y', 'yes'):
            print('Dakujem, ze si si zahral tuto fantasticku hru. Príď aj nabudúce.')
            game_state = states.QUIT
