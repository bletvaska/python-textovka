#!/usr/bin/env python3

import features
import states
import commands
import json


def parse(line: str, commands: list) -> tuple:
    for command in commands:
        for alias in command['aliases'] + (command['name'],):
            if line.startswith(alias):
                param = line.split(alias)[1].strip()
                return (command, param)

    return (None, None)


def main():
    context = {
        'commands': None,
        'inventory': None,
        'state': states.PLAYING,
        'room': None,
        'world': None
    }

    # load world
    file = open('world.json', 'r', encoding='utf-8')
    context['world'] = json.load(file)
    file.close()

    context['commands'] = commands.commands

    context['room'] = context['world'][0]

    context['inventory'] = [
        {
            'name': 'ucebnica jazyka python',
            'description': 'Mocná učebnica jazyka Python od známeho Pytonistu Jana.',
            'features': [features.MOVABLE, features.USABLE]
        }
    ]

    commands.look_around(None, context)

    # game loop
    while context['state'] == states.PLAYING:
        line = input('> ').strip().lower()

        # parse input line
        command, param = parse(line, context['commands'])
        if command is not None:
            command['exec'](param, context)
        else:
            print('Taký príkaz nepoznám.')

        # check game winning
        if context['room']['name'] == 'garden':
            context['state'] = states.WIN

    # celebrations
    if context['state'] == states.WIN:
        print("  ____                            _         _       _   _                 _ ")
        print(" / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |")
        print("| |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |")
        print("| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|")
        print(" \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)")
        print("                  |___/                                                     ")

    print('...koniec...')


if __name__ == '__main__':
    main()
