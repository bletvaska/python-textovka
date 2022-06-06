from dataclasses import dataclass, field
from typing import List

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self):
        print('>> pouzitie vedra')
       