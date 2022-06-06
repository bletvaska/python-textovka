from dataclasses import dataclass, field
from typing import List

from context import Context
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # arrange
        # 1. v batohu/miestnosti sa nachadzaju horiace dvere. ak tam nie su, tak napiseme:
        #
        # Sklonil si sa nad vedro s vodou a chlipol si si. Poprevaloval si si vodu v ustach a vyplul si ju naspat. Na neskor.
        #
        #
        # # act
        # 1. aktualizujeme vedro
        #     opis - Prázdne vedro.
        #     vedro uz bude nepouzitelne
        #
        # 2. aktualizujeme dvere
        #     odstranime dvere z hry (batohu/miestnosti)
        #
        # # render
        #
        # Rozohnal si sa a cely obsah vedra si vylial na horiace dvere. Tie sa pod tarchou vody a vdaka plamenom rozpadli na marne kusky. Plamene sa ti podarilo tymto odvaznym tahom uplne zahasit.

        print('>> pouzitie vedra')
