from dataclasses import dataclass, field

from items.item import Item

NORMAL = 0
SOAKED = 1
BURNING = 2


@dataclass
class Door(Item):
    name: str = 'dvere'
    description: str = 'Veľké dubové dvere. Zamknuté.'
    state = NORMAL

