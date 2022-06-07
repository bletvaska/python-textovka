from dataclasses import dataclass, field
from typing import List

import states
from commands.command import Command
from items.item import Item
from room import Room


@dataclass
class Context:
    current_room: Room
    world: List[Room]
    commands: List[Command] = field(default_factory=list)
    backpack: List[Item] = field(default_factory=list)
    game_state: str = states.PLAYING
