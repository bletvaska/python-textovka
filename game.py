#!/usr/bin/env python3

from states import STATE_PLAYING
from commands import cmd_about, cmd_commands, cmd_drop, cmd_explore, cmd_inventory, cmd_look_around, cmd_quit, cmd_take, cmd_use
from helper import show_room


# ! FIXME zamysliet sa nad jednopismenkovymi prikazmi
def parse(line: str, commands: list) -> dict:
    # walk throught the list of commands
    for cmd in commands:
        for alias in cmd['aliases']:

            if line.startswith(alias):
                # extract parameter, if cmd was found
                cmd['param'] = line[len(alias):].strip()
                return cmd

    return None


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
    context['commands'] += [
        {
            'name': 'inventar',
            'description': 'Zobrazí obsah hráčovho batohu',
            'aliases': ['inventar', 'inventory', 'i'],
            'exec': cmd_inventory
        },

        {
            'name': 'o hre',
            'description': 'Zobrazí informácie o autorovi hry a o hre samotnej.',
            'aliases': ['o hre', 'about', 'info'],
            'exec': cmd_about
        },

        {
            'name': 'rozhliadni sa',
            'description': 'Vypíše obsah aktuálnej miestnosti.',
            'aliases': ['rozhliadni sa', 'look around'],
            'exec': cmd_look_around
        },

        {
            'name': 'koniec',
            'description': 'Ukončí rozohratú hru.',
            'aliases': ['koniec', 'quit', 'end', 'q'],
            'exec': cmd_quit
        },

        {
            'name': 'preskumaj',
            'description': 'Preskúma zvolený predmet.',
            'aliases': ['preskumaj', 'explore'],
            'exec': cmd_explore,
        },

        {
            'name': 'vezmi',
            'description': 'Vezme predmet z miestnosti do batohu.',
            'aliases': ['vezmi', 'zober', 'take'],
            'exec': cmd_take,
        },

        {
            'name': 'poloz',
            'description': 'Vyloží predme z batohu do aktuálnej miestnosti.',
            'aliases': ['poloz', 'drop'],
            'exec': cmd_drop,
        },

        {
            'name': 'prikazy',
            'description': 'Zobrazí zoznam dostupných príkazov v hre.',
            'aliases': ['prikazy', 'commands'],
            'exec': cmd_commands,
        },

        {
            'name': 'pouzi',
            'description': 'Použije daný predmet.',
            'aliases': ['pouzi', 'use', 'u'],
            'exec': cmd_use
        },
    ]


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

        cmd = parse(line, context['commands'])

        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](cmd['param'], context)

    # it must finish here
    print('(c)2021 mirek')
