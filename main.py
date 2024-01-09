#!/usr/bin/env python3
import states
from commands import About, Commands, Quit, Command
from helpers import intro, outro

intro()

game_state = states.PLAYING
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
