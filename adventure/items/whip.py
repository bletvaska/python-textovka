from rich import print

from helpers import get_item_by_type
from .diamond import Diamond
from .diamond_on_ceiling import DiamondOnCeiling
from .features import MOVABLE, USABLE
from .item import Item


class Whip(Item):
    name = 'bic'
    description = 'Tvoj neoceniteľný pomocník..!'
    features = [MOVABLE, USABLE]

    def on_use(self, context):
        # check usage conditions
        diamond_on_ceiling = get_item_by_type(DiamondOnCeiling, context.current_room.items)
        if diamond_on_ceiling is None:
            return False

        # use item
        context.current_room.items.remove(diamond_on_ceiling)
        context.current_room.items.append(Diamond())

        # post-processing
        self.features.remove(USABLE)
        context.score += 5

        # render
        print('Podarilo sa ti zraziť [bold magenta]diamant[/bold magenta] dolu!')

        return True
