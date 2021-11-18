from random import choice

from .features import MOVABLE, USABLE

headlines = [
    'Tenkrát poprvé: Moje prvé kroky s Pajtonom',
    'Ako som si doma vytetoval logo Pajtonu na pliecko',
    'Je Python single?',
    'Rubrika pre emancipovaných mužov: Pečieme s Viktorom',
    'Viktorove rady: Ako dobre vymastiť pekáč'
]


def _use(context: dict) -> None:
    print('Fúúúú... Nové Bravíčko... Pozrime sa čo píšu...')
    headline = choice(headlines)
    print(headline)


newspaper = {
    'name': 'noviny',
    'description': 'Najnovšie Bravíčko plné toho najfantastickejšieho obsahu pre Silviu.',
    'features': [MOVABLE, USABLE],
    'use': _use
}
