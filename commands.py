from features import MOVABLE, USABLE
import states
from utils import get_item_by_name
from usages import use_canister, use_matches


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
    if item_name == 'kanister':
        use_canister(context, item)

    elif item_name == 'zapalky':
        use_matches(context, item)


    else:
        # print(f'Použil si predmet {item["name"]}')
        raise NotImplementedError(f'Usage of item "{item["name"]}" was not yet implemented')


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
