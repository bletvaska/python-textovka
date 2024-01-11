from items.features import USABLE, MOVABLE
from items.item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]
