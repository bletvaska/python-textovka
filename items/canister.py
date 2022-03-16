from dataclasses import dataclass

from context import Context
from utils import get_item_by_name
from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = 'Vysokooktánový benzín tvorí obsah tohto kanistra. Kvalitka za rozumnú cenu.'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]

    def use(self, context: Context):
        # init
        room = context.room

        # 1. aktualizujem dvere:
        #    - description dvere su poliate benzinom
        door = get_item_by_name('dvere', room['items'])
        door.description = 'Masívne dubové dvere dôkladne nasiaknuté vysokooktánovým benzínom.'
        door.state = 'wet'

        # 2. aktualizujem kanister
        #    - description - prazdny kanister
        #    - features - nebude USABLE
        self.name = 'prazdny kanister'
        self.description = 'Prázdny kanister od benzínu.'
        self.features.remove(USABLE)

        # 3. render - vylejem kanister na dvere
        print('Odšroboval si zátku kanistra a celý jeho obsah si vylial na dvere. Veľmi dôkladne si ich pooblieval a '
              'v miestnosti sa rozľahla vôňa vysokooktánového benzínu. Srdce nejedného feťáka by v tejto chvíli '
              'zaplesalo Blahom.')
