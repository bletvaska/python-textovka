#!/usr/bin/env python3
import states

print(' ___           _ _                         _')
print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___')
print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
print(' | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\')
print('|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/')

print('                         and his Great Escape')

game_state = states.PLAYING

while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'o hre':
        print('(c)2022 created by mighty mire(c) the programmer')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát je jeho úlohou uniknúť z podzmeného väzenia, '
              'v ktorom sa náhodou ocitol.')

    elif line == 'prikazy':
        print('Dostupné príkazy v hre:')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

    elif line == 'koniec':
        confirm = input('Naozaj chceš skončiť? (ano/nie) ').strip().lower()
        if confirm in ('ano', 'áno', 'a', 'yes', 'y'):
            game_state = states.QUIT
            print('Ďakujem, že si si zahral túto fantastickú hru.')
        else:
            print('Tak nabudúce dávaj pozor na to, čo si skutočne želáš.')
        continue

    else:
        print('Tento príkaz nepoznám.')

print('Dobru chut.')
