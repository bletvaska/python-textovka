from items.features import MOVABLE, USABLE
from items.item import Item


class Whip(Item):
    name = 'bic'
    description = 'Tvoj neoceniteľný pomocník..!'
    features = [MOVABLE, USABLE]

    def use(self, context):
        return False
