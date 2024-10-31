from items.features import MOVABLE, USABLE
from items.item import Item


class Parachute(Item):
    name: str = 'padak'
    description: str = 'Obyčajný padák. Made in U.S.A. 1933'
    features: list[int] = [MOVABLE, USABLE]

    def use(self, context) -> bool:
        print('Nad hlavou sa ti roztvoril padák a po chvíli si šťastne pristál...')
        return True
