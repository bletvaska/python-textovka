from dataclasses import dataclass, field

from context import Context
from helpers import get_item_by_name
from items.door import SOAKED, BURNING
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Matches(Item):
    name: str = 'zapalky'
    description: str = 'Štandardné zápalky. Tri.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # 1. preconditions
        # som v miestnosti s dverami?
        door = get_item_by_name('dvere', context.current_room.items)
        if door is None:
            print('zahrkal si zapalkami pri usku a presvedcil si sa, ze v nej naozaj nieco je.')
            return

        # su dvere su poliate benzinom?
        if door.state != SOAKED:
            print('Hmm... To mi nejako nevychádza. Si istý, že tie drevené dvere len tak podpáliš jednou zápalkou?')
            return

        # 2. action
        # dvere zacnu horiet

        # - aktualizujeme popis aj nazov dveri
        door.name = 'horiace dvere'
        door.description = 'Veľké dubové masívne horiace dvere.'
        door.state = BURNING

        # zapalky uz nebudu pouzitelne
        # - odstranime USABLE zo zapaliek
        self.features.remove(USABLE)
        # - aktualizujeme opis (prazdna krabicka)
        self.description = 'Prázdna krabička bezpečnostných zápaliek značky Billa.'

        # 3. render
        print('Skrtol si zapalkou a dvere okamzite zblkli. Ak si si doteraz myslel, ze ti tu bola zima a este aj sero, '
              'tak uz to tak nie je. Je tu prijemne teplucko.')
