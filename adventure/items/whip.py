from .features import MOVABLE, USABLE
from .item import Item


class Whip(Item):
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný pomocník..!'
    features: list[int] = [MOVABLE, USABLE]
