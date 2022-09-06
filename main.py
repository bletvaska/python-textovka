#!/usr/bin/env python3
import states
from helpers import intro, outro

if __name__ == '__main__':
    intro()

    # game init
    game_state = states.PLAYING
    backpack = ['bic', 'revolver']

    # game loop
    while game_state == states.PLAYING:
        # normalize input string
        line = input('> ').lower().lstrip().rstrip()

        if line == '':  # len(line) == 0
            # pass
            continue

        elif line == 'o hre':
            intro()
            print('Túto megašupabombašpica hru vytvoril v (c)2022 mladý nádejný a atraktívny programátor mirek')
            print('Hra je ďaľším pokračovaním nestarnúceho dobrodruha Indiana Jonesa. Tentokrát je jeho úlohou dostať '
                  'sa zo zajatia fašistickej ponorky.')

        elif line == 'prikazy':
            print('V hre je možné použiť tieto príkazy:')
            print('* inventar - zobrazí obsah batohu')
            print('* koniec - ukončí rozohratú hru')
            print('* o hre - zobrazí informácie o hre')
            print('* preskumaj - preskúma zvolený predmet')
            print('* prikazy - zobrazí zoznam dostupných príkazov v hre')

        elif line == 'pomoc':
            print('Ta pomôž si sám.')

        elif line == 'koniec':
            choice = input('Naozaj chceš skončiť? (a/n) ').lower().lstrip().rstrip()
            if choice == 'a':
                game_state = states.QUIT

        elif line == 'inventar':
            if len(backpack) == 0:  # backpack == []
                print('Batoh je prázdny.')
            else:
                print('V batohu máš:')
                for item in backpack:
                    print(f'* {item}')

        elif line.startswith('preskumaj'):
            item_name = line.split('preskumaj', maxsplit=1)[1].lstrip()

            if item_name == '':  # len(item_name) == 0
                print('Neviem, aký predmet chceš preskúmať.')
            else:
                if item_name in backpack:
                    print(f'ta skumam {item_name}')
                else:
                    print('Taký predmet pri sebe nemáš.')
                # print('Tvoj neoceniteľný pomocník..!')

        else:
            print('Taký príkaz nepoznám.')

    outro()
