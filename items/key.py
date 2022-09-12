from dataclasses import dataclass, field

from items.features import USABLE, MOVABLE
from items.item import Item


@dataclass
class Key(Item):
    name: str = 'kluc'
    description: str = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        print('pouzivam klucik')