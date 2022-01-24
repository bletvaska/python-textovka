#!/usr/bin/env python3


print('Indiana Jones and his Great Escape')

line = None

while line != 'koniec':

    line = input('> ').lower().lstrip().rstrip()

    if line == 'o hre':
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentkrát sa snaží ujsť z uzavretej kobky pod zemou.')
        print('Túto hru spáchal v 2022 (c) mirek.')

    elif line == 'prikazy':
        print('Zoznam dostupných príkazov:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam príkazov hry')

    elif line == 'koniec':
        pass

    else:
        print('Taký príkaz nepoznám.')

print('Created by (c)2022 mirek')
