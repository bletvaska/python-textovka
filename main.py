#!/usr/bin/env python

def main():
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                        and his Great Escape')
    print()

    line = None

    # game loop
    while line != 'koniec':
        line = input('> ').lstrip().rstrip().lower()

        # about, info, ?
        if line == 'o hre':
            print('(c)2022 created by mire(c) z koši(c)')
            print('Ďaľšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')

        # commands, help
        elif line == 'prikazy' or line == 'help':
            print('Zoznam príkazov v hre:')
            print('* koniec - skončenie programu')
            print('* o hre - vypíše info o hre')
            print('* prikazy - vypíše zoznam príkazov')

        # quit, exit, q, bye
        elif line not in ('koniec', ''):
            print('Taký príkaz nepoznám.')

    print('>> koniec')


if __name__ == '__main__':
    main()
