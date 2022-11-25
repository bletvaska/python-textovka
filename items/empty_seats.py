from dataclasses import dataclass, field

from items.features import EXAMINABLE
from items.item import Item


@dataclass
class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obvyklé letecké sedadlá.'
    features: list = field(default_factory=lambda: [EXAMINABLE])
