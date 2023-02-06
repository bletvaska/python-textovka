#!/usr/bin/env python
import states
from commands import About, Commands, Quit
from helpers import intro, outro

intro()
game_state = states.PLAYING

while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        pass

    elif line == 'o hre':
        About().exec()

    elif line == 'prikazy':
        Commands().exec()

    elif line == 'koniec':
        Quit().exec()

    else:
        print('Taký príkaz nepoznám.')

outro()
