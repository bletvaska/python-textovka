from adventure.helpers import get_item_by_type
from .features import MOVABLE, USABLE
from .item import Item
from .writing_on_wall import WritingOnWall


class Dictionary(Item):
    name: str = 'slovnik'
    description: str = 'Je to anglicko-staroegyptský slovník, 14. upravené vydanie.'
    features: list[int] = [MOVABLE, USABLE]

    def on_use(self, context):
        # check if there is writing on wall in the room
        item = get_item_by_type(WritingOnWall, context.current_room.items)
        if item is None:
            return False

        print('"Prístup k pokladom veľkého faraóna bude mať ten, kto zhromaždí pri oltári všetkých päť magických '
              'diamantov."')

        return True
