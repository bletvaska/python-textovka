#!/usr/bin/env python3
import states


def intro():
    """
    Shows intro.

    This function shows intro banner for the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")

    print("Indiana Jones and his Great Escape".center(70))


def outro():
    """
    Shows outro (credits).

    This functions shows credits at the end of the game. This is the last test, the player will see.
    """
    print('*-' * 35)
    print('Created by (c) mirek - A very talented young python programmer.')
    print('Please support his next magic project by sending some funds')
    print('(at least 100 Euros). He will create something.')


def main():
    # game init
    game_state = states.PLAYING

    # intro
    intro()

    print('Nachádzaš sa v miestnosti plnej ružových slonov. Aby si si neublížil, tak stena je pokrytá vankúšikmi. Tiež '
          'ružovými. Žiadne okno ti neposkytne rozkošný pohľad na vonkajšiu faunu a flóru.')

    # game loop
    while game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue  # pass

        elif line in ('o hre', 'about', 'info'):
            print('Ďalšie napínavé dobrodružstvo Indiana Jonesa. Tentokrát sa Indy ...')
            print('Túto nadupanú hru spáchal (c) mirek')

        elif line in ('prikazy', 'commands', 'help', '?',):
            print('Dostupné príkazy v hre:')
            print('* o hre - zobrazí informácie o hre')
            print('* koniec - ukončí hru')
            print('* prikazy - zobrazí zoznam aktuálne dostupných príkazov')
            print('* rozhliadni sa - zobrazí opis miestnosti')

        elif line in ('rozhliadni sa', 'look around'):
            print('Nachádzaš sa v miestnosti plnej ružových slonov. Aby si si neublížil, tak stena je pokrytá '
                  'vankúšikmi. Tiež ružovými. Žiadne okno ti neposkytne rozkošný pohľad na vonkajšiu faunu a flóru.')

        elif line in ('koniec', 'quit', 'q', 'bye'):
            x = input('Naozaj chceš skončiť? (a/n) ').strip().lower()
            if x in ('a', 'ano', 'y', 'yes'):
                game_state = states.QUIT
            else:
                print('Tak hráme ďalej...')

        else:
            print('Taký príkaz nepoznám.')

    # credits
    outro()


if __name__ == '__main__':
    main()
