def get_item_by_name(name: str, items: dict):
    for item in items:
        if name == item["name"]:
            return item

    # return None


def show_room(room: dict):
    """
    Shows the room description

    This function shows the room description, which contains the room name,
    room description, items in room and list of exists.
    :param room: the room to show description about
    """

    # type check for room
    if type(room) is not dict:
        raise TypeError(
            f'Inapropriate type for room. Expected dict, but "{type(room)}" was given.'
        )

    print(f"Nachádzaš sa v miestnosti {room['name']}")
    print(room["description"])

    # show exits
    if len(room["exits"]) == 0:
        print("Z tejto miestnosti nevedú žiadne východy.")

    # show items
    if len(room["items"]) == 0:
        print("Nenachadzaju sa tu ziadne predmety")
    else:
        print("Vidíš: ")
        for item in room["items"]:
            print(f"   {item['name']}")

    # return None


def banner():
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print("|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/")
    print("             Indiana Jones and his Great Escape")
    print()