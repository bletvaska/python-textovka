import json

import requests

import config
from features import MOVABLE, USABLE
import states
from utils import get_item_by_name, get_room_by_name
from usages import use_canister, use_matches, use_bucket, use_newspaper


def cmd_take(context: dict, arg: str):
    item_name = arg
    room = context['room']
    backpack = context['backpack']['items']

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš zobrať.')
        return

    item = get_item_by_name(item_name, room['items'])

    # if no such item in room
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # is item movable?
    if MOVABLE not in item['features']:
        print('Tento predmet sa nedá zobrať.')
        return

    # is backpack full?
    if len(backpack) >= context['backpack']['capacity']:
        print('Batoh je plný.')
        return

    # take item
    context['history'].append(f'VEZMI {item_name}')

    # remove item from room
    room['items'].remove(item)

    # drop item in the backpack
    backpack.append(item)

    # print out
    print(f'Predmet {item["name"]} si si vložil do batohu.')


def cmd_inventory(context: dict, arg: str):
    backpack = context['backpack']['items']

    if backpack == []:
        print('Batoh je prázdny.')
    else:
        print("V batohu máš:")
        for item in backpack:
            print(f'\t* {item["name"]}')


def cmd_explore(context: dict, arg: str):
    item_name = arg
    backpack = context['backpack']['items']
    room = context['room']

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš preskúmať.')
        return

    # find item by name
    item = get_item_by_name(item_name, room['items'] + backpack)

    # if no such item available
    if item is None:
        print('Taký predmet tu nikde nevidím.')
    else:
        print(item['description'])


def cmd_drop(context: dict, arg: str):
    item_name = arg
    backpack = context['backpack']['items']
    room = context['room']

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš položiť.')
        return

    # if no such item available
    item = get_item_by_name(item_name, backpack)
    if item is None:
        print('Taký predmet u seba nemáš.')
        return

    # update history
    context['history'].append(f'POLOZ {item_name}')

    # remove item from backpack
    backpack.remove(item)

    # drop item in the room
    room['items'].append(item)

    # print out
    print(f'Predmet {item["name"]} si položil do miestnosti.')


def cmd_look_around(context: dict, arg: str):
    """
    Prints description about the room

    Prints out the description about the room given as parameter.
    :param room: room to describe
    """
    room = context['room']

    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room['description'])

    # print items in the room
    if room['items'] == []:  # len(room['items'] == 0
        print('Nevidíš tu nič zvláštne.')
    else:
        print("Vidíš:")
        for item in room['items']:
            print(f'\t* {item["name"]}')

    # print exits
    exits = []
    for _exit in room['exits']:
        if room['exits'][_exit] is not None:
            exits.append(_exit)

    if exits == []:
        print('Z miestnosti nevedú žiadne východy.')
    else:
        print('Môžeš ísť:')
        for ex in exits:
            if ex == 'north':
                print('\t* sever')
            if ex == 'south':
                print('\t* juh')
            if ex == 'east':
                print('\t* východ')
            if ex == 'west':
                print('\t* západ')


def cmd_commands(context: dict, arg: str):
    print('Dostupné príkazy v hre:')

    for cmd in commands:
        print(f'* {cmd["name"]} - {cmd["description"]}')


def cmd_about(context: dict, arg: str):
    print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
    print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
          'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.')
    print('\n(c) 2021 hru spáchal mirek')


def cmd_quit(context: dict, arg: str):
    context['state'] = states.QUIT


def cmd_use(context: dict, arg: str):
    item_name = arg
    backpack = context['backpack']['items']
    room = context['room']

    # is there name given?
    if item_name == '':
        print('Neviem čo chceš použiť.')
        return

    # is there such item?
    item = get_item_by_name(item_name, backpack + room['items'])
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # is item usable?
    if USABLE not in item['features']:
        print('Tento predmet sa nedá použiť')
        return

    # using the item
    # update history
    context['history'].append(f'POUZI {item_name}')

    # item['exec'](context, item)
    if item_name == 'kanister':
        use_canister(context, item)

    elif item_name == 'zapalky':
        use_matches(context, item)

    elif item_name == 'vedro':
        use_bucket(context, item)

    elif item_name == 'noviny':
        use_newspaper(context, item)

    else:
        # print(f'Použil si predmet {item["name"]}')
        raise NotImplementedError(f'Usage of item "{item["name"]}" was not yet implemented')


