from game_context import GameContext
from rooms import directions
from .features import MOVABLE, USABLE
from .item import Item


class Showel(Item):
    name = 'lopata'
    description = 'Je to zázrak, že ešte drží pohromade...'
    features = [MOVABLE, USABLE]

    def use(self, context: GameContext):
        # check usage conditions
        if context.current_room.name != 'oáza':
            print('nedobre')
            return False

        # use item
        context.current_room.exits[directions.DOWN] = 'podzemie'
        print('Pod vrstvou piesku si objavil vchod do podzemia!')
        self.features.remove(USABLE)

        return True
