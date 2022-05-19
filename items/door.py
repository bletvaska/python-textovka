from dataclasses import dataclass, field

from items.item import Item


@dataclass
class Door(Item):
    name: str = 'dvere'
    description: str = 'Veľké dubové dvere. Zamknuté.'
    features: list[int] = field(default_factory=list)
