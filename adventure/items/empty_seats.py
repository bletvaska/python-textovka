from .features import EXPLORABLE
from .item import Item


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obvyklé letecké sedadlá.'
    features = [EXPLORABLE]
