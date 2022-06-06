from dataclasses import field, dataclass
from typing import List

from context import Context
from helpers import get_item_by_name
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = '10L kanister plny vysokooktanoveho kvalitneho benzinu z ruskej ropy'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # arrange
        # ak sa dvere v batohu/miestnosti nenachadzaju, tak vypiseme:
        door = get_item_by_name('dvere', context.backpack)
        if door is None:
            print('Odsroboval si vrchnak na kanistri a nasal si vonu kvalitneho vysokooktanoveho benzinu.')
            return

        # act
        # oblejem dvere - aktualizujeme opis dveri
        #
        # Masivne veľké dubové dvere plne nasiaknuté vysokooktánovým benzínom.
        #
        #
        # kanister bude prazdny - aktualizujeme opis kanistru
        #
        # Prázdny 10L kanister.
        #
        #
        # kanister bude nepouzitelny - odstranime vlastnost USABLE
        #
        #
        # # renderd
        #
        # Odsroboval si vrchnák na kanistri a celý jeho vysokooktánový obsah si vylial na masívne dubové dvere. Ani kvapka nevyšla nazmar.
