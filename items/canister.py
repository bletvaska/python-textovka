from dataclasses import dataclass, field

from context import Context
from helpers import get_item_by_name
from items.door import SOAKED
from items.features import MOVABLE, USABLE
from items.item import Item


@dataclass
class Canister(Item):
    name: str = 'kanister'
    description: str = 'Veľký 25l kanister. Po odšróbovaní vrchnáka si zistil, že je to benzín. Kvalitka. 98 oktánov.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # check if door is in the room
        door = get_item_by_name('dvere', context.current_room.items)
        if door is None:
            print('Vzal si kanister do ruky, trošku si zaposiloval a uľavil si si sprostým slovom. '
                  'Hneď sa cítiš lepšie.')
            return

        # action

        # make door soaked
        door.description = 'Veľké masívne dubové dvere. Len tak niečo a niekto s nimi nepohne, keď sú zamknuté. A to ' \
                           'teda sú. A ešte k tomu aj parádne nasiaknuté vysokooktánovým benzínom.'
        door.state = SOAKED

        # update canister
        self.description = 'Veľký 25L kanister. Odšroboval si veko a nadýchol si sa. Ešte pred chvíľou tu bol ' \
                           'určite vysokooktánový benzín. Ale teraz tu už nie je nič.'
        self.features.remove(USABLE)

        # render
        print('Odšroboval si vrchnák z kanistra, rozohnal si sa a celý jeho vysokooktánový obsah si vylial '
              'na dubové dvere.')
