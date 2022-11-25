from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = 'Zachovalá dôstojnícka uniforma.'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE, EXAMINABLE])

    def examine(self, context):
        # action

        self.features.remove(EXAMINABLE)

        # render
        print('V jednom jej vrecku si objavil kľúč!')

    def use(self, context):
        return False
