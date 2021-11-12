from typing import List


def get_item_by_name(name: str, items: List[dict]) -> dict:
    # check if name was given
    if not name:
        raise ValueError('Name is empty.')

    # search for item by name
    for item in items:
        if name == item['name']:
            return item

    # return None


def show_room(room: dict):
    """
    Show content of the room.
    The function shows name and description of the room. It also prints the list of items, which are in the room, or
    the information about there are no items in the room. Finally, it prints out also list of available exits from the
    room or special string, when there is no exit from the room.
    :param room: the room to print info about
    """
    # type checking
    if type(room) is not dict:
        raise TypeError('Room is not of type dictionary.')

    print(f'Nachádzaš sa v miestnosti {room["name"]}.')
    print(f'{room["description"]}')

    if room["exits"] == []:
        print("Z tejto miestnosti nevedú žiadne východy.")

    if room["items"] == []:
        print("Nevidíš tu nič zvláštne.")
    else:
        # print(f"Vidíš: {', '.join(room['items'])}")
        for item in room['items']:
            print(f"   * {item['name']}")

    # return None