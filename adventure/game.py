#!/usr/bin/env python
import states
from commands import About, Commands, Quit
from helpers import intro, outro

# intro
intro()

# init
game_state = states.PLAYING
commands = [
    About(),
    Commands(),
    Quit()
]

# game loop
while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        continue

    for command in commands:
        if command.name == line:
            game_state = command.exec()
            break
    else:
        print('Taký príkaz nepoznám.')

outro()
