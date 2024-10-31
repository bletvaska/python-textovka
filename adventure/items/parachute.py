from helpers import get_room_by_name
from items.features import MOVABLE, USABLE
from items.item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]

    def use(self, context) -> bool:
        # overit, ci sa predmet da pouzit
        if context.current_room.name != 'vo vzduchu':
            return False

        # pouzitie predmetu
        context.current_room = get_room_by_name('púšť', context.world)
        print('Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...')
        print()
        context.current_room.show()
        return True
