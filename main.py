#!/usr/bin/env python3

import states
from commands.about import About
from commands.commands import Commands
from commands.down import Down
from commands.drop import Drop
from commands.examine import Examine
from commands.inventory import Inventory
from commands.lookaround import LookAround
from commands.north import North
from commands.quit import Quit
from commands.take import Take
from commands.up import Up
from commands.use import Use
from gamecontext import GameContext
from helpers import intro, outro, get_room_by_name
from items.revolver import Revolver
from items.whip import Whip
from world import world


def main():
    intro()

    # game init
    context = GameContext(
        game_state=states.PLAYING,
        backpack=[
            Whip(),
            Revolver()
        ],
        commands=[
            About(),
            Commands(),
            Down(),
            Drop(),
            Examine(),
            Inventory(),
            LookAround(),
            North(),
            Quit(),
            Take(),
            Up(),
            Use()
        ],
        current_room=get_room_by_name('v lietadle', world)
    )

    # show room
    context.current_room.show()

    # game loop
    while context.game_state == states.PLAYING:
        # normalize input string
        line = input('> ').lower().lstrip().rstrip()

        if line == '':  # len(line) == 0
            # pass
            continue

        for command in context.commands:
            if line.startswith(command.name):
                param = line.split(command.name, maxsplit=1)[1].lstrip()
                command.parameter = param
                command.exec(context)
                break
        else:
            print('Tento príkaz nepoznám.')

    outro()


if __name__ == '__main__':
    main()
