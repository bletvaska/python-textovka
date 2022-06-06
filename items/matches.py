from dataclasses import dataclass, field
from typing import List

from context import Context
from helpers import get_item_by_name
from items.door import SOAKED, BURNING
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Krabička bezpečnostných zápaliek značky BILLA.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # arrange
        # v batohu/miestnosti sa nachadzaju dvere poliate benzinom
        door = get_item_by_name('dvere', context.backpack)
        if door is None or door.state != SOAKED:
            print('Zahrkal si krabickou od zapaliek, aby si sa uistil, ze v nej nieco je. '
                  'A fakt - su v nej tri zapalky.')
            return

        # act
        # aktualizujeme zapalky - po pouziti
        self.description = 'prázdna krabička bezpečnostných zápaliek značky BILLA.'
        self.features.remove(USABLE)

        # aktualizujeme dvere - po zapaleni
        door.description = 'Masivne veľké dubové horiace dvere.'
        door.name = 'horiace dvere'
        door.state = BURNING

        # render
        print('Skrtol si zapalkou a dvere okamzite zachvatili plamene. Obrovske teplo ta donutilo urobit krok vzad, cim'
              'sa ti naskytol vyrazne lepsi pohlad na celu tuto milu horiacu scenu.')
