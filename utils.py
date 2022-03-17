from typing import List

from items.item import Item
from room import Room


def get_item_by_name(name: str, items: List[Item]) -> Item | None:
    for item in items:
        if item.name == name:
            return item

    # return None


def get_room_by_name(name: str, world: List[Room]) -> Room | None:
    for room in world:
        if room.name == name:
            return room

    # return None
