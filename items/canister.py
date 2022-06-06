from dataclasses import field, dataclass
from typing import List

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = '10L kanister plny vysokooktanoveho kvalitneho benzinu z ruskej ropy'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self):
        print('>> pouzitia kanistra.')
