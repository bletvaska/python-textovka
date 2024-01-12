from items.features import MOVABLE, USABLE
from items.item import Item


class Whip(Item):
    name: str = 'bic'
    description: str = 'Tvoj neoceniteľný pomocník...!'
    features: list[int] = [MOVABLE, USABLE]

    def use(self, context) -> bool:
        return False
