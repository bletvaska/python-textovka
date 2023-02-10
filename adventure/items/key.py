from rich import print

from helpers import get_item_by_type
from .diamond import Diamond
from .dictionary import Dictionary
from .features import MOVABLE, USABLE
from .heavy_chest import HeavyChest
from .item import Item
from .map import Map


class Key(Item):
    name = 'kluc'
    description = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features = [MOVABLE, USABLE]

    def on_use(self, context):
        # check usage conditions
        chest = get_item_by_type(HeavyChest, context.current_room.items)
        if chest is None:
            return False

        # use item
        context.current_room.items.extend([
            Map(),
            Dictionary(),
            Diamond(),
        ])

        # post-processing
        self.features.remove(USABLE)
        context.score += 5

        # render
        print('Otvoril si [bold magenta]truhlu[/bold magenta] a našiel si v nej zaujímavé veci!')

        return True
