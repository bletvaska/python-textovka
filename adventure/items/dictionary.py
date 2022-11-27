from .features import MOVABLE
from .item import Item


class Dictionary(Item):
    name = 'slovnik'
    description = 'Je to anglicko-staroegyptský slovník, 14. upravené vydanie.'
    features = [MOVABLE]
