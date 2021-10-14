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

        # check room name
        if context['room']['name'] == 'garden':
            print("__        __   _ _   ____                   _ ")
            print("\\ \\      / /__| | | |  _ \\  ___  _ __   ___| |")
            print(" \\ \\ /\\ / / _ \\ | | | | | |/ _ \\| '_ \\ / _ \\ |")
            print("  \\ V  V /  __/ | | | |_| | (_) | | | |  __/_|")
            print("   \\_/\\_/ \\___|_|_| |____/ \\___/|_| |_|\\___(_)")
            print()

            context['state'] = states.WIN

    print('(c) 2021 spáchal mirek ako výsledný projekt hustého akvaristicko-teraristického školenia')


if __name__ == '__main__':
    play_game()
