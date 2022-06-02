#!/usr/bin/env python3
import states
from helpers import intro, outro, get_item_by_name
from items import Whip, Revolver, Newspaper

intro()
game_state = states.PLAYING
backpack = [
    Whip(),
    Revolver(),
    Newspaper()
]

while game_state == states.PLAYING:
    line = input('> ').lower().lstrip().rstrip()

    if line == '':  # len(line) == 0
        continue

    elif line == 'inventar':
        if backpack == []:  # len(backpack) == 0:
            print('Batoh je prázdny.')
        else:
            print('V batohu máš:')
            for item in backpack:
                print(f'* {item.name}')

    elif line == 'o hre':
        print('(c)2022 created by mighty mire(c) the programmer')
        print('Ďalšie dobrodružstvo Indiana Jonesa. Tentokrát je jeho úlohou uniknúť z podzmeného väzenia, '
              'v ktorom sa náhodou ocitol.')

    elif line.startswith('pouzi'):
        name = line.split('pouzi')[1].lstrip()

        # check if there is something to examine 😉
        if name == '':
            print('Neviem, čo chceš použiť.')
        else:
            # check if item is in backpack
            item = get_item_by_name(name, backpack)
            if item is None:
                print('Taký predmet tu nikde nevidím.')
            else:
                print(f'Používam predmet {item.name}.')

    elif line.startswith('preskumaj'):
        name = line.split('preskumaj')[1].lstrip()

        # check if there is something to examine ;)
        if name == '':
            print('Neviem, aký predmet chceš preskúmať.')
        else:
            # check if item is in backpack
            item = get_item_by_name(name, backpack)
            if item is None:
                print('Taký predmet pri sebe nemáš.')
            else:
                print(item.description)

    elif line == 'prikazy':
        print('Dostupné príkazy v hre:')
        print('* inventar - zobrazí obsah hráčovho batohu')
        print('* koniec - ukončí rozohratú hru')
        print('* o hre - zobrazí informácie o hre')
        print('* pouzi - použije zvolený predmet')
        print('* preskumaj - zobrazí opis zvoleného predmetu')
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

outro()
