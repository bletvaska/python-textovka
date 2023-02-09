from .features import MOVABLE, USABLE
from .item import Item


class Parachute(Item):
    name = 'padak'
    description = 'Obyčajný padák MADE IN U.S.A. 1933'
    features = [MOVABLE, USABLE]

    def use(self, context):
        print('pouzivam padak')
