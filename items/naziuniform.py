from dataclasses import dataclass, field

from .features import MOVABLE, USABLE
from .item import Item


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = 'Zachovalá dôstojnícka uniforma.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context):
        # action
        self.name = 'nemecka uniforma (oblecena)'
        self.features.remove(USABLE)
        self.features.remove(MOVABLE)

        # render
        print('Obliekol si si uniformu... Padne ti ako uliata.')
