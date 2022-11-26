from dataclasses import dataclass, field

from items.features import EXAMINABLE
from items.item import Item
from items.parachute import Parachute


@dataclass
class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obyčajné letecké sedadlá.'
    features: list = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # add parachute to current room
        context.current_room.items.append(Parachute())

        # remove EXAMINABLE from list of features
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
