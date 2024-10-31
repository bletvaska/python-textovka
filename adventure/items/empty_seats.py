from rich import print
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_context import GameContext

from .features import EXAMINABLE
from .item import Item
from .parachute import Parachute


class EmptySeats(Item):
    name: str = "prazdne sedadla"
    description: str = "Obyčajné letecké sedadlá."
    features: list[int] = [EXAMINABLE]

    def examine(self, context: 'GameContext'):
        # 1. vlozis do miestnosti predmet padak
        context.current_room.items.append(Parachute())

        # 2. odstranis vlasnost EXAMINABLE zo zoznamu vlastnosti
        self.features.remove(EXAMINABLE)

        # render
        print('Pod jedným z nich si našiel [bold magenta]padák[/bold magenta]. Šťastná to náhoda.')
