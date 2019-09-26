class About:

    def __init__(self):
        self._name = 'o hre'
        self._description = 'Túto hru spáchal mirek v roku 2019. Celkom fajnú.'

    def exec(self):
        print(self._description)




def show_room(room: dict):
    # show description
    print(room['description'])

    # show exits
    if len(room['exits']) > 0:
        print('Možné východy:')
        for exit in room['exits']:
            print(f"    {exit}")
    else:
        print('Z miestnosti nevedú žiadne východy.')

    # show items
    if len(room['items']) > 0:
        print('Vidíš:')
        for item in room['items']:
            print(f'     {item["name"]}')
    else:
        print('Nevidíš nič zvláštne.')


def show_inventory(backpack: list):
    if len(backpack) > 0:
        print('V batohu máš:')
        for item in backpack:
            print(f'     {item["name"]}')
    else:
        print('Batoh je prázdny.')


def help():
    print('ta pomoz si sam.')


def commands():
    cmds = (
        'rozhliadni sa',
        'o hre',
        'pomoc',
        'prikazy',
        'sever',
        'juh',
        'vychod',
        'zapad',
        'dolu',
        'vezmi',
        'poloz',
        'preskumaj',
        'koniec'
    )
    print('\n'.join(cmds))


def quit():
    print('ta diky ze si si zahral tuto mocnu hru, lebo je fakt mocna.')


def east(world: dict, current_room: str):
    """
    Enter the room on east from current room.
    If there is no exit to the east, then no change. The new room will be returned from the function.
    :param world: the world the player is in
    :param current_room: the name of current room player is in
    :return: the name of new room on the east
    """
    room = world[current_room]

    if 'vychod' in room['exits']:
        current_room = room['exits']['vychod']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def west(world: dict, current_room: str):
    room = world[current_room]

    if 'zapad' in room['exits']:
        current_room = room['exits']['zapad']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def north(world: dict, current_room: str):
    room = world[current_room]

    if 'sever' in room['exits']:
        current_room = room['exits']['sever']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def south(world: dict, current_room: str):
    room = world[current_room]

    if 'juh' in room['exits']:
        current_room = room['exits']['juh']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def down(world: dict, current_room: str):
    room = world[current_room]

    if 'dolu' in room['exits']:
        current_room = room['exits']['dolu']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def drop_item(world: dict, current_room: str, backpack: list, name: str):
    room = world[current_room]
    for item in backpack:
        if item['name'] == name:
            room['items'].append(item)
            backpack.remove(item)
            print(f'{item["name"]} si vyložil z batohu.')
            break
    else:
        print('Taký predmet u seba nemáš.')


def take_item(world: dict, current_room: str, backpack: list, name: str):
    room = world[current_room]
    for item in room['items']:
        if item['name'] == name:
            if 'movable' not in item['features']:
                print('Tento predmet sa nedá vziať.')
            elif len(backpack) >= 1:
                print('Batoh je plný.')
            else:
                backpack.append(item)
                room['items'].remove(item)
                print(f'{item["name"]} si vložil do batohu.')

            break  # return
    else:
        print('Taký predmet tu nikde nevidím.')


def examine_item(world: dict, current_room: str, backpack: list, name: str):
    room = world[current_room]
    items = room['items'] + backpack

    for item in items:
        if item['name'] == name:
            print(item['description'])
            return

    print('Taký predmet tu nikde nevidím.')


def use_whip(world: dict, current_room: str, backpack: list):
    if current_room != 'nad priepastou':
        print('Svihol si bičíkom vo vzduchu. Ale švihá, pomyslel si si. Ako za mladých čias.')
        return

    room = world[current_room]
    # pridanie prechodu z miestnosti na vychod
    room['exits']['vychod'] = 'chram'

    # vyhodenie bica z miestnosti alebo z batohu
    for item in backpack:
        if item['name'] == 'bic':
            backpack.remove(item)
            break
    else:
        for item in room['items']:
            if item['name'] == 'bic':
                room['items'].remove(item)
                break

    print(
        'Rozohnal si sa, vzduchom to zasvišťalo a tvoj bič sa zachytil o visiaci konár v hornej časti jaskyne. Prehupnúť sa na druhú stranu už nebude žiadny problém.')


def use_item(world: dict, current_room: str, backpack: list, name: str):
    room = world[current_room]
    items = room['items'] + backpack

    for item in items:
        if item['name'] == name:
            if 'usable' not in item['features']:
                print('Tento predmet sa nedá použiť')
                return

            if name == 'bic':
                use_whip(world, current_room, backpack)
                return

    print('Taký predmet tu nikde nevidím.')
