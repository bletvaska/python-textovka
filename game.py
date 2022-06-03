#!/usr/bin/env python3
import states
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from helpers import intro, outro, get_item_by_name
from items.features import USABLE
from items.newspaper import Newspaper
from items.revolver import Revolver
from items.whip import Whip


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
        cmd = Inventory()
        cmd.exec(backpack)

    elif line == 'o hre':
        cmd = About()
        cmd.exec()

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
                if USABLE in item.features:
                    item.use()
                else:
                    print(f'Tento predmet sa nedá použiť.')

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
        Commands().exec()

    elif line == 'koniec':
        Quit().exec(game_state)

    else:
        print('Tento príkaz nepoznám.')

outro()
