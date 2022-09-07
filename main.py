#!/usr/bin/env python3

import states
from commands.about import About
from commands.commands import Commands
from commands.inventory import Inventory
from commands.quit import Quit
from gamecontext import GameContext
from helpers import intro, outro, get_item_by_name
from items.features import USABLE
from items.newspaper import Newspaper
from items.revolver import Revolver
from items.whip import Whip


def main():
    intro()

    # game init
    context = GameContext(
        game_state=states.PLAYING,
        backpack=[
            Whip(),
            Revolver(),
            Newspaper()
        ],
        commands=[
            About(),
            Commands(),
            Inventory(),
            Quit()
        ]
    )

    # game loop
    while context.game_state == states.PLAYING:
        # normalize input string
        line = input('> ').lower().lstrip().rstrip()

        if line == '':  # len(line) == 0
            # pass
            continue

        for command in context.commands:
            if command.name == line:
                command.exec(context)
                break
        else:
            print('Tento príkaz nepoznám.')
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

    outro()


if __name__ == '__main__':
    main()
