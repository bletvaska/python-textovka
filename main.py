#!/usr/bin/env python

import states
from commands.about import About
from commands.commands import Commands
from commands.drop import Drop
from commands.inventory import Inventory
from commands.lookaround import LookAround
from commands.quit import Quit
from commands.take import Take
from context import Context
from items.features import MOVABLE, USABLE
from helpers import get_item_by_name
from items.item import Item
from room import Room


def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('                        and his Great Escape')
    print()


def outro():
    """
    Shows the outro screen of the game.
    """
    print('(c)2022 by mirek')
    print('See you soon.')


def main():
    # game init
    # game_state = states.PLAYING
    # backpack = []

    room = Room(name='dungeon',
                description='Nachádzaš sa vo veľmi tmavej miestnosti. Kamenné múry dávajú tušiť, že sa'
                            'nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? '
                            'Okná tu nie sú žiadne, čo by ťa uistilo o správnosti tohto predpokladu.',
                items=[
                    Item(name='zapalky',
                         description='Štandardné zápalky. Tri.',
                         features=[MOVABLE, USABLE]),
                    Item(name='vedro',
                         description='Vedro plné vody. Ťažko povedať, či aj pitnej.',
                         features=[MOVABLE, USABLE]),
                    Item(name='kanister',
                         description='Veľký 25l kanister. Po odšróbovaní vrchnáka si zistil, že je to benzín. Kvalitka. 98 oktánov.',
                         features=[USABLE, MOVABLE]),
                    Item(name='dvere',
                         description='Veľké dubové dvere. Zamknuté.',
                         features=[])
                ],
                exits=[
                    'sever',
                    'juh'
                ]
                )
    context = Context(current_room=room)
    context.current_room.show()

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue

        # rozhliadni sa, look around
        elif line in ('rozhliadni sa', 'look around'):
            cmd = LookAround()
            cmd.exec(line, context)

        # about, info, ?
        elif line in ('o hre', 'about', 'info', '?'):
            cmd = About()
            cmd.exec(line, context)

        # drop item
        elif line.startswith('poloz'):
            cmd = Drop()
            cmd.exec(line, context)

        # take item
        elif line.startswith('vezmi'):
            Take().exec(line, context)

        # commands, help
        elif line in ('prikazy', 'help', 'commands'):
            Commands().exec(line, context)

        # quit, exit, q, bye
        elif line in ('koniec', 'quit', 'exit', 'q', 'bye'):
            Quit().exec(line, context)

        # inventory
        elif line in ('inventar', 'i', 'inventory'):
            cmd = Inventory()
            cmd.exec(line, context)

        else:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    intro()
    main()
    outro()
