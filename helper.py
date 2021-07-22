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
    if room['exits'] == []:
        print('Z tejto miestnosti neexistujú žiadne východy.')

    print()
