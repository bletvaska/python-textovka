from .features import MOVABLE
from .item import Item


class CarBattery(Item):
    name: str = 'automobilovu bateriu'
    description: str = 'Ešte je trochu nabitá.'
    features: list[int] = [MOVABLE]
