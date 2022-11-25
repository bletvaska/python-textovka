from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Key(Item):
    name: str = 'kluc'
    description: str = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        return False
