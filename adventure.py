#!/usr/bin/env python3

import states
from features import MOVABLE, USABLE


def cmd_take(room: dict, line: str, backpack: list):
    item_name = line.removeprefix('vezmi').strip()

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš zobrať.')
        return

    # if item not in backpack
    for item in room['items']:
        if item['name'] == item_name:
            if MOVABLE in item['features']:
                # remove item from room
                room['items'].remove(item)

                # drop item in the backpack
                backpack.append(item)

                # print out
                print(f'Predmet {item["name"]} si si vložil do batohu.')

            else:
                print('Tento predmet sa nedá zobrať.')

            return

    # if no such item available
    print('Taký predmet tu nikde nevidím.')


def cmd_inventory(backpack: list):
    if backpack == []:
        print('Batoh je prázdny.')
    else:
        print("V batohu máš:")
        for item in backpack:
            print(f'\t* {item["name"]}')


def cmd_explore(room: dict, line: str, backpack: list):
    item_name = line.removeprefix('preskumaj').strip()

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš preskúmať.')
        return

    # if item not in room items
    for item in room['items'] + backpack:
        if item['name'] == item_name:
            print(item['description'])
            return

    # if no such item available
    print('Taký predmet tu nikde nevidím.')


def cmd_drop(room: dict, line: str, backpack: list):
    item_name = line.removeprefix('poloz').strip()

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš položiť.')
        return

    # if item not in backpack
    for item in backpack:
        if item['name'] == item_name:
            # remove item from backpack
            backpack.remove(item)

            # drop item in the room
            room['items'].append(item)

            # print out
            print(f'Predmet {item["name"]} si položil do miestnosti.')
            return

    # if no such item available
    print('Taký predmet u seba nemáš.')


def cmd_look_around(room: dict):
    """
    Prints description about the room

    Prints out the description about the room given as parameter.
    :param room: room to describe
    """
    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room['description'])

    # print items in the room
    if room['items'] == []:  # len(room['items'] == 0
        print('Nevidíš tu nič zvláštne.')
    else:
        print("Vidíš:")
        for item in room['items']:
            print(f'\t* {item["name"]}')


def cmd_commands():
    print('Dostupné príkazy v hre:')
    print('* inventar - zobrazí obsah hráčovho batoha')
    print('* koniec - ukončí hru')
    print('* o hre - zobrazí informácie o hre')
    print('* poloz - vyloží predmet z batohu do miestnosti')
    print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
    print('* rozhliadni sa - zobrazí opis miestnosti, v ktorej sa hráč aktuálne nachádza')


def cmd_about():
    print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
    print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
          'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.')
    print('\n(c) 2021 hru spáchal mirek')


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
    cmd_look_around(room)

    # game loop
    while game_state == states.PLAYING:
        line = input('> ').lstrip().rstrip().lower()

        if len(line) == 0:  # line == ''
            continue

        elif line in ('o hre', 'about'):
            cmd_about()

        elif line in ('rozhliadni sa', 'look around'):
            cmd_look_around(room)

        elif line in ('prikazy', 'commands', 'help', '?'):
            cmd_commands()

        elif line in ('koniec', 'quit', 'exit', 'q'):
            game_state = states.QUIT

        elif line.startswith('preskumaj'):
            cmd_explore(room, line, backpack)

        elif line.startswith('poloz'):
            cmd_drop(room, line, backpack)

        elif line.startswith('vezmi'):
            cmd_take(room, line, backpack)

        elif line in ('inventar', 'inventory', 'i'):
            cmd_inventory(backpack)

        else:
            print('Tento príkaz nepoznám.')

    print('Končíme.')


if __name__ == '__main__':
    play_game()
