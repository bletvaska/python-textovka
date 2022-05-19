from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Štandardné zápalky. Tri.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])
