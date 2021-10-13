#!/usr/bin/env python3

import states
from features import MOVABLE, USABLE
from commands import parse, cmd_look_around
from world import world
from utils import get_room_by_name


def play_game():
    # init game
    context = {
        'backpack': {
            'items': [
                {
                    'name': 'noviny',
                    'description': 'dennik sme s autorskou strankou sama marca',
                    'features': [MOVABLE, USABLE],
                }
            ],
            'capacity': 2
        },
        'room': get_room_by_name('dungeon', world),
        'world': world,
        'state': states.PLAYING
    }

    # game intro
    print('Indiana Jones')
    print('alebo veľké Pythoňácke dobrodružstvo')
    cmd_look_around(context, None)

    # game loop
    while context['state'] == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        # empty input?
        if len(line) == 0:  # line == ''
            continue

        # parse
        (cmd, arg) = parse(line)
        if cmd is None:
            print('Tento príkaz nepoznám.')
        else:
            cmd['exec'](context, arg)

    print('Končíme.')


if __name__ == '__main__':
    play_game()
