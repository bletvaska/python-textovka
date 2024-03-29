from rich import print

from .features import MOVABLE
from .item import Item


class Map(Item):
    name: str = 'mapu'
    description: str = 'Je to mapa okolia tábora. [bold green]Oáza[/bold green] na [bold yellow]sever[/bold yellow] od ' \
                  'tábora je označená krížikom a nič nehovoriacim slovom "HIER".'
    features: list[int] = [MOVABLE]
