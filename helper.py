def get_item_by_name(name: str, items: list):
    for item in items:
        if name == item.name:
            return item

    # return None


def show_room(room: dict) -> None:
    """
    Shows the content of the room

    This function shows the content of the room: it's name, description, exits and items, which are located in the room.
    @param room: the room to show
    """
    if not isinstance(room, dict):
        # if type(room) != dict:
        raise TypeError('Room is not of type dictionary.')

    print(f'Nachádzaš sa v miestnosti {room["name"]}')
    print(room["description"])

    # show exits
    translation = {
        'north': 'sever',
        'south': 'juh',
        'east': 'východ',
        'west': 'západ'
    }

    # check if there is any exit
    some_exit = False
    for ex in room['exits']:
        if room['exits'][ex] is not None:
            some_exit = True
            break

    if some_exit is False:
        print('Z miestnosti nevedú žiadne východy.')
    else:
        print('Možné východy z miestnosti:')
        for exit in room['exits']:
            if room['exits'][exit] is not None:
                print(f' * {translation[exit]}')

    # print items
    if len(room['items']) == 0:
        print('Nevidíš tu nič zvláštne.')
    else:
        print('Vidíš:')
        for item in room['items']:
            print(f' * {item.name}')

        # print('Vidíš:', ', '.join(room['items']))

    # return None
