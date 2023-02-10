from .features import MOVABLE, USABLE
from .item import Item


class Showel(Item):
    name = 'lopata'
    description = 'Je to zázrak, že ešte drží pohromade...'
    features = [MOVABLE, USABLE]

    def use(self, context) -> bool:
        return False

