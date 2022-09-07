#!/usr/bin/env python3

import states
from commands.about import About
from commands.commands import Commands
from commands.quit import Quit
from helpers import intro, outro, get_item_by_name
from items.features import USABLE
from items.newspaper import Newspaper
from items.revolver import Revolver
from items.whip import Whip


def main():
    intro()

    # game init
    game_state = states.PLAYING
    backpack = [
        Whip(),
        Revolver(),
        Newspaper()
    ]
    commands = [
        About(),
        Commands(),
        Quit()
    ]

    # game loop
    while game_state == states.PLAYING:
        # normalize input string
        line = input('> ').lower().lstrip().rstrip()

        if line == '':  # len(line) == 0
            # pass
            continue

        for command in commands:
            if command.name == line:
                command.exec()
                break
        else:
            print('Tento príkaz nepoznám.')

        # elif line == 'o hre':
        #     intro()
        #     print('Túto megašupabombašpica hru vytvoril v (c)2022 mladý nádejný a atraktívny programátor mirek')
        #     print('Hra je ďaľším pokračovaním nestarnúceho dobrodruha Indiana Jonesa. Tentokrát je jeho úlohou dostať '
        #           'sa zo zajatia fašistickej ponorky.')
        #
        # elif line == 'prikazy':
        #     print('V hre je možné použiť tieto príkazy:')
        #     print('* inventar - zobrazí obsah batohu')
        #     print('* koniec - ukončí rozohratú hru')
        #     print('* o hre - zobrazí informácie o hre')
        #     print('* pouzi - použije zvolený predmet')
        #     print('* preskumaj - preskúma zvolený predmet')
        #     print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
        #
        # elif line == 'pomoc':
        #     print('Ta pomôž si sám.')
        #
        # elif line == 'koniec':
        #     choice = input('Naozaj chceš skončiť? (a/n) ').lower().lstrip().rstrip()
        #     if choice == 'a':
        #         game_state = states.QUIT
        #
        # elif line == 'inventar':
        #     if len(backpack) == 0:  # backpack == []
        #         print('Batoh je prázdny.')
        #     else:
        #         print('V batohu máš:')
        #         for item in backpack:
        #             print(f'* {item.name}')
        #
        # elif line.startswith('preskumaj'):
        #     item_name = line.split('preskumaj', maxsplit=1)[1].lstrip()
        #
        #     if item_name == '':  # len(item_name) == 0
        #         print('Neviem, aký predmet chceš preskúmať.')
        #     else:
        #         item = get_item_by_name(item_name, backpack)
        #         if item is None:
        #             print('Taký predmet pri sebe nemáš.')
        #         else:
        #             print(item.description)
        #
        # elif line.startswith('pouzi'):
        #     item_name = line.split('pouzi', maxsplit=1)[1].lstrip()
        #     if item_name == '':
        #         print('Neviem čo chceš použiť.')
        #     else:
        #         item = get_item_by_name(item_name, backpack)
        #
        #         if item is None:
        #             print('Taký predmet tu nikde nevidím.')
        #         else:
        #             if USABLE not in item.features:
        #                 print('Tento predmet sa nedá použiť.')
        #             else:
        #                 item.use()
        #
        # else:
        #     print('Taký príkaz nepoznám.')

    outro()


if __name__ == '__main__':
    main()
