from dataclasses import dataclass, field

from .features import MOVABLE
from .item import Item


@dataclass
class Map(Item):
    name: str = 'mapa'
    description: str = ''
    features: list[int] = field(default_factory=lambda: [MOVABLE])
