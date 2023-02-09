from context import Context
from helpers import get_room_by_name
from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Obyčajný padák MADE IN U.S.A. 1933'
    features = [MOVABLE, USABLE]

    def use(self, context: Context) -> bool:
        # check usability
        # is indy in room free fall?
        if context.current_room.name != 'voľný pád':
            return False

        # act
        # move to the room desert
        context.current_room = get_room_by_name('púšť', context.world)
        self.features.remove(USABLE)

        # render
        print('Nad hlavou sa ti otvoril padák a po chvíli šťastne pristál...')
        context.current_room.show()

        return True
