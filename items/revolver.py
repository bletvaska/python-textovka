from dataclasses import dataclass, field
from typing import List

from items.features import MOVABLE
from items.item import Item


@dataclass
class Revolver(Item):
    name: str = 'revolver'
    description: str = 'Štandardný revolver značky Smis-end-Weson'
    features: List[int] = field(default_factory=lambda: [MOVABLE])
