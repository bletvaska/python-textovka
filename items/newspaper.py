import random
from dataclasses import dataclass, field

from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Newspaper(Item):
    name: str = 'noviny'
    description: str = 'Čerstvé vydanie Denníka N.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])
    headlines: list[str] = field(default_factory=lambda: [
        'V gigantických katakombách bojovali partizáni proti nacistom, teraz chránia Odesu pred Rusmi (reportáž z podzemia)',
        'Iveta Radičová: Premiér Heger mal konať (+ video)',
        'Rus, ktorý zaskočil slovenských konšpirátorov: Nečakal som, že je u vás Putin taký obľúbený',
        'Košická nemocnica uplatňuje pri výbere primárov zvláštne pravidlá, vďaka nim uspel Paškov známy',
        'Týždeň v zdraví: Viete, že fajčenie vážne škodí aj srdcu? Je všetka vegánska strava naozaj zdravá? Prečo nás po plači bolí hlava?'
    ])

    def use(self):
        print('Ta zalistoval som si v denníku a čítam, že:')
        headline = random.choice(self.headlines)
        print(headline)
