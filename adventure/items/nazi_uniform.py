from context import Context
from .features import EXPLORABLE, MOVABLE, USABLE
from .item import Item
from .key import Key


class NaziUniform(Item):
    name = 'nemecka uniforma'
    description = 'Zachovalá dôstojnícka uniforma.'
    features = [EXPLORABLE, MOVABLE, USABLE]

    def explore(self, context: Context):
        context.current_room.items.append(Key())
        self.features.remove(EXPLORABLE)
        print('V jednom z jej vreciek si objavil kľúč!')

    def use(self, context):
        # action
        self.name = 'nemecka uniforma (oblecena)'

        # render
        print('Obliekol si si uniformu... Padne ti ako uliata.')

        return True
