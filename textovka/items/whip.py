from .features import MOVABLE, USABLE
from .item import Item


class Whip(Item):
    name = 'bic'
    description = 'Tvoj neoceniteľný pomocník...!'
    features = [MOVABLE]
