from dataclasses import dataclass, field

from .features import MOVABLE
from .item import Item


@dataclass
class Whip(Item):
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný pomocník..!'
    features: list[int] = field(default_factory=lambda: [MOVABLE])
