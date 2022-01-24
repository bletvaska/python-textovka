#!/usr/bin/env python3


print('Indiana Jones and his Great Escape')

line = None

while line not in ('koniec', 'quit', 'q', 'bye'):

    line = input('> ').lower().lstrip().rstrip()

    if line in ('o hre', 'about', 'info'):
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou.')
        print('Túto hru spáchal v 2022 (c) mirek.')

    elif line in ('prikazy', 'commands', 'help', '?'):
        print('Zoznam dostupných príkazov:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam príkazov hry')

    elif line in ('koniec', 'quit', 'q', 'bye'):
        line = input('Naozaj chceš skončiť? (a/n) ').lower().lstrip().rstrip()
        if line == 'a':
            line = 'koniec'

    else:
        print('Taký príkaz nepoznám.')

print('Created by (c)2022 mirek')
