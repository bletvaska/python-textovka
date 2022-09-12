from dataclasses import dataclass, field

from .features import MOVABLE
from .item import Item


@dataclass
class Diamond(Item):
    name: str = 'diamant'
    description: str = ''
    features: list[int] = field(default_factory=lambda: [MOVABLE])
