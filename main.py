#!/usr/bin/env python3

import states
from commands.about import About
from commands.commands import Commands
from commands.down import Down
from commands.drop import Drop
from commands.east import East
from commands.examine import Examine
from commands.inventory import Inventory
from commands.lookaround import LookAround
from commands.north import North
from commands.quit import Quit
from commands.south import South
from commands.take import Take
from commands.up import Up
from commands.use import Use
from commands.west import West
from gamecontext import GameContext
from helpers import intro, outro, get_room_by_name, get_item_by_name
from items.revolver import Revolver
from items.whip import Whip
from world import rooms


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
            East(),
            Examine(),
            Inventory(),
            LookAround(),
            North(),
            Quit(),
            South(),
            Take(),
            Up(),
            Use(),
            West()
        ],
        current_room=get_room_by_name('v lietadle', rooms)
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

                # check if indiana jones is not in a death room
                if context.current_room.name == 'smrt vo vzduchu':
                    print('Stal si sa zakladateľom športového odvetvia, ktoré vojde do histórie ako skok hlboký.')
                    context.game_state = states.DEATH_BY_FREE_FALL

                # check if indiana jones is wearing uniform in front of nazi camp
                elif context.current_room.name == 'pred taborom':
                    uniform = get_item_by_name('nemecka uniforma (oblecena)', context.backpack)
                    if uniform is None:
                        print('Vojak si ťa so záujmom prehliadol a zastrelil ťa...')
                        context.game_state = states.SHOT_BY_NAZI_GUARD
                    else:
                        if context.current_room.south is None:
                            context.current_room.south = 'uprostred tabora'
                            print('Keď ťa vojak uvidel, otvoril ti bránu. (Hlupkák!)')

                break
        else:
            print('Tento príkaz nepoznám.')

    outro()


if __name__ == '__main__':
    main()
