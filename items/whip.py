from dataclasses import dataclass, field
from typing import List

from items.features import MOVABLE
from items.item import Item


@dataclass
class Whip(Item):
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný kamarát na každom jednom dobrodužstve.'
    features: List[int] = field(default_factory=lambda: [MOVABLE])
