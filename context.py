from dataclasses import dataclass, field

import states
from items.item import Item
from room import Room


@dataclass
class Context:
    current_room: Room
    backpack: list[Item] = field(default_factory=list)
    game_state: str = states.PLAYING
