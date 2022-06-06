from dataclasses import dataclass, field
from typing import List

from context import Context
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Krabička bezpečnostných zápaliek značky BILLA.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # arrange
        # 1. v batohu/miestnosti sa nachadzaju dvere poliate benzinom. a ak nie, tak napiseme:
        #
        #     Zahrkal si krabickou od zapaliek, aby si sa uistil, ze v nej nieco je. A fakt - su v nej tri zapalky.
        #
        # # act
        # 2. aktualizujeme zapalky
        #     odstranime USABLE zo zoznamu ficur
        #     aktualizujeme opis: Prázdna krabička bezpečnostných zápaliek značky BILLA.
        #
        # 3. aktualizujeme dvere
        #     aktualizujeme opis: Masivne veľké dubové horiace dvere.
        #     aktualizujeme nazov: horiace dvere
        #
        # # render
        # 4. vypiseme na obrazovku
        #
        # Skrtol si zapalkou a dvere okamzite zachvatili plamene. Obrovske teplo ta donutilo urobit krok vzad, cim sa ti naskytol vyrazne lepsi pohlad na celu tuto milu horiacu scenu.

        print('>> pouzitie zapaliek')
