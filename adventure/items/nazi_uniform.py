from .features import MOVABLE, USABLE, EXAMINABLE
from .item import Item
from .key import Key


class NaziUniform(Item):
    name = 'nemecka uniforma'
    description = 'Zachovalá dôstojnícka uniforma.'
    features = [MOVABLE, USABLE, EXAMINABLE]

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
