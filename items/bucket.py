from dataclasses import dataclass, field
from typing import List

from context import Context
from helpers import get_item_by_name
from items.door import BURNING
from items.features import MOVABLE, USABLE
from items.item import Item
from states import WINNER


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody.'
    features: List[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # arrange
        # v batohu/miestnosti sa nachadzaju dvere poliate benzinom
        door = get_item_by_name('horiace dvere', context.current_room.items)
        if door is None or door.state != BURNING:  # door.name != 'horiace dvere':
            print('Sklonil si sa nad vedro s vodou a chlipol si si. Poprevaloval si si vodu v ustach'
                  ' a vyplul si ju naspat. Na neskor.')
            return

        # act
        # aktualizujeme vedro - po pouziti
        self.description = 'Prázdne vedro.'
        self.features.remove(USABLE)

        # aktualizujeme dvere - odstranime z hry
        context.current_room.items.remove(door)

        # aktualizujem stav hry
        context.game_state = WINNER

        # render
        print('Rozohnal si sa a cely obsah vedra si vylial na horiace dvere. Tie sa pod tarchou vody a vdaka '
              'plamenon rozpadli na marne kusky. Plamene sa ti podarilo tymto odvaznym tahom uplne zahasit.')
