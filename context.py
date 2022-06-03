from dataclasses import dataclass, field
from typing import List

import states
from commands.command import Command
from items.item import Item


@dataclass
class Context:
    commands: List[Command]
    backpack: List[Item] = field(default_factory=lambda: [])
    game_state: str = states.PLAYING
