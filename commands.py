import states
from helpers import get_item_by_name, show_room
from items import MOVABLE


def cmd_about(context: dict, param: str):
    print('(c)2021 created by mirek')
    print('Ďalšie veľké dobrodružstvo Indiana Jonesa. Tentokrát zápasí s jazykom Python v tmavej miestnosti.')


def cmd_commands(context: dict, param: str):
    print('Zoznam príkazov v hre:')
    for cmd in commands:
        print(f'* {cmd["name"]} - {cmd["description"]}')


def cmd_show_inventory(context: dict, param: str):
    if context['backpack']['items'] == []:
        print("Batoh je prázdny.")
    else:
        print("V batohu máš:")
        for item in context['backpack']['items']:
            print(f"   * {item['name']}")


def cmd_drop_item(context: dict, param: str):
    backpack = context['backpack']
    room = context['room']
    name = param

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš položiť.')
        return

    # search for item in backpack items
    item = get_item_by_name(name, backpack['items'])

    # item not found
    if item is None:
        print('Taký predmet pri sebe nemáš.')
        return

    # drop item
    backpack['items'].remove(item)
    room['items'].append(item)
    print(f'Do miestnosti si položil predmet {name}.')


def cmd_take_item(context: dict, name: str):
    backpack = context['backpack']
    room = context['room']

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš zobrať.')
        return

    # search for item in room items
    item = get_item_by_name(name, room['items'])

    # item not found
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # is the item movable?
    if MOVABLE not in item['features']:
        print('Tento predmet sa nedá vziať.')
        return

    # is backpack full?
    if len(backpack['items']) >= backpack['max']:
        print('Batoh je plný')
        return

    # take item
    room['items'].remove(item)
    backpack['items'].append(item)
    print(f'Do batohu si si vložil predmet {name}.')


def cmd_examine_item(context: dict, param: str):
    name = param

    # if the name was not entered
    if name == '':
        print('Neviem, čo chceš preskúmať.')
        return

    # search for item in room items
    item = get_item_by_name(name, context['room']['items'] + context['backpack']['items'])

    # item not found
    if item is None:
        print('Taký predmet tu nikde nevidím.')
        return

    # show item description
    print(item['description'])


def cmd_quit(context: dict, param: str):
    context['state'] = states.QUIT


def cmd_look_around(context: dict, param: str):
    show_room(context['room'])


commands = [
    {
        'name': 'o hre',
        'description': 'zobrazí informácie o hre',
        'aliases': ('about', 'info', '?'),
        'exec': cmd_about,
    },

    {
        'name': 'inventar',
        'description': 'zobrazí obsah batohu',
        'aliases': ("i", "inventory", 'batoh'),
        'exec': cmd_show_inventory,
    },

    {
        'name': 'koniec',
        'description': 'ukončí rozohratú hru',
        'aliases': ('quit', 'bye', 'q', 'exit',),
        'exec': cmd_quit,
    },

    {
        'name': 'prikazy',
        'description': 'zobrazí príkazy, ktoré sa dajú použiť v hre',
        'aliases': ('commands', 'help', 'pomoc',),
        'exec': cmd_commands,
    },

    {
        'name': "rozhliadni sa",
        'description': 'vypíše opis miestnosti, v ktorej sa hráč práve nachádza',
        'aliases': ("look around", "kukaj het"),
        'exec': cmd_look_around,
    },

    {
        'name': "poloz",
        'description': 'položí zvolený predmet v miestnosti',
        'aliases': ("drop",),
        'exec': cmd_drop_item,
    },

    {
        'name': "vezmi",
        'description': 'vezme predmet z miestnosti a vloží si ho do batohu',
        'aliases': ("take",),
        'exec': cmd_take_item,
    },

    {
        'name': "preskumaj",
        'description': 'zobrazí opis daného predmetu',
        'aliases': ("examine",),
        'exec': cmd_examine_item,
    },
]
