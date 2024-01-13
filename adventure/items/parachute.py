from rich import print

from adventure.helpers import get_room_by_name
from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]

    def on_use(self, context) -> bool:
        # check usage conditions
        if context.current_room.name != 'voľný pád':
            return False

        # use item
        context.current_room = get_room_by_name('púšť', context)
        print('Nad hlavou sa ti roztvoril [bold magenta]padák[/bold magenta] a po chvíli si šťastne pristál...')
        context.current_room.show()

        # remove usability
        self.features.remove(USABLE)

        return True
