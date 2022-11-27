from .features import USABLE, MOVABLE
from .item import Item


class CarBattery(Item):
    name = 'automobilova bateria'
    description = 'Ešte je trochu nabitá.'
    features = [MOVABLE]
