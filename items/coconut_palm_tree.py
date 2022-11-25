from dataclasses import dataclass, field

from helpers import get_current_room
from items.features import EXAMINABLE
from items.item import Item
from items.nazi_uniform import NaziUniform


@dataclass
class CoconutPalmTree(Item):
    name: str = 'kokosova palma'
    description: str = 'Zdá sa, že na jej plody nedosiahneš.'
    features: list = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # action
        room = get_current_room(context)
        room.items.append(NaziUniform())
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú uniformu.')
