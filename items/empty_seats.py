from game_context import GameContext
from .features import EXAMINABLE
from .item import Item
from .parachute import Parachute


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obvyklé letecké sedadlá.'
    features = [EXAMINABLE]

    def examine(self, context: GameContext):
        # crate parachute
        parachute = Parachute()

        # append parachute to current room
        context.current_room.items.append(parachute)

        # make item not examinable anymore
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
