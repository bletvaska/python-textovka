from .features import MOVABLE
from .item import Item


class Map(Item):
    name = 'mapu'
    description = 'Je to mapa okolia tábora. [bold green]Oáza[/bold green] na sever od tábora je označená krížikom a ' \
                  'nič nehovoriacim slovom "HIER".'
    features = [MOVABLE]
