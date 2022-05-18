from items import Item


def get_item_by_name(name: str, items: list[Item]) -> Item | None:
# def get_item_by_name(name, items):
    """
    Returns the item found in list of items by it's name.
    :param name: name of the item to find
    :param items: list of items
    :return: item, if found, None otherwise
    """
    for item in items:
        if name == item.name:
            return item

    return None  # default behaviour
