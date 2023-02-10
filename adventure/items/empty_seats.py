from rich import print

from .features import EXAMINABLE
from .item import Item
from .parachute import Parachute


class EmptySeats(Item):
    name = 'prazdne sedadla'
    description = 'Obyčajné letecké sedadlá.'
    features = [EXAMINABLE]

    def on_examine(self, context):
        # add parachute to current room
        context.current_room.items.append(Parachute())

        # remove EXAMINABLE from list of features
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel [bold yellow]padák[/bold yellow]. Šťastná to náhoda.')
