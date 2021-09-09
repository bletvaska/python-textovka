#!/usr/bin/env python3

import features
import states


def cmd_inventory(name: str, context: dict) -> None:
    if len(context['inventory']) == 0:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in context['inventory']:
            print(f'\t* {item["name"]}')


def look_around(name: str, context: dict) -> None:
    room = context['room']
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if len(room['items']) == 0:
        print('Nevidíš tu nič zaujímavé.')
    else:
        print(f'Vidíš:')
        for item in room['items']:
            print(f'\t* {item["name"]}')


def drop(name: str, context: dict) -> None:
    if name == '':
        print('Neviem, aký predmet chceš položiť.')
    else:
        for item in context['inventory']:
            if item['name'] == name:
                # vybrat ho z inventaru
                context['inventory'].remove(item)

                # polozit ho do miestnosti
                context['room']['items'].append(item)

                print(f'Predmet {name} si vyložil do miestnosti.')
                break
        else:
            print('Taký predmet u seba nemáš.')


def take(name: str, context: dict) -> None:
    """
    Represents the TAKE command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    room = context['room']
    inventory = context['inventory']

    if name == '':
        print('Neviem, aký predmet chceš vziať.')
    else:
        for item in room['items']:
            if item['name'] == name:
                # overit, ci je batoh plny
                # todo: zmeni konstantu na premennu
                if len(inventory) >= 2:
                    print('Batoh je plný.')

                # overit, ci sa da zobrat
                elif features.MOVABLE in item['features']:
                    # vybrat ho z roomu
                    room['items'].remove(item)

                    # vlozit do batohu
                    inventory.append(item)

                    print(f'Predmet {name} si si vložil do batohu.')
                else:
                    print('Tento predmet sa nedá zobrať.')

                break
        else:
            print('Taký predmet tu nikde nevidím.')


def examine(name: str, context: dict) -> None:
    """
    Represents the examine command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    room = context['room']
    inventory = context['inventory']

    if len(name) == 0:
        print('Neviem, aký predmet chceš preskúmať.')
    else:
        for item in room['items'] + inventory:
            if item['name'] == name:
                print(item['description'])
                break
        else:
            print('Taký predmet tu nigde nevidím.')


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

    context['commands'] = [
        {
            'name': 'preskumaj',
            'aliases': ('examine',),
            'exec': examine,
            'description': 'zobrazí informácie o zvolenom predmete'
        },

        {
            'name': 'poloz',
            'aliases': ('drop',),
            'exec': drop,
            'description': 'vyberie predmet z batohu a položí ho do miestnosti'
        },

        {
            'name': 'koniec',
            'aliases': ('quit', 'bye', 'q', 'ukoncit'),
            'description': 'ukončí rozohratú hru',
            'exec': quit_game
        },

        {
            'name': 'o hre',
            'aliases': ('about',),
            'description': 'zobrazí informácie o hre',
            'exec': about
        },

        {
            'name': 'rozhliadni sa',
            'aliases': ('look around',),
            'description': 'zobrazí obsah miestnosti',
            'exec': look_around
        },

        {
            'name': 'inventar',
            'aliases': ('inventory', 'i'),
            'description': 'zobrazí obsah batohu',
            'exec': cmd_inventory
        },

        {
            'name': 'vezmi',
            'aliases': ('take',),
            'description': 'vezme predmet z miestnosti a vloží ho do batohu',
            'exec': take
        },

        {
            'name': 'prikazy',
            'aliases': ('commands', 'help', 'pomoc'),
            'description': 'zobrazí zoznam príkazov dostupných v hre',
            'exec': None  # commands
        }
    ]

    context['room'] = {
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
                'features': [features.MOVABLE, features.USABLE]
            },

            {
                'name': 'dvere',
                'description': 'Veľké masívne drevené dvere. Zamknuté.',
                'features': []
            }
        ]
    }

    line = None

    context['inventory'] = [
        {
            'name': 'ucebnica jazyka python',
            'description': 'Mocná učebnica jazyka Python od známeho Pytonistu Jana.',
            'features': [features.MOVABLE, features.USABLE]
        }
    ]

    look_around(None, context)

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


def about(name: str, context: dict) -> None:
    print('Hru spáchal v (c) 2021 mirek.')
    print('Ďalšie dobrodužstvo Indiana Jonesa. Tentokrát sa pokúsi o únik zo skladu Košického Technického múzea.')


def quit_game(name: str, context: dict) -> None:
    print('ta koncime')
    context['state'] = states.QUIT


def commands(name: str, context: dict) -> None:
    print('Zoznam príkazov hry:')

    for command in context['commands']:
        print(f'\t* {command["name"]} - {command["description"]}')


if __name__ == '__main__':
    main()
