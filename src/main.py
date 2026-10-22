#!/usr/bin/env python
import states
# from states import PLAYING, QUIT
# from states import PLAYING as STATE_PLAYING
# import helpers
from helpers import intro
from commands.about import About


intro()

line = None
game_state = states.PLAYING

while game_state == states.PLAYING:
    line = input('> ').lstrip().rstrip().lower()

    if line == '':
        pass

    elif line == 'o hre':
        cmd = About()
        cmd.exec()

    elif line == 'prikazy':
        print('V hre je mozne pouzit tieto prikazy:')
        print('* o hre - zobrazi informacie o hre')
        print('* prikazy - zobrazi zoznam dostupnych prikazov v hre')
        print('* koniec - ukončí hru')

    elif line == 'koniec':
        choice = input('Naozaj chceš skončiť? (a/n) ').strip().lower()
        if choice == 'a':
            game_state = states.QUIT

    else:
        print('Taký príkaz nepoznám')

outro()
