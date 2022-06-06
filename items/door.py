from dataclasses import dataclass

from items.item import Item

NORMAL = 1
SOAKED = 2
BURNING = 3


@dataclass
class Door(Item):
    name: str = 'dvere'
    description: str = 'Masivne veľké dubové dvere.'
    state: int = NORMAL
