from .features import MOVABLE, USABLE
from .item import Item


class Whip(Item):
    name = 'bic'
    description = 'tvoj neoceniteľný pomocník...!'
    features = [MOVABLE, USABLE]
