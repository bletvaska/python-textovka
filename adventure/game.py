#!/usr/bin/env python

import states
from commands import About, Commands, Quit, LookAround, Inventory, Examine, Take
from commands.drop import Drop
from context import Context
from helpers import intro, outro
from items.empty_seats import EmptySeats
from items.whip import Whip
from rooms import Room


def main():
    # init
    context = Context(
        commands=[
            About(),
            Commands(),
            Drop(),
            Examine(),
            Inventory(),
            LookAround(),
            Quit(),
            Take(),
        ],

        current_room=Room(name='v lietadle',
                          description='Prebudil si sa v malom dvojmotorovom lietadle plachtiacom nad egyptskou púšťou. '
                                      'Je tu nádherný kľud, pretože motory sú vypnuté a na palube nie je okrem teba '
                                      'živej duše. (Celkom zaujímavá situácia, že áno?)',
                          items=[EmptySeats(), Whip()],
                          exits=[])
    )

    # show room
    context.current_room.show()

    # game loop
    while context.game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if line == '':  # len(line) == 0
            continue

        for command in context.commands:
            if line.startswith(command.name):
                param = line.split(command.name)[1].strip()
                command.param = param
                command.exec(context)
                break
        else:
            print('Taký príkaz nepoznám.')


if __name__ == '__main__':
    intro()
    main()
    outro()
