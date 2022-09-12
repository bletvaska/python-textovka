from dataclasses import dataclass, field

from .features import MOVABLE
from .item import Item


@dataclass
class Dictionary(Item):
    name: str = 'slovnik'
    description: str = ''
    features: list[int] = field(default_factory=lambda: [MOVABLE])
