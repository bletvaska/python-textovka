from .features import MOVABLE
from .item import Item


class Map(Item):
    name = 'mapa'
    description = 'Je to mapa okolia tábora. Oáza na sever od tábora je označená krížikom a nič nehovoriacim slovom ' \
                  '"HIER". '
    features = [MOVABLE]
