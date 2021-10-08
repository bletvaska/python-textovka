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
            # is item movable?
            if MOVABLE in item['features']:
                # is backpack full?
                if len(backpack) >= 2:
                    print('Batoh je plný.')
                    return

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


def cmd_inventory(room: dict, line: str, backpack: list):
    if backpack == []:
        print('Batoh je prázdny.')
    else:
        print("V batohu máš:")
        for item in backpack:
            print(f'\t* {item["name"]}')


def cmd_explore(room: dict, item_name: str, backpack: list):
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


def cmd_look_around(room: dict, line: str, backpack: list):
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


def cmd_commands(room: dict, line: str, backpack: list):
    print('Dostupné príkazy v hre:')
    print('* inventar - zobrazí obsah hráčovho batoha')
    print('* koniec - ukončí hru')
    print('* o hre - zobrazí informácie o hre')
    print('* poloz - vyloží predmet z batohu do miestnosti')
    print('* prikazy - zobrazí zoznam dostupných príkazov v hre')
    print('* rozhliadni sa - zobrazí opis miestnosti, v ktorej sa hráč aktuálne nachádza')
    print('* vezmi - vezme predmet z miestnosti a vloží ho do batohu')


def cmd_about(room: dict, line: str, backpack: list):
    print('Indiana Jones a jeho Pythoňácke dobrodružstvo')
    print('Nestarnúci hrdina Indiana Jones sa tentokrát ocitol sám pustý v škaredej miestnosti. A jedine '
          'Pythoňácky programátori mu môžu zachrániť krk. Je to na tebe.')
    print('\n(c) 2021 hru spáchal mirek')


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
        'aliases': ('inventory','i'),
        'exec': cmd_inventory
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
