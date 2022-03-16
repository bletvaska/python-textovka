from dataclasses import dataclass
from typing import List

import states


@dataclass
class Context:
    backpack: dict
    room: dict
    world: dict
    history: List[str]
    commands: List
    state: int = states.PLAYING
