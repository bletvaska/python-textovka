#!/usr/bin/env python3

"""
+---------+
|         |
|  hall   |
|         |
+---------+                   N
     |                        ^
     |                    W < + > E
     v                        v
+---------+    +---------+    S
|         |    |         |
| chamber |--->|   pit   |
|         |    |         |
+---------+    +---------+
"""


import json

import game_parser
from states import STATE_PLAYING
from helper import get_room_by_name, show_room
from world import world


def init_game(context: dict) -> None:
    # initialize backpack
    context['backpack']['items'].append({
        'name': 'noviny',
        'description': 'Nové tajmsy, husté čítanie na každý deň.',
        'features': ['movable', 'usable'],
    })
    context['backpack']['items'].append({
        'name': 'bic',
        'description': 'Neoddeliteľná súčasť hrdinu Indiana Jonesa použiteľná v každom dobrodružstve.',
        'features': ['movable', 'usable'],
    })

    # initialize world
    context['world'] = world

    # initialize room
    context['room'] = get_room_by_name(context['world'], 'chamber')

    # initialize commands
    context['commands'] += game_parser.commands


if __name__ == '__main__':
    # state of the game
    context = {
        'state': STATE_PLAYING,
        'room': None,
        'world': None,
        'backpack': {
            'capacity': 2,
            'items': []
        },
        'commands': []
    }

    init_game(context)

    # intro banner
    print(' ___           _ _                         _                       ')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ')
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print('|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/')

    print('                                                     (c) 2021 mirek')

    show_room(context['room'])

    # exporting world to file world.json
    # file = open('world.json', 'w', encoding='utf-8')
    with open('world.json', 'w', encoding='utf-8') as file:
        json.dump(context['world'], file, ensure_ascii=False, indent=3)

    # input parser
    while context['state'] == STATE_PLAYING:
        # read input from user and normalize it
        line = input('> ').rstrip().lstrip().lower()

        # test if line is empty
        if line == '':
            continue

        cmd = game_parser.parse(line, context['commands'])

        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](cmd['param'], context)

    # it must finish here
    print('(c)2021 mirek')
