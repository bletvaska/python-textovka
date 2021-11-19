#!/usr/bin/env python3
import states

from helpers import show_room, get_room_by_name
from items import figa, coin
from commands import *
from world import world

if __name__ == '__main__':
    # init game
    context = {
        'state': states.PLAYING,
        'backpack': {
            'items': [],
            'max': 2,
        },
        'world': world,
        'room': get_room_by_name(world, 'garden'),
        'commands': [
            cmd_about,
            cmd_inventory,
            cmd_drop,
            cmd_take,
            cmd_examine,
            cmd_quit,
            cmd_look_around,
            cmd_commands,
            cmd_use,
            cmd_west
        ]
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    # banner
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print("                       and his Great Escape                        ")
    print()

    # rendering the dark room
    show_room(context['room'])

    # main loop
    while context['state'] == states.PLAYING:
        # normalizing string
        line = input('> ').lower().strip()

        # empty input
        if line == '':
            continue

        command, param = parse(line, context)
        if command is None:
            print('Taký príkaz nepoznám.')
        else:
            callback = command['exec']
            callback(context, param)

        # check game win

    # game credits
    print('(c)2021 by mirek mocný programátor')
