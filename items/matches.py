from dataclasses import dataclass

from context import Context
from utils import get_item_by_name
from .features import USABLE, MOVABLE
from .item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Krabička so zápalkami.'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]

    def use(self, context: Context):
        # init
        room = context.room
        backpack = context.backpack['items']

        # 1. overim, ci su dvere poliate benzinom
        #    - ci su dvere v stave 'wet'
        door = get_item_by_name('dvere', room['items'])
        if door.state != 'wet':
            print('Zahrkal si krabičkou pri ušku, aby si sa uistil, že nie je prázdna. Usmial si sa.')
            return

        # 2. aktualizujem zapalky
        #    - odstranim ich z hry
        if self in room['items']:
            room['items'].remove(self)
        else:
            backpack.remove(self)

        # 3. aktualizujem dvere
        #    - zmenim description - dvere v plamenoch
        #    - zmenim stav na 'on fire'
        door.description = 'Dvere v plameňoch.'
        door.state = 'on fire'
        door.name = 'horiace dvere'

        # 4. renderujem scenu - skrtol si zapalkou a dvere zacali horiet
        print('Otvoril si krabičku a vytiahol si z nej jedinú zápalku. Nadýchol si sa a škrtol si. Miestnosť sa '
              'okamžite rozžiarila. Síce nie tvojim šarmantným úsmevom, ale plamenňom, ktorý oakmžite zachvátil dvere '
              'nasiaknuté vysokooktánovým benzínom. Nejedno srdce pyromana by teraz vzplanulo radosťou.')
