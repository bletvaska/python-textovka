from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = ''
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        return False
