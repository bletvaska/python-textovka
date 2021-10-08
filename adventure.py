#!/usr/bin/env python3

import states
from features import MOVABLE, USABLE
from commands import parse, cmd_look_around


def play_game():
    backpack = [
        {
            'name': 'noviny',
            'description': 'dennik sme s autorskou strankou sama marca',
            'features': [MOVABLE, USABLE],
        },
    ]

    game_state = states.PLAYING
    room = {
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
                'features': []
            }
        ],
        'exits': []
    }

    # game intro
    print('Indiana Jones')
    print('alebo veľké Pythoňácke dobrodružstvo')
    cmd_look_around(room, None, None)

    # game loop
    while game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        # empty input?
        if len(line) == 0:  # line == ''
            continue

        # parse
        (cmd, arg) = parse(line)
        if cmd is None:
            print('Tento príkaz nepoznám.')
        else:
            cmd['exec'](room, arg, backpack)


        # elif line in ('o hre', 'about'):
        #     cmd_about()
        #
        # elif line in ('rozhliadni sa', 'look around'):
        #     cmd_look_around(room)
        #
        # elif line in ('prikazy', 'commands', 'help', '?'):
        #     cmd_commands()
        #
        # elif line in ('koniec', 'quit', 'exit', 'q'):
        #     game_state = states.QUIT
        #
        # elif line.startswith('preskumaj'):
        #     cmd_explore(room, line, backpack)
        #
        # elif line.startswith('poloz'):
        #     cmd_drop(room, line, backpack)
        #
        # elif line.startswith('vezmi'):
        #     cmd_take(room, line, backpack)
        #
        # elif line in ('inventar', 'inventory', 'i'):
        #     cmd_inventory(backpack)
        #
        # else:
        #     print('Tento príkaz nepoznám.')

    print('Končíme.')


if __name__ == '__main__':
    play_game()
