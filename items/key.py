from items.features import MOVABLE, USABLE
from items.item import Item


class Key(Item):
    name = 'kluc'
    description = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features = [MOVABLE, USABLE]

    def use(self, context):
        return False
