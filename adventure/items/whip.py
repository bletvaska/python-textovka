from .features import MOVABLE
from .item import Item


class Whip(Item):
    name = 'bic'
    description = 'Tvoj neoceniteľný pomocník!'
    features = [MOVABLE]
