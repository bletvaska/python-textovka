from items.item import Item
from rooms.room import Room


def intro():
    """
    Shows the game intro banner.
    """
    print(' ___           _ _                         _                       ')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___ ')
    print(" | || '_ \ / _` | |/ _` | '_ \ / _` |  _  | |/ _ \| '_ \ / _ \/ __|")
    print(" | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\__ \\")
    print('|___|_| |_|\__,_|_|\__,_|_| |_|\__,_|  \___/ \___/|_| |_|\___||___/')
    print("        Indiana Jones and his Greatest Python Adventure")
    print()

    # return None


def outro():
    """
    Shows the game outro banner.
    """
    print('---')
    print('Tento remake v rámci školenia Python 101 vytvoril')
    print('(c)2023 by mire(c) z koši(c)')
    print()

    # return None


def get_item_by_name(name: str, items: list[Item]) -> Item:
    for item in items:
        if item.name == name:
            return item

    # return None


def get_room_by_name(name: str, rooms: list[Room]) -> Room:
    return rooms[0]
