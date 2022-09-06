#!/usr/bin/env python3
import states


def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('          Indiana Jones and his Great U-boat Escape')
    print()


if __name__ == '__main__':
    intro()

    # game loop
    game_state = states.PLAYING
    while game_state == states.PLAYING:
        # normalize input string
        line = input('> ').lower().lstrip().rstrip()

        if line == '':  # len(line) == 0
            # pass
            continue

        elif line == 'o hre':
            print('Túto megašupabombašpica hru vytvoril v (c)2022 mladý nádejný a atraktívny programátor mirek')
            print('Hra je ďaľším pokračovaním nestarnúceho dobrodruha Indiana Jonesa. Tentokrát je jeho úlohou dostať '
                  'sa zo zajatia fašistickej ponorky.')

        elif line == 'prikazy':
            print('V hre je možné použiť tieto príkazy:')
            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o hre')
            print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

        elif line == 'pomoc':
            print('Ta pomôž si sám.')

        elif line == 'koniec':
            choice = input('Naozaj chceš skončiť? (a/n) ').lower().lstrip().rstrip()
            if choice == 'a':
                print("Ďakujem, že si si zahral túto špica hru. Stav sa aj nabudúce.")
                game_state = states.QUIT

        else:
            print('Taký príkaz nepoznám.')
