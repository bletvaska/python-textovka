from context import Context
from .features import EXPLORABLE
from .item import Item
from .parachute import Parachute


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obvyklé letecké sedadlá.'
    features = [EXPLORABLE]

    def explore(self, context: Context):
        context.current_room.items.append(Parachute())
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
