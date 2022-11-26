from items.features import EXAMINABLE
from items.item import Item
from items.parachute import Parachute


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obyčajné letecké sedadlá.'
    features = [EXAMINABLE]

    def examine(self, context):
        # add parachute to current room
        context.current_room.items.append(Parachute())

        # remove EXAMINABLE from list of features
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
