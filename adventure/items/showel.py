import states
from .features import MOVABLE, USABLE
from .item import Item


class Showel(Item):
    name = 'lopata'
    description = 'Je to zázrak, že ešte drží pohromade...'
    features = [MOVABLE, USABLE]

    def use(self, context) -> bool:
        # check
        if context.current_room.name != 'oáza':
            return False

        # action
        self.features.remove(USABLE)
        context.game_state = states.GAME_SOLVED

        # render
        print('Pod vrstvou piesku si objavil vchod do podzemia!')
        return True

