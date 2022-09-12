from dataclasses import dataclass, field

from .features import MOVABLE
from .item import Item


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = 'Zachovalá dôstojnícka uniforma.'
    features: list[int] = field(default_factory=lambda: [MOVABLE])
