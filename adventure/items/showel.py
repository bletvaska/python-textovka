from rooms import directions
from .features import MOVABLE, USABLE
from .item import Item


class Showel(Item):
    name = 'lopata'
    description = 'Je to zázrak, že ešte drží pohromade...'
    features = [MOVABLE, USABLE]

    def use(self, context):
        # check usage conditions
        if context.current_room.name != 'oáza':
            print('nedobre')
            return False

        # use item
        context.current_room.exits[directions.DOWN] = 'podzemie'
        print('Pod vrstvou piesku si objavil vchod do podzemia!')
        self.features.remove(USABLE)

        return True
