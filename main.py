#!/usr/bin/env python
import states


def main():
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                        and his Great Escape')
    print()

    # game init
    game_state = states.PLAYING

    # game loop
    while game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue

        # about, info, ?
        elif line in ('o hre', 'about', 'info', '?'):
            print('(c)2022 created by mire(c) z koši(c)')
            print('Ďaľšie dobrodružstvo Indiana Jonesa je tentokrát vytvorené v jazyku Python.')

        # commands, help
        elif line in ('prikazy', 'help', 'commands'):
            print('Zoznam príkazov v hre:')
            print('* koniec - skončenie programu')
            print('* o hre - vypíše info o hre')
            print('* prikazy - vypíše zoznam príkazov')

        # quit, exit, q, bye
        elif line in ('koniec', 'quit', 'exit', 'q', 'bye'):
            game_state = states.QUIT

        else:
            print('Taký príkaz nepoznám.')

    print('>> koniec')


if __name__ == '__main__':
    main()
