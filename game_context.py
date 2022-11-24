from dataclasses import dataclass, field

import world
from room import Room
from states import STATE_PLAYING


@dataclass
class GameContext:
    current_room: str = 'v lietadle'
    rooms: list[Room] = world.rooms
    backpack: list[str] = field(default_factory=list)
    commands: list = field(default_factory=list)
    game_state: str = STATE_PLAYING
