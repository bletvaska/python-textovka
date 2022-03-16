def get_item_by_name(name: str, items: list) -> dict:
    for item in items:
        if item['name'] == name:
            return item

    # return None


def get_room_by_name(name: str, world: list) -> dict:
    for room in world:
        if room['name'] == name:
            return room

    # return None


def show_room(room: dict):
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
