# from items import Item
from room import Room


def get_item_by_name(name: str, items: list) -> object:
    for item in items:
        if item.name == name:
            return item

    # return None


def get_room_by_name(name: str, world: list) -> Room:
    for room in world:
        if room.name == name:
            return room

    # return None
