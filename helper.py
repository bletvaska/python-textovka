def find_item(name: str, items: list) -> dict:
    for item in items:
        if item['name'] == name:
            return item

    return None


def get_room_by_name(name: str, world: list) -> dict:
    for room in world:
        if room['name'] == name:
            return room

    return None
