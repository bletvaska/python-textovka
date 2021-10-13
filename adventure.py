#!/usr/bin/env python3

import states
from features import MOVABLE, USABLE
from commands import parse, cmd_look_around


def play_game():
    # init game
    context = {
        'backpack': {
            'items': [],
            'capacity': 2
        },
        'room': None,
        'world': {},
        'state': states.PLAYING
    }

    context['backpack']['items'].append(
        {
            'name': 'noviny',
            'description': 'dennik sme s autorskou strankou sama marca',
            'features': [MOVABLE, USABLE],
        }
    )

    context['room'] = {
        'name': 'dungeon',
        'description': 'Nachádzaš sa v tmavej miestnosti, kde sa po stenách nachádzajú hieroglify z obdobia Juraja Jánošíka. Valaška a krpce sú najščastejším motívom, ktorý vidíš na vyrytých postavách na stene. Stiesňujúce miesto.',
        'items': [
            {
                'name': 'vedro',
                'description': 'Vedro plné vody.',
                'features': [MOVABLE, USABLE]
            },

            {
                'name': 'zapalky',
                'description': 'Krabička so zápalkami.',
                'features': [MOVABLE, USABLE]
            },

            {
                'name': 'kanister',
                'description': 'Vysokooktánový benzín tvorí obsah tohto kanistra. Kvalitka za rozumnú cenu.',
                'features': [MOVABLE, USABLE]
            },

            {
                'name': 'dvere',
                'description': 'Masívne dubové dvere. Zamknuté.',
                'features': [],
                'state': None
            }
        ],
        'exits': {
            'east': 'garden',
            'west': None,
            'north': None,
            'south': None
        }
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
