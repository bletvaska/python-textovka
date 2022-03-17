from dataclasses import dataclass, field
from typing import List

import states
from room import Room


@dataclass
class Context:
    backpack: dict
    room: Room
    world: dict
    commands: list
    state: int = states.PLAYING
    history: List[str] = field(default_factory=list)
