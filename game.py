#!/usr/bin/env python3

def get_item_by_name(items: list, name: list) -> dict:
    for item in items:
        if item['name'] == name:
            return item

    return None


def cmd_use(param: str, room: dict, backpack: dict, commands: list):
    name = param

    if name == '':
        print('Neviem čo chceš použiť.')

    else:
        item = get_item_by_name(room['items'] + backpack['items'], name)

        if item is None:
            print('Takýto predmet tu nikde nevidím.')
        elif 'usable' not in item['features']:
            print('Tento predmet sa nedá použiť.')
        else:
            print(f'Práve sa zamýšľaš, ako použiť predmet {name}.')


def cmd_drop(param: str, room: dict, backpack: dict, commands: list):
    name = param

    if name == '':
        print('Neviem, čo chceš položiť.')

    else:

        # find item item by name
        item = get_item_by_name(backpack['items'], name)

        # if nout found
        if item is None:
            print('Taký predmet tu nigde nevidím.')
            return

        # if found
        backpack['items'].remove(item)
        room['items'].append(item)
        print(f'Do miestnosti si položil predmet {name}.')

        # for item in backpack['items']:
        #     if item['name'] == name:
        #         backpack['items'].remove(item)
        #         room['items'].append(item)
        #         print(f'Do miestnosti si položil predmet {name}.')
        #         break

        # # if no such item was found
        # else:
        #     print('Taký predmet tu nigde nevidím.')


def cmd_take(param: str, room: dict, backpack: dict, commands: list):
    name = param

    if len(backpack['items']) >= backpack['capacity']:
        print('Batoh je plný.')

    elif name == '':
        print('Neviem, čo chceš zobrať.')

    else:
        for item in room['items']:
            if item['name'] == name:
                if 'movable' in item['features']:
                    backpack['items'].append(item)
                    room['items'].remove(item)
                    print(f'Predmet {name} si si vložil do batohu.')
                else:
                    print('Tento predmet sa nedá zobrať.')
                break

        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_explore(param: str, room: dict, backpack: dict, commands: list):
    name = param

    # if no name was given
    if name == '':
        print('Neviem, čo chceš preskúmať.')

    else:
        for item in room['items'] + backpack['items']:
            # if name was found
            if item['name'] == name:
                print(item['description'])

                # is item observable?
                if 'observable' in item['features']:
                    if item['name'] == 'chladnicka':
                        print('Zaprel si sa celou silou do dvier chladničky, '
                              'až si ich urval. Ale tá rukoväť by sa ti mohla '
                              'zísť.')
                        room['items'].append(
                            {
                                'name': 'rukovat',
                                'description': 'Kovová rukoväť značky Calex. Schopná fungovať aj ako páčidlo.',
                                'features': ['movable']
                            }
                        )
                        item['features'].remove('observable')
                break
        # if no such item was found
        else:
            print('Taký predmet tu nigde nevidím.')


def cmd_inventory(param: str, room: dict, backpack: dict, commands: list):
    if backpack['items'] == []:
        print('Batoh je prázdny.')
    else:
        print('V batohu máš:')
        for item in backpack['items']:
            print(f'\t{item["name"]}')


def cmd_commands(param: str, room: dict, backpack: dict, commands: list):
    print('Dostupné príkazy v hre:')

    for cmd in commands:
        print(f'\t{cmd["name"]} - {cmd["description"]}')

    print()


def cmd_about(param: str, room: dict, backpack: dict, commands: list):
    print('Hru spáchal  (c)2021 mirek')
    print('Ďalší príbeh Indiana Jonesa sa odohráva v temnej komôrke.')
    print()


def show_room(param: str = None, room: dict = None, backpack: dict = None, commands: list = None):
    """
    Prints room on the screen.

    Prints out the room given as the parameter of type dictionary on the screen.

    :params room: the room to show
    """
    if type(room) is not dict:
        raise TypeError('Room is not of type dictionary.')

    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room['description'])

    # print items in the room
    if room['items'] == []:
        print('Nevidíš tu nič zvláštne.')
    else:
        print('Vidíš: ')
        for item in room['items']:
            print(f'\t{item["name"]}')

    # print exits from the room
    if room['exits'] == []:
        print('Z tejto miestnosti neexistujú žiadne východy.')

    print()


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


if __name__ == '__main__':
    print(' ___           _ _                         _                       ')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ')
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print('|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/')

    print('                                                     (c) 2021 mirek')

    backpack = {
        'capacity': 2,
        'items': [
            {
                'name': 'noviny',
                'description': 'Nové tajmsy, husté čítanie na každý deň.',
                'features': ['movable']
            }
        ]
    }

    room = {
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

    commands = [
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
            'exec': show_room
        },

        {
            'name': 'koniec',
            'description': 'Ukončí rozohratú hru',
            'aliases': ['koniec', 'quit', 'end', 'q'],
            # 'exec': cmd_quit
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

    show_room(room=room)

    line = None

    # input parser
    while line != 'koniec':
        # read input from user and normalize it
        line = input('> ').rstrip().lstrip().lower()

        # test if line is empty
        if line == '':
            continue

        cmd = parse(line, commands)

        if cmd is None:
            print('Taký príkaz nepoznám.')
        else:
            cmd['exec'](cmd['param'], room, backpack, commands)

        # elif line in ('koniec', ''):
        #     continue
