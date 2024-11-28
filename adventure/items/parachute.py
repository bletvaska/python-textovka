from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]
