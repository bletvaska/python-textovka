from dataclasses import dataclass, field

from items.features import MOVABLE, USABLE, EXAMINABLE
from items.item import Item
from items.key import Key


@dataclass
class NaziUniform(Item):
    name: str = 'nemecka uniforma'
    description: str = 'Zachovalá dôstojnícka uniforma.'
    features: list = field(default_factory=lambda: [MOVABLE, USABLE, EXAMINABLE])

    def examine(self, context):
        # action
        context.current_room.items.append(Key())
        self.features.remove(EXAMINABLE)

        # render
        print('V jednom jej vrecku si objavil kľúč!')

    def use(self, context):
        # action
        self.name = 'nemecka uniforma (oblecena)'

        # render
        print('Obliekol si si uniformu... Padne ti ako uliata.')

        return True
