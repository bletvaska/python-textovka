from dataclasses import dataclass

from item import Item


@dataclass
class Whip(Item):
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný pomocník..!'
    # features: list = [MOVABLE, USABLE]
