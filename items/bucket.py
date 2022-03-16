from dataclasses import dataclass

from .features import MOVABLE, USABLE
from .item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody.'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]