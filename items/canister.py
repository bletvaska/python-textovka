from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = 'Veľký 25l kanister. Po odšróbovaní vrchnáka si zistil, že je to benzín. Kvalitka. 98 oktánov.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])
