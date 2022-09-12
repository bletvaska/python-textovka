from dataclasses import dataclass, field

from .features import MOVABLE, USABLE, EXAMINABLE
from .item import Item
from .key import Key


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = 'Zachovalá dôstojnícka uniforma.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE, EXAMINABLE])

    def use(self, context):
        # action
        self.name = 'nemecka uniforma (oblecena)'
        self.features.remove(USABLE)
        self.features.remove(MOVABLE)

        # render
        print('Obliekol si si uniformu... Padne ti ako uliata.')

    def examine(self, context):
        key = Key()
        context.current_room.items.append(key)

        print('V jednom jej vrecku si objavil kľúč!')
