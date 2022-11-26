from dataclasses import dataclass, field

from items.item import Item
from rooms.room import Room
from states import STATE_PLAYING


@dataclass
class GameContext:
    current_room: Room = None
    rooms: list[Room] = field(default_factory=list)
    backpack: list[Item] = field(default_factory=list)
    commands: list = field(default_factory=list)
    game_state: str = STATE_PLAYING
