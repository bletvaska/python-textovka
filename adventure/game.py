#!/usr/bin/env python
import states
from commands import About, Commands, Quit
from helpers import intro, outro

intro()
game_state = states.PLAYING

# game loop
while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        pass

    elif line == 'o hre':
        game_state = About().exec()

    elif line == 'prikazy':
        game_state = Commands().exec()

    elif line == 'koniec':
        game_state = Quit().exec()

    else:
        print('Taký príkaz nepoznám.')

outro()
