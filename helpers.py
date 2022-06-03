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
    print('Dobru chut.')


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
