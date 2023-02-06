#!/usr/bin/env python

print('Indiana Jones a jeho najväčšie Pythonovské dobrodružstvo')
line = None

while line != 'koniec':
    line = input('> ').lstrip().rstrip().lower()

    if line == '':  # len(line) == 0
        pass

    elif line == 'o hre':
        print('(c)2023 created by mirek')
        print('Dalšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')

    elif line == 'prikazy':
        print('V hre je možné použiť tieto príkazy:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

    elif line == 'koniec':
        choice = input('Naozaj chceš ukončiť túto hru? (a/n) ').lower().lstrip().rstrip()
        if choice in ('ano', 'a', 'yes', 'y'):
            break
        elif choice == 'nie':
            line = None
        else:
            print('Zle zadaná hodnota.')
            line = None

    else:
        print('Taký príkaz nepoznám.')

print('koniec')
