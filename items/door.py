from dataclasses import dataclass

from items.item import Item


@dataclass
class Door(Item):
    name: str = 'dvere'
    description: str = 'Masivne veľké dubové dvere.'
