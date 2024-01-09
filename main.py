#!/usr/bin/env python3
import states
from commands import About, Commands, Quit
from helpers import intro, outro


# game initialization
game_state = states.PLAYING
commands = [
    About(),
    Commands(),
    Quit()
]

# game loop
intro()
while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()  # echo line | lower | lstrip | rstrip

    if line == '':  # if len(line) == 0:
        pass  # {}

    elif line == 'o hre':
        cmd = About()
        cmd.exec()

    elif line == 'prikazy':
        cmd = Commands()
        cmd.exec()

    elif line == 'koniec':
        cmd = Quit()
        cmd.exec()

    else:
        print('Taký príkaz nepoznám.')

outro()
