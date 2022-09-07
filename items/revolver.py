from dataclasses import dataclass, field

from .features import MOVABLE, USABLE
from .item import Item


@dataclass
class Revolver(Item):
    name: str = 'revolver'
    description: str = 'Sedemkomorový revolver značky Smith&Wesson.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self):
        print('Ta vytasil si, zamachroval si a vystrelil si do vzduchu. Ano. Si chlap.')
