from dataclasses import dataclass, field

from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Čerstvé vydanie Denníka N.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self):
        print('Ta zalistoval som si v denníku a čítam, že:')
        print('V gigantických katakombách bojovali partizáni proti nacistom, teraz chránia Odesu pred Rusmi (reportáž '
              'z podzemia)')
