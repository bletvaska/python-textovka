from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Made in USA 1939'
    features = [MOVABLE, USABLE]
