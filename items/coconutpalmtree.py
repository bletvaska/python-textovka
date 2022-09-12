from dataclasses import dataclass, field

from .features import EXAMINABLE
from .item import Item
from .naziuniform import NaziUniform


@dataclass
class CoconutPalmTree(Item):
    name: str = 'kokosova palma'
    description: str = 'Zdá sa, že na jej plody nedosiahneš.'
    features: list[int] = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # action
        uniform = NaziUniform()
        context.current_room.items.append(uniform)
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú uniformu.')
