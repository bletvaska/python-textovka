from dataclasses import dataclass, field

from items.features import MOVABLE
from items.item import Item


@dataclass
class Whip(Item):
    name: str = 'bič'
    description: str = 'Tvoj neoceniteľný pomocník..!'
    features: list = field(default_factory=lambda: [MOVABLE])
