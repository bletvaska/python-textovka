import random
from dataclasses import dataclass, field
from typing import List

from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Posledné vydanie Bravíčka. To najlepšie čítanie pre každého chovateľa Pytóna.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self):
        print('Aaaa Bravíčko. Zalistoval si čerstvým vydaním tohto legendárneho časopisu každého správneho Pytonistu '
              'a píšu...')

        headlines = (
            'Python 3.11 bude vydany v piatok 13.',
            'Spravny Pythonista pouziva len Python >= 3.7',
            'import this'
        )

        print(random.choice(headlines))
