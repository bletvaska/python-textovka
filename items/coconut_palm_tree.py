from dataclasses import dataclass, field

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
        context.current_room.items.append(NaziUniform())
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú uniformu.')
