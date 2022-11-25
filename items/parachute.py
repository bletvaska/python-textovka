from dataclasses import dataclass, field

from helpers import get_current_room
from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item


@dataclass
class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context) -> bool:
        # check usage conditions
        room = get_current_room(context)
        if room.name != 'vo vzduchu':
            return False

        # use item
        context.current_room = 'púšť'
        print('Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...')
        room = get_current_room(context)
        room.show(context)

        # remove usability
        self.features.remove(USABLE)

        return True
