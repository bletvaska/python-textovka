from dataclasses import dataclass, field

from context import Context
from items.features import USABLE, MOVABLE
from items.item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Ešte teplé vydanie Denníka N.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        print('citam noviny')
