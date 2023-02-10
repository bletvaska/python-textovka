from helpers import get_item_by_name
from .features import MOVABLE, USABLE
from .item import Item


class Dictionary(Item):
    name = 'slovnik'
    description = 'Je to anglicko-staroegyptský slovník, 14. upravené vydanie.'
    features = [MOVABLE, USABLE]

    def on_use(self, context):
        # check if there is writing on wall in the room
        item = get_item_by_name('napis na stene', context.current_room.items)
        if item is None:
            return False

        print('"Prístup k pokladom veľkého faraóna bude mať ten, kto zhromaždí pri oltári všetkých päť magických '
              'diamantov."')

        return True
