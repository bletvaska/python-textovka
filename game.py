#!/usr/bin/env python3

if __name__ == '__main__':
    # banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("                       and his Great Escape                        ")
    print()

    # main loop
    line = None
    while line != 'koniec':
        # normalizing string
        line = input('> ').lower().strip()

        if line in ('', 'koniec'):
            continue

        elif line == 'o hre':
            print('(c)2021 created by mirek')
            print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrá zápasí s jazykom Python v tmavej miestnosti.')

        elif line == 'prikazy':
            print('Zoznam príkazov v hre:')
            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o hre')
            print('* prikazy - zobrazí príkazy, ktoré sa dajú použiť v hre')

        else:
            print('Taký príkaz nepoznám.')

    print('(c)2021 by mirek mocný programátor')

