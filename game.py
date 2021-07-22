#!/usr/bin/env python3

import parser
from states import STATE_PLAYING
from helper import show_room


def init_game(context: dict) -> None:
    # initialize backpack
    context['backpack']['items'].append({
        'name': 'noviny',
        'description': 'Nové tajmsy, husté čítanie na každý deň.',
        'features': ['movable']
    })

    # initialize room
    context['room'] = {
        'description': 'Nachádzaš v tmavej miestnosti. Kamenné múry dávajú tušiť, že sa nachádzaš v nejakej kamennej kobke. Žeby podzemie hradu v Grunwalde? Okná tu nie sú žiadne, čo by ťa uistili o správnosti tohto predpokladu.',
        'name': 'kobka',
        'items': [
            {
                'name': 'vedro',
                'description': 'Vedro plné vody.',
                'features': ['movable', 'usable']
            },
            {
                'name': 'kanister',
                'description': 'Kanister plný benzínu.',
                'features': ['movable']
            },
            {
                'name': 'zapalky',
                'description': 'Zápalky na vatru.',
                'features': ['movable']
            },
            {
                'name': 'chladnicka',
                'description': 'Chladnička značky Calex. Zvláštne znamenie: pokazená.',
                'features': ['observable']
            }
        ],
        'exits': []
    }

    # initialize commands
    context['commands'] += parser.commands


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

    # input parser
    while context['state'] == STATE_PLAYING:
        # read input from user and normalize it
        line = input('> ').rstrip().lstrip().lower()

        # test if line is empty
        if line == '':
            continue

        cmd = parser.parse(line, context['commands'])

        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](cmd['param'], context)

    # it must finish here
    print('(c)2021 mirek')
