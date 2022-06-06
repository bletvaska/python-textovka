from typing import List

from items.item import Item


def intro():
    """
    The game intro banner.
    """
    print(' ___           _ _                         _')
    print('|_ _|_ __   __| (_) __ _ _ __   __ _      | | ___  _ __   ___  ___')
    print(" | || '_ \\ / _` | |/ _` | '_ \\ / _` |  _  | |/ _ \\| '_ \\ / _ \\/ __|")
    print(' | || | | | (_| | | (_| | | | | (_| | | |_| | (_) | | | |  __/\\__ \\')
    print('|___|_| |_|\\__,_|_|\\__,_|_| |_|\\__,_|  \\___/ \\___/|_| |_|\\___||___/')

    print('                         and his Great Escape')


def outro():
    """
    The game outro banner.
    """
    print()
    print('(c)2022 by mire(c) z kosi(c)')


def congratulations():
    print("  ____                            _         _       _   _                 _")
    print(" / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |")
    print("| |   / _ \\| '_ \\ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \\| '_ \\/ __| |")
    print("| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \\__ \\_|")
    print("\\____\\___/|_| |_|\\__, |_|  \\__,_|\\__|\\__,_|_|\\__,_|\\__|_|\\___/|_| |_|___(_)")
    print("                  |___/                                                    ")

    print()
    print("Úspešne si ukončil túto parádnu hru napísanú v jazyku Python. Indiana Jones by bol na teba určite hrdý.")
    print()


def get_item_by_name(name: str, items: List[Item]) -> Item | None:
    """
    Returns the item from the list by its name.

    This function returns the item object, which is located in the list given by
    items parameter. If the item is found, then it is returned. If it is not found,
    None is returned.
    :param name: the name of the item to find
    :param items: list of items
    :return: item, if found or None otherwise
    """
    for item in items:
        if name == item.name:
            return item

    # return None
