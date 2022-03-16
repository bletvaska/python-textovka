from dataclasses import dataclass

from .item import Item


@dataclass
class Door(Item):
    name: str = 'dvere'
    description: str = 'Masívne dubové dvere. Zamknuté.'
    state: int = None
