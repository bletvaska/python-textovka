#!/usr/bin/env python3

import json

from commands import commands as list_of_commands
from helper import show_room
import states


def parse(context, line, commands):
    for cmd in commands:
        for alias in cmd['aliases']:
            if line.startswith(alias):
                context['params'] = line.replace(alias, '').strip()
                return cmd

    return None


def main():
    # game initialization
    context = {
        'state': states.STATE_PLAYING,
        'inventory': [],
        'inventory_capacity': 2,
        'room': 'tmavá miestnosť',
    }

    context['inventory'].append({
        'name': 'ZAPALKY',
        'description': 'No zápalky. 4 kusy. Nepoužité. Krbové.',
        'features': ['movable', 'usable']
    })

    # load world
    with open('world.json', 'r') as file:
        context['world'] = json.load(file)

    # welcome
    print(' _____                            ____                       ')
    print('| ____|___  ___ __ _ _ __   ___  |  _ \ ___   ___  _ __ ___  ')
    print("|  _| / __|/ __/ _` | '_ \ / _ \ | |_) / _ \ / _ \| '_ ` _ \ ")
    print('| |___\__ \ (_| (_| | |_) |  __/ |  _ < (_) | (_) | | | | | |')
    print('|_____|___/\___\__,_| .__/ \___| |_| \_\___/ \___/|_| |_| |_|')
    print('                    |_|                     (c) mirek 2021   ')
    print()

    room_name = context['room']
    room = context['world'][room_name]
    show_room(room)

    # game loop
    while context['state'] == states.STATE_PLAYING:
        # parsovanie vstupu
        line = input('> ').upper().strip()

        cmd = parse(context, line, list_of_commands)
        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](context)

        # checking final state
        if context['room'] == 'záhradka':
            context['state'] = states.STATE_WIN

    # closing
    if context['state'] == states.STATE_WIN:
        print("  ____                            _       _ ")
        print(" / ___|___  _ __   __ _ _ __ __ _| |_ ___| |")
        print("| |   / _ \| '_ \ / _` | '__/ _` | __/ __| |")
        print("| |__| (_) | | | | (_| | | | (_| | |_\__ \_|")
        print(" \____\___/|_| |_|\__, |_|  \__,_|\__|___(_)")
        print("                  |___/                     ")
        print()

        print(
            'Tak sa ti to nakoniec podarilo! Ušiel si z pazúrov svojej domácej, ktorá ťa zamkla. Gratulujem! Môžeš ísť na pivo.')

    print('Created by (c)2021 mirek')


if __name__ == '__main__':
    main()
