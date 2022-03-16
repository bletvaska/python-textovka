from dataclasses import dataclass
from typing import List

import states
from room import Room


@dataclass
class Context:
    backpack: dict
    room: Room
    world: dict
    history: List[str]
    commands: List
    state: int = states.PLAYING
