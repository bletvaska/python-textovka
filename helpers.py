def intro():
    """
    Shows the intro screen of the game.
    """
    print(" ___           _ _                         _                       ")
    print("|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ")
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\")
    print("|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/")
    print('          Indiana Jones and his Great U-boat Escape')
    print()

    # return None


def outro():
    """
    Shows the outro screen of the game.
    """
    print()
    print("Ďakujem, že si si zahral túto špica hru. Stav sa aj nabudúce.")
    print('(c)2022 by mirek')

    # return None


def get_item_by_name(name, items):
    for item in items:
        if item.name == name:
            return item

    # return None


def get_room_by_name(name, rooms):
    for room in rooms:
        if room.name == name:
            return room

    # return None
