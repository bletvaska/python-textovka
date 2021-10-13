from features import MOVABLE, USABLE
import states


def cmd_take(context: dict, arg: str):
    item_name = arg
    room = context['room']
    backpack = context['backpack']['items']

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
                if len(backpack) >= context['backpack']['capacity']:
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

    # if item not in room items
    for item in room['items'] + backpack:
        if item['name'] == item_name:
            print(item['description'])
            return

    # if no such item available
    print('Taký predmet tu nikde nevidím.')


def cmd_drop(context: dict, arg: str):
    item_name = arg
    backpack = context['backpack']['items']
    room = context['room']

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

    # if item available?
    # canister = get_item_by_name('kanister', room['items'] + backpack)
    # if canister is None:
    # else:

    for item in backpack + room['items']:
        if item['name'] == item_name:
            # is item usable?
            if USABLE in item['features']:
                if item_name == 'kanister':
                    # 1. aktualizujem dvere:
                    #    - description dvere su poliate benzinom
                    # get_item_by_name(name, list)

                    # door = get_item_by_name('dvere', room['items'])
                    for i in room['items']:
                        if i['name'] == 'dvere':
                            i['description'] = 'Masívne dubové dvere dôkladne nasiaknuté vysokooktánovým benzínom.'
                            break

                    # 2. aktualizujem kanister
                    #    - description - prazdny kanister
                    #    - features - nebude USABLE
                    canister = item
                    canister['name'] = 'prazdny kanister'
                    canister['description'] = 'Prázdny kanister od benzínu.'
                    canister['features'].remove(USABLE)

                    # 3. render - vylejem kanister na dvere
                    print('Odšroboval si zátku kanistra a celý jeho obsah si vylial na dvere. Veľmi dôkladne si ich pooblieval a v miestnosti sa rozľahla vôňa vysokooktánového benzínu. Srdce nejedného feťáka by v tejto chvíli zaplesalo Blahom.')
                else:
                    print(f'Použil si predmet {item["name"]}')
            else:
                print('Tento predmet sa nedá použiť')
            return

    # if no such item available
    print('Taký predmet tu nikde nevidím.')


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
