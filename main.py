#!/usr/bin/env python

import states
from commands.about import About
from commands.command import Command
from commands.commands import Commands
from commands.drop import Drop
from commands.inventory import Inventory
from commands.lookaround import LookAround
from commands.quit import Quit
from commands.take import Take
from context import Context
from items.bucket import Bucket
from items.canister import Canister
from items.door import Door
from items.matches import Matches
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


def parse(line: str, commands: list[Command]):
    pass


def main():
    # game init
    room = Room(name='dungeon',
                description='Nachádzaš sa vo veľmi tmavej miestnosti. Kamenné múry dávajú tušiť, že sa'
                            'nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? '
                            'Okná tu nie sú žiadne, čo by ťa uistilo o správnosti tohto predpokladu.',
                items=[
                    Matches(),
                    Bucket(),
                    Canister(),
                    Door()
                ],
                exits=[
                    'sever',
                    'juh'
                ]
                )
    context = Context(current_room=room)
    context.current_room.show()

    commands = [
        About(),
        Commands(),
        Drop(),
        Inventory(),
        LookAround(),
        Quit(),
        Take()
    ]

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':
            continue

        cmd = parse(line, commands)

        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd.exec(line, context)

        # for cmd in commands:
        #     if line.startswith(cmd.name):
        #         cmd.exec(line, context)
        #         break
        # else:
        #     print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    intro()
    main()
    outro()
