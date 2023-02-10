from .features import MOVABLE
from .item import Item


class CarBattery(Item):
    name = 'automobilovu bateriu'
    description = 'Ešte je trochu nabitá.'
    features = [MOVABLE]
