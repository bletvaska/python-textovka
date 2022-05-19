from dataclasses import dataclass, field
from random import choice

from context import Context
from items.features import USABLE, MOVABLE
from items.item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Ešte teplé a farebné vydanie Bravíčka.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])
    headlines = [
        'Tenkrát poprvé: Moje prvé kroky s Pajtonom',
        'Ako som si doma vytetoval logo Pajtonu na pliecko',
        'Je Python single?',
        'Rubrika pre emancipovaných mužov: Pečieme s Viktorom',
        'Viktorove rady: Ako dobre vymastiť pekáč'
    ]

    def use(self, context: Context):
        print('Fúúúú... Nové Bravíčko... Pozrime sa čo píšu...')
        headline = choice(self.headlines)
        print(headline)
