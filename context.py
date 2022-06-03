from dataclasses import dataclass
from typing import List

from items.item import Item


@dataclass
class Context:
    commands: List[Item]
    backpack: List[Item]
    game_state: str
