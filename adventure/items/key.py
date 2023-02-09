from .features import MOVABLE
from .item import Item


class Key(Item):
    name = 'kluc'
    description = 'Veľký mosadzný kľúč, zrejme od nejakej truhly.'
    features = [MOVABLE]
