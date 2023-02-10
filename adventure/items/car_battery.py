from .features import MOVABLE
from .item import Item


class CarBattery(Item):
    name = 'automobilova bateria'
    description = 'Ešte je trochu nabitá.'
    features = [MOVABLE]
