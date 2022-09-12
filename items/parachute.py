from dataclasses import dataclass, field

import world
from helpers import get_room_by_name
from .features import MOVABLE, USABLE
from .item import Item


@dataclass
class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák MADE IN U.S.A. 1933'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        # check conditions
        if context.current_room.name != 'vo vzduchu':
            print('Podľa teba som zrejme blbec, ale skutočne nechápem, k čomu by ti to v súčasnej dobe bolo dobré.')
            return

        # action
        room = get_room_by_name('miesto pristatia', world.rooms)
        context.current_room = room
        self.features.remove(USABLE)

        # render
        print('Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...')
        # room.show()
