from context import Context
from .features import EXPLORABLE, MOVABLE
from .item import Item


class NaziUniform(Item):
    name = 'nemecka uniforma'
    description = 'Zachovalá dôstojnícka uniforma.'
    features = [EXPLORABLE, MOVABLE]

    def explore(self, context: Context):
        context.current_room.items.append(Key())
        self.features.remove(EXPLORABLE)
        print('V jednom z jej vreciek si objavil kľúč!')
