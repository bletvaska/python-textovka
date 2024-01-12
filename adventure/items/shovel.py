from rich import print

from rooms import directions
from .features import MOVABLE, USABLE
from .item import Item


class Shovel(Item):
    name: str = 'lopatu'
    description: str = 'Je to zázrak, že ešte drží pohromade...'
    features: list[int] = [MOVABLE, USABLE]

    def on_use(self, context):
        # check usage conditions
        if context.current_room.name != 'oáza':
            return False

        # shovel usage
        context.current_room.exits[directions.DOWN] = 'podzemie'

        # post-processing
        self.features.remove(USABLE)
        context.score += 5

        # render
        print('Pod vrstvou piesku si objavil vchod do [bold green]podzemia[/bold green]!')

        return True
