from game_context import GameContext
from items.features import EXAMINABLE
from items.item import Item
from items.parachute import Parachute


class EmptySeats(Item):
    name: str = 'prazdne sedadla'
    description: str = 'Obyčajné letecké sedadlá.'
    features: list[int] = [EXAMINABLE]

    def examine(self, context: GameContext) -> None:
        # vloz do aktualnej miestnosti predmet padak
        context.current_room.items.append(Parachute())

        # odstranime vlastnost preskumatelnost zo sedadiel
        self.features.remove(EXAMINABLE)

        # vyrenderuj
        print('Pod jedným z nich si našiel padák. Šťastná to náhoda.')
