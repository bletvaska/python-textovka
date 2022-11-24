from dataclasses import dataclass, field

from rooms.room import Room
from states import STATE_PLAYING


@dataclass
class GameContext:
    current_room: str
    rooms: list[Room] = field(default_factory=list)
    backpack: list[str] = field(default_factory=list)
    commands: list = field(default_factory=list)
    game_state: str = STATE_PLAYING
