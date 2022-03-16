from dataclasses import dataclass
from typing import List

import states
from commands import Command


@dataclass
class Context:
    backpack: dict
    room: dict
    world: dict
    history: List[str]
    commands: List[Command]
    state: int = states.PLAYING
