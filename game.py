#!/usr/bin/env python3
import states

from helpers import show_room, get_room_by_name
from items import figa, coin, canister, matches, fire_extinguisher, newspaper
from commands import *
# from world import world
import json

if __name__ == '__main__':
    # init game
    with open('world.json', 'r', encoding='utf-8') as file:
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
        'history': [],
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
            cmd_save,
        ]
    }

    context['backpack']['items'].append(figa)
    context['backpack']['items'].append(coin)

    # serialization
    # import json
    # file = open('world.json', 'w+', encoding='utf-8')
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
        if context['room']['name'] == 'heaven':
            context['state'] = states.WIN

        elif context['room']['name'] == 'hell':
            context['state'] = states.DEAD

    # final animation
    # when player wins
    if context['state'] == states.WIN:
        print("__        __   _ _   ____                   _")
        print("\\ \\      / /__| | | |  _ \\  ___  _ __   ___| |")
        print(" \\ \\ /\\ / / _ \\ | | | | | |/ _ \\| '_ \\ / _ \\ |")
        print("  \\ V  V /  __/ | | | |_| | (_) | | | |  __/_|")
        print("   \\_/\\_/ \\___|_|_| |____/ \\___/|_| |_|\\___(_)")

    # when player dies
    elif context['state'] == states.DEAD:
        print('You are dead!')

    # game credits
    print('(c)2021 by mirek mocný programátor')
