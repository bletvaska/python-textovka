from .features import EXAMINABLE
from .item import Item


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obvyklé letecké sedadlá.'
    features = [EXAMINABLE]
