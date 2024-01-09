#!/usr/bin/env python3
import states
from commands import About, Commands
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
        choice = input('Naozaj chceš skončiť? (a/n) ').lower().strip()
        if choice in ('a', 'y', 'ano', 'yes'):
            print('Ďakujem, že si si zahral túto úžasnú (ukradnutú) hru.')
            game_state = states.QUIT

    else:
        print('Taký príkaz nepoznám.')

outro()
