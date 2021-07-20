#!/usr/bin/env python3

print(' ___           _ _                         _                       ')
print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ')
print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
print('|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/')

print('                                                     (c) 2021 mirek')


line = None

while line != 'koniec':
    line = input('> ').rstrip().lstrip().lower()

    if line == 'o hre':
        print('Hru spáchal  (c)2021 mirek')
        print('Ďalší príbeh Indiana Jonesa sa odohráva v temnej komôrke.')

    elif line == 'prikazy':
        print('Dostupné príkazy v hre:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o fantastickom autorovi hry a o hre samotnej')
        print('* prikazy - zobrazí zoznam príkazov, ktoré hra podporuje')

    elif line in ('koniec', ''):
        continue

    else:
        print('Taký príkaz nepoznám.')
