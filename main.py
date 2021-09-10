#!/usr/bin/env python3

import features
import states
import commands


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

    context['commands'] = commands.commands
    context['world'] = [
        {
            'name': 'dungeon',
            'description': 'Nachádzaš sa v tmavej miestnosti. Každé okno je zvonku zabarikádované a do miestnosti preniká len '
                           'úzky prameň svetla. Masívne drevené dvere sú jediným východom z miestnosti.',
            'items': [
                {
                    'name': 'kanister',
                    'description': 'Kanister plný benzínu.',
                    'features': [features.MOVABLE, features.USABLE]
                },

                {
                    'name': 'hasiaci pristroj',
                    'description': 'Ručný hasiaci prístroj plný. Značka - červený.',
                    'features': [features.MOVABLE, features.USABLE]
                },

                {
                    'name': 'zapalky',
                    'description': 'Krabička zápaliek vyrobená ešte v Československu. Kvalitka.',
                    'features': [features.MOVABLE, features.USABLE],
                    'total': 3,
                },

                {
                    'name': 'dvere',
                    'description': 'Veľké masívne drevené dvere. Zamknuté.',
                    'features': [],
                    'state': 'zamknute'
                }
            ],
            'exits': {
                'west': None,
                'east': None,
                'south': None,
                'north': None
            }
        },

        {
            'name': 'garden',
            'description': 'Pomerne zarastené hriadky niečoho, čo by sa dalo voľne nazvať záhradkou. Darí sa tu skorocelu a inej burine.',
            'items': [],
            'exits': {
                'east': 'dungeon',
                'west': None,
                'north': None,
                'south': None
            }
        }
    ]

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

    print('...koniec...')


if __name__ == '__main__':
    main()
