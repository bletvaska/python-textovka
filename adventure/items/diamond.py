from .features import MOVABLE
from .item import Item


class Diamond(Item):
    name = 'diamant'
    description = 'Ťažký, neforemný drahý kameň.'
    features = [MOVABLE]
