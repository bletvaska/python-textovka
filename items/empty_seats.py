from dataclasses import dataclass, field

from helpers import get_current_room
from items.features import EXAMINABLE
from items.item import Item
from items.parachute import Parachute


@dataclass
class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obvyklé letecké sedadlá.'
    features: list = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # add parachute to current room
        room = get_current_room(context)
        room.items.append(Parachute())

        # remove EXAMINABLE from list of features
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
