from items.features import EXAMINABLE
from items.item import Item


class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obyčajné letecké sedadlá.'
    features: list[int] = [EXAMINABLE]
