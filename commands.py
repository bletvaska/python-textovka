def show_room(room):
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


def show_inventory(backpack):
    if len(backpack) > 0:
        print('V batohu máš:')
        for item in backpack:
            print(f'     {item["name"]}')
    else:
        print('Batoh je prázdny.')


def about():
    print(
        'Ta tuto mocnu hru o Indianovi Jonesovi spachal uz nie az taky mlady fajny programator mirek v roku 2019. A ak ho chces podporit, ta mozes nejake fsimne poslat na ucet s IBANom SK1234567890987654321')


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


def east(world, current_room):
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


def west(world, current_room):
    room = world[current_room]

    if 'zapad' in room['exits']:
        current_room = room['exits']['zapad']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def north(world, current_room):
    room = world[current_room]

    if 'sever' in room['exits']:
        current_room = room['exits']['sever']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def south(world, current_room):
    room = world[current_room]

    if 'juh' in room['exits']:
        current_room = room['exits']['juh']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def down(world, current_room):
    room = world[current_room]

    if 'dolu' in room['exits']:
        current_room = room['exits']['dolu']
        show_room(world[current_room])
    else:
        print('tam sa neda ist')

    return current_room


def drop_item(world, current_room, backpack, name):
    room = world[current_room]
    for item in backpack:
        if item['name'] == name:
            room['items'].append(item)
            backpack.remove(item)
            print(f'{item["name"]} si vyložil z batohu.')
            break
    else:
        print('Taký predmet u seba nemáš.')


def take_item(world, current_room, backpack, name):
    room = world[current_room]
    for item in room['items']:
        if item['name'] == name:
            if len(backpack) >= 1:
                print('Batoh je plný.')
            else:
                backpack.append(item)
                room['items'].remove(item)
                print(f'{item["name"]} si vložil do batohu.')

            break  # return
    else:
        print('Taký predmet tu nikde nevidím.')


def examine_item(world, current_room, backpack, name):
    room = world[current_room]
    items = room['items'] + backpack

    for item in items:
        if item['name'] == name:
            print(item['description'])
            return

    print('Taký predmet tu nikde nevidím.')
