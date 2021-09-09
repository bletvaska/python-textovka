#!/usr/bin/env python3

import features
import states


def cmd_inventory(name: str, room: dict, inventory: list) -> None:
    if len(inventory) == 0:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in inventory:
            print(f'\t* {item["name"]}')


def look_around(name: str, room: dict, inventory: list) -> None:
    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if len(room['items']) == 0:
        print('Nevidíš tu nič zaujímavé.')
    else:
        print(f'Vidíš:')
        for item in room['items']:
            print(f'\t* {item["name"]}')


def drop(name: str, room: dict, inventory: list) -> None:
    if name == '':
        print('Neviem, aký predmet chceš položiť.')
    else:
        for item in inventory:
            if item['name'] == name:
                # vybrat ho z inventaru
                inventory.remove(item)

                # polozit ho do miestnosti
                room['items'].append(item)

                print(f'Predmet {name} si vyložil do miestnosti.')
                break
        else:
            print('Taký predmet u seba nemáš.')


def take(name: str, room: dict, inventory: list) -> None:
    """
    Represents the TAKE command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

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


def examine(name: str, room: dict, inventory: list) -> None:
    """
    Represents the examine command.

    :param name: the name of item do describe
    :param room: the room object, where the player is currently in
    :param inventory: the player's inventory
    """

    if len(name) == 0:
        print('Neviem, aký predmet chceš preskúmať.')
    else:
        for item in room['items'] + inventory:
            if item['name'] == name:
                print(item['description'])
                break
        else:
            print('Taký predmet tu nigde nevidím.')


def main():
    room = {
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
    state = states.PLAYING
    inventory = [
        {
            'name': 'ucebnica jazyka python',
            'description': 'Mocná učebnica jazyka Python od známeho Pytonistu Jana.',
            'features': [features.MOVABLE, features.USABLE]
        }
    ]

    look_around(None, room, None)

    while state == states.PLAYING:
        line = input('> ').strip().lower()

        # parser
        for command in cmds:
            if line == command['name']:
                command['exec']('parameter', room, inventory)
                break
        else:
            print('Taký príkaz nepoznám.')

        # if line == 'o hre':
        #     about()
        #
        # elif line == 'prikazy':
        #     commands()
        #
        # elif line in ('koniec', 'quit', 'bye', 'q', 'ukoncit'):
        #     print('ta koncime')
        #     state = states.QUIT
        #
        # elif line == 'rozhliadni sa':
        #     look_around(room)
        #
        # elif line in ('inventar', 'inventory', 'i'):
        #     cmd_inventory(inventory)
        #
        # elif line.startswith('preskumaj'):
        #     name = line.split('preskumaj')[1].strip()
        #     examine(name, room, inventory)
        #
        # elif line.startswith('vezmi'):
        #     name = line.split('vezmi')[1].strip()
        #     take(name, room, inventory)
        #
        # elif line.startswith('poloz'):
        #     name = line.split('poloz')[1].strip()
        #     drop(name, room, inventory)
        #
        # else:
        #     print('Taký príkaz nepoznám.')

    print('...koniec...')


def about(name: str, room: dict, inventory: list) -> None:
    print('Hru spáchal v (c) 2021 mirek.')
    print('Ďalšie dobrodužstvo Indiana Jonesa. Tentokrát sa pokúsi o únik zo skladu Košického Technického múzea.')


cmds = [
    {
        'name': 'preskumaj',
        'exec': examine,
        'description': 'zobrazí informácie o zvolenom predmete'
    },

    {
        'name': 'poloz',
        'exec': drop,
        'description': 'vyberie predmet z batohu a položí ho do miestnosti'
    },

    {
        'name': 'koniec',
        'description': 'ukončí rozohratú hru',
        'exec': None
    },

    {
        'name': 'o hre',
        'description': 'zobrazí informácie o hre',
        'exec': about
    },

    {
        'name': 'rozhliadni sa',
        'description': 'zobrazí obsah miestnosti',
        'exec': look_around
    },

    {
        'name': 'inventar',
        'description': 'zobrazí obsah batohu',
        'exec': cmd_inventory
    },

    {
        'name': 'vezmi',
        'description': 'vezme predmet z miestnosti a vloží ho do batohu',
        'exec': take
    },

    {
        'name': 'prikazy',
        'description': 'zobrazí zoznam príkazov dostupných v hre',
        'exec': None  # commands
    }
]


def commands(name: str, room: dict, inventory: list) -> None:
    print('Zoznam príkazov hry:')

    for command in cmds:
        print(f'\t* {command["name"]} - {command["description"]}')


if __name__ == '__main__':
    main()
