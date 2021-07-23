def get_item_by_name(items: list, name: list) -> dict:
    for item in items:
        if item['name'] == name:
            return item

    return None


def show_room(room: dict):
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
    if list(room['exits'].values()).count(None) == 4:
        print('Z tejto miestnosti nevedú žiadne východy.')
    else:
        print('Východy z miestnosti:')
        exits = room['exits']
        for exit in exits:
            if exits[exit] is not None:
                if exit == 'north':
                    print('\tsever')
                elif exit == 'south':
                    print('\tjuh')
                elif exit == 'east':
                    print('\tvýchod')
                elif exit == 'west':
                    print('\tzápad')

    print()


def get_room_by_name(rooms: list, name: str) -> dict:
    for room in rooms:
        if room['name'] == name:
            return room
