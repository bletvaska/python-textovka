from helpers import get_room_by_name
from items.features import MOVABLE, USABLE
from items.item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Obyčajný padák. Made in U.S.A. 1933'
    features = [MOVABLE, USABLE]

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
