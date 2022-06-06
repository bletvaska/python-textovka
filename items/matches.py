from dataclasses import dataclass, field
from typing import List

from context import Context
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Krabička bezpečnostných zápaliek značky BILLA.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        print('>> pouzitie zapaliek')
