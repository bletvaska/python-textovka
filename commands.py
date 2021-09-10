import random

import features
import states
import usages
from helper import find_item


def inventory(name: str, context: dict) -> None:
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


def use(name: str, context: dict) -> None:
    """
    Represents the examine command.

    :param name: the name of item do describe
    :param context: the game context
    """

    room = context['room']
    inventory = context['inventory']

    # nezadal meno predmetu
    if len(name) == 0:
        print('Neviem, aký predmet chceš použiť.')
        return

    # najdem predmet v miestnosti alebo inventari
    item = find_item(name, room['items'] + inventory)
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # overim, ci je predmet pouzitelny
    if features.USABLE not in item['features']:
        print('Tento predmet sa nedá použiť.')
        return

    # pouzitie predmetov
    if name == 'ucebnica jazyka python':
        usages.use_textbook()

    elif name == 'kanister':
        usages.use_can(item, context)

    elif name == 'zapalky':
        usages.use_matches(item, context)

    elif name == 'hasiaci pristroj':
        usages.use_fire_extinguisher(item, context)

    else:
        print(f'Snažím sa použiť predmet {name}')


def about(name: str, context: dict) -> None:
    print('Hru spáchal v (c) 2021 mirek.')
    print('Ďalšie dobrodužstvo Indiana Jonesa. Tentokrát sa pokúsi o únik zo skladu Košického Technického múzea.')


def quit_game(name: str, context: dict) -> None:
    print('ta koncime')
    context['state'] = states.QUIT


def show_commands(name: str, context: dict) -> None:
    print('Zoznam príkazov hry:')

    for command in context['commands']:
        print(f'\t* {command["name"]} - {command["description"]}')


commands = [
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
        'exec': inventory
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
    },

    {
        'name': 'pouzi',
        'aliases': ('pouzit', 'use'),
        'description': 'použije zvolený predmet',
        'exec': use
    }
]
