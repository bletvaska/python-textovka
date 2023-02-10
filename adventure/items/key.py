from helpers import get_item_by_name
from .diamond import Diamond
from .dictionary import Dictionary
from .features import MOVABLE, USABLE
from .item import Item
from .map import Map


class Key(Item):
    name = 'kluc'
    description = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features = [MOVABLE, USABLE]

    def on_use(self, context):
        # check usage conditions
        chest = get_item_by_name('tazka okovana truhlica', context.current_room.items)
        if chest is None:
            return False

        # use item
        context.current_room.items.extend([
            Map(),
            Dictionary(),
            Diamond(),
        ])
        print('Otvoril si truhlu a našiel si v nej zaujímavé veci!')

        # remove usability
        self.features.remove(USABLE)
        return True
