from dataclasses import dataclass, field

import states
from helpers import get_item_by_name
from .diamond import Diamond
from .dictionary import Dictionary
from .features import USABLE, MOVABLE
from .item import Item
from .map import Map


@dataclass
class Key(Item):
    name: str = 'kluc'
    description: str = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        # check
        chest = get_item_by_name('tazka okovana truhlica', context.current_room.items)
        if chest is None:
            print('Nie je tu čo odomknúť.')
            return

        # action
        context.current_room.items.append(Map())
        context.current_room.items.append(Diamond())
        context.current_room.items.append(Dictionary())
        self.features.remove(USABLE)

        # render
        print('Otvoril si truhlu a našiel si v nej zaujímavé veci!')
