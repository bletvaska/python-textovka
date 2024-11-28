from rich import print

from .features import EXAMINABLE
from .item import Item
from .parachute import Parachute


class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obyčajné letecké sedadlá.'
    features: list[int] = [EXAMINABLE]

    def examine(self, context):
        # 1. v miestnosti poloz padak
        context.current_room.items.append(Parachute())

        # 2. odstran vlastnost EXAMINABLE zo zoznamu vlastnosti
        self.features.remove(EXAMINABLE)

        # 3. render
        print('Pod jedným z nich si našiel [bold magenta]padák[/bold magenta]. Šťastná to náhoda.')
