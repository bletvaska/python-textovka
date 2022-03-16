from dataclasses import dataclass

from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Krabička so zápalkami.'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]



