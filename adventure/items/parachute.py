from rich import print

from helpers import get_room_by_name
from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]

    def use(self, context) -> bool:
        # 1. kontrola pouzitia
        if context.current_room.name != 'vo vzduchu':
            return False

        # 2. action
        context.current_room = get_room_by_name('púšť', context.world)
        self.features.remove(USABLE)

        # 3. render
        print('[bold green]Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...[/bold green]')
        context.current_room.show()
        return True
