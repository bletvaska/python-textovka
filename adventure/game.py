#!/usr/bin/env python
import states
from commands.about import About
from commands.commands import Commands
from commands.down import Down
from commands.drop import Drop
from commands.east import East
from commands.examine import Examine
from commands.help import Help
from commands.inventory import Inventory
from commands.look_around import LookAround
from commands.north import North
from commands.quit import Quit
from commands.save import Save
from commands.south import South
from commands.take import Take
from commands.up import Up
from commands.use import Use
from commands.west import West
from game_context import GameContext
from helpers import intro, outro, parse_line, get_room_by_name
from items.dictionary import Dictionary
from rooms.world import load_world


def main():
    intro()

    # game initialization
    context = GameContext(
        rooms=load_world(),
        commands=[
            About(),
            Commands(),
            Down(),
            Drop(),
            East(),
            Examine(),
            Help(),
            Inventory(),
            LookAround(),
            North(),
            Quit(),
            Save(),
            South(),
            Take(),
            Up(),
            Use(),
            West()
        ],
    )

    # room = context.current_room = get_room_by_name('v lietadle', context)
    # context.backpack.append(Dictionary())
    room = context.current_room = get_room_by_name('podzemie', context)
    room.show()

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':  # len(line) == 0
            continue
            # pass

        # parse command line
        command = parse_line(line, context)
        if command is None:
            print('Tento príkaz nepoznám.')
        else:
            command.exec(context)
            context.current_room.act(context)

    outro()


if __name__ == '__main__':
    main()