def _go(context: dict, direction: str):
    room = context['room']

    # overim, ze ci sa na dany smer da ist
    # ak sa neda, tak vypisem spravu
    if room['exits'][direction] is None:
        print('Tam sa nedá ísť.')
        return

    # update history
    context['history'].append(direction)

    # v opacnom pripade:
    # * zmenim aktualnu miestnost na novu
    context['room'] = get_room_by_name(room['exits'][direction], context['world'])

    # * rozhliadnem sa v nej
    cmd_look_around(context, None)


def cmd_east(context: dict, arg: str):
    _go(context, 'east')


def cmd_west(context: dict, arg: str):
    _go(context, 'west')


def cmd_north(context: dict, arg: str):
    _go(context, 'north')


def cmd_south(context: dict, arg: str):
    _go(context, 'south')


def cmd_save(context: dict, arg: str):
    if arg == '':
        print('Neviem, kam chceš stav hry uložiť.')
        return

    if arg == 'cloud':
        payload = {
            "history": context['history']
        }

        headers = {
            'X-Parse-Application-Id': config.app_id,
            'X-Parse-REST-API-Key': config.rest_api_key,
            'Content-Type': 'application/json'
        }

        with requests.post(f'{config.base_url}/history', headers=headers, json=payload) as response:
            data = response.json()
            print(f'Tvoja pozícia má kľúč "{data["objectId"]}".')

    # save to file
    try:
        with open(arg, 'w') as file:
            json.dump(context['history'], file)
    except Exception as ex:
        print('CHYBA: Chyba pri zápise do súboru.')
        print(f'CHYBA: {ex}')


commands = [
    {
        'name': 'vezmi',
        'description': 'vezme predmet z miestnosti a vloží si ho do batohu',
        'aliases': ('take',),
        'exec': cmd_take
    },

    {
        'name': 'poloz',
        'description': 'vyloží predmet z batohu do miestnosti',
        'aliases': ('drop',),
        'exec': cmd_drop
    },

    {
        'name': 'prikazy',
        'description': 'zobrazí zoznam príkazov použiteľných v hre',
        'aliases': ('commands', 'help', 'pomoc', '?'),
        'exec': cmd_commands
    },

    {
        'name': 'o hre',
        'description': 'zobrazí informácie o hre',
        'aliases': ('about',),
        'exec': cmd_about
    },

    {
        'name': 'rozhliadni sa',
        'description': 'zobrazí opis miestnosti, v ktorej sa hráč aktuálne nachádza',
        'aliases': ('look around',),
        'exec': cmd_look_around
    },

    {
        'name': 'preskumaj',
        'description': 'preskúma zvolený predmet',
        'aliases': ('explore',),
        'exec': cmd_explore
    },

    {
        'name': 'inventar',
        'description': 'vypíše obsah hráčovho batohu',
        'aliases': ('inventory', 'i'),
        'exec': cmd_inventory
    },

    {
        'name': 'koniec',
        'description': 'ukončí hru',
        'aliases': ('quit', 'exit', 'q', 'bye', 'end'),
        'exec': cmd_quit
    },

    {
        'name': 'pouzi',
        'description': 'použije zvolený predmet',
        'aliases': ('use',),
        'exec': cmd_use
    },

    {
        'name': 'vychod',
        'description': 'prejde do miestnosti na východ od aktuálnej',
        'aliases': ('east', 'v'),
        'exec': cmd_east
    },

    {
        'name': 'zapad',
        'description': 'prejde do miestnosti na západ od aktuálnej',
        'aliases': ('west', 'z'),
        'exec': cmd_west
    },

    {
        'name': 'sever',
        'description': 'prejde do miestnosti na sever od aktuálnej',
        'aliases': ('north', 's'),
        'exec': cmd_north
    },

    {
        'name': 'juh',
        'description': 'prejde do miestnosti na juh od aktuálnej',
        'aliases': ('south', 'j'),
        'exec': cmd_south
    },

    {
        'name': 'uloz',
        'description': 'uloží stav rozohratej hry do súboru',
        'aliases': ('ulozit', 'save'),
        'exec': cmd_save
    }
]


def parse(line: str) -> dict:
    for cmd in commands:

        aliases = list(cmd['aliases'])
        aliases.append(cmd['name'])

        for alias in aliases:
            if line.startswith(alias):
                arg = line.removeprefix(alias).strip()
                return (cmd, arg)

    return (None, None)
