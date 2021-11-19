#!/usr/bin/env python3
import states

from helpers import show_room, get_room_by_name
from items import figa, coin, canister, matches, fire_extinguisher, newspaper
from commands import *
# from world import world
import json

if __name__ == '__main__':
    # init game
    with open('world.json', 'r') as file:
        world = json.load(file)
    # file.close()

    # post processing
    room = get_room_by_name(world, 'dungeon')
    room['items'].append(canister)
    room['items'].append(matches)
    room['items'].append(fire_extinguisher)
    room['items'].append(newspaper)

    context = {
        'state': states.PLAYING,
        'backpack': {
            'items': [],
            'max': 2,
        },
        'world': world,
        'room': room,  # get_room_by_name(world, 'dungeon'),
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
            cmd_west,
            cmd_east,
            cmd_south,
            cmd_north,
        ]
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    # serialization
    # import json
    # file = open('world.json', 'w+')
    # json.dump(context['world'], file, indent=4, ensure_ascii=False)
    # file.close()

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
