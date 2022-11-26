from dataclasses import dataclass, field

from helpers import get_room_by_name
from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item


@dataclass
class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context) -> bool:
        # check usage conditions
        if context.current_room.name != 'voľný pád':
            return False

        # use item
        context.current_room = get_room_by_name('púšť', context.rooms)
        print('Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...')
        context.current_room.show()

        # remove usability
        self.features.remove(USABLE)

        return True
