from dataclasses import dataclass, field

from .features import EXAMINABLE
from .item import Item


@dataclass
class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obvyklé letecké sedadlá.'
    features: list[str] = field(default_factory=lambda: [EXAMINABLE])
