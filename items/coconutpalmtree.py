from dataclasses import dataclass, field

from .features import EXAMINABLE
from .item import Item


@dataclass
class CoconutPalmTree(Item):
    name: str = 'kokosova palma'
    description: str = 'Zdá sa, že na jej plody nedosiahneš.'
    features: list[str] = field(default_factory=lambda: [EXAMINABLE])

    def examine(self, context):
        # action

        # render
        print('Pod koreňmi palmy si objavil ukrytú uniformu.')
