from items.features import EXAMINABLE
from items.item import Item


class EmptySeats(Item):
    name = "prazdne sedadla"
    description = "Obyčajné letecké sedadlá."
    features: list[int] = [EXAMINABLE]
