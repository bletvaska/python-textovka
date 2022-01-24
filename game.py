#!/usr/bin/env python3

import states


print('Indiana Jones and his Great Escape')

game_state = states.PLAYING

while game_state == states.PLAYING:

    # normalizing input string
    line = input('> ').lower().lstrip().rstrip()

    # empty input?
    if line == '':
        continue

    # about game
    elif line in ('o hre', 'about', 'info'):
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou.')
        print('Túto hru spáchal v 2022 (c) mirek.')

    # list of commands
    elif line in ('prikazy', 'commands', 'help', '?'):
        print('Zoznam dostupných príkazov:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam príkazov hry')

    # quit game
    elif line in ('koniec', 'quit', 'q', 'bye'):
        line = input('Naozaj chceš skončiť? (a/n) ').lower().lstrip().rstrip()
        if line == 'a':
            game_state = states.QUIT

    # unknown command
    else:
        print('Taký príkaz nepoznám.')

print('Created by (c)2022 mirek')
