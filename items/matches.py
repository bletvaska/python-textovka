from dataclasses import dataclass

from .item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Krabička so zápalkami.'
