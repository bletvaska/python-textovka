from dataclasses import dataclass, field

from context import Context
from helpers import get_item_by_name
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = 'Veľký 25l kanister. Po odšróbovaní vrchnáka si zistil, že je to benzín. Kvalitka. 98 oktánov.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # check if door is in the room
        door = get_item_by_name('dvere', context.current_room)
        if door is None:
            print(
                'Vzal si kanister do ruky, trošku si zaposiloval a uľavil si si sprostým slovom. Hneď sa cítiš lepšie.')
            return
