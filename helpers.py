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
