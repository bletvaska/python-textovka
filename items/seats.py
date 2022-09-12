from dataclasses import dataclass, field

from .features import EXAMINABLE
from .item import Item
from .parachute import Parachute


@dataclass
class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obvyklé letecké sedadlá.'
    features: list[str] = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # action
        parachute = Parachute()
        context.current_room.items.append(parachute)
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel padák! (šťastná to náhoda...)')
