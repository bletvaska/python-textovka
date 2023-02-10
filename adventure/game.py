#!/usr/bin/env python

from rich import print

import states
from game_context import GameContext
from helpers import intro, outro, parse_line, get_room_by_name


def main():
    # game initialization
    context = GameContext()

    context.current_room = get_room_by_name('v lietadle', context)
    context.current_room.show()

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':  # len(line) == 0
            continue
            # pass

        # parse command line
        command = parse_line(line, context)
        if command is None:
            print('[red]Tento príkaz nepoznám.[/red]')
        else:
            command.exec(context)
            context.current_room.act(context)


if __name__ == '__main__':
    intro()
    main()
    outro()
