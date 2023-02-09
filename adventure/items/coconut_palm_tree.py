from context import Context
from .features import EXPLORABLE
from .item import Item
from .nazi_uniform import NaziUniform


class CoconutPalmTree(Item):
    name = 'kokosova palma'
    description = 'Zdá sa, že na jej plody nedosiahneš.'
    features = [EXPLORABLE]

    def explore(self, context: Context):
        # act/explore
        context.current_room.items.append(NaziUniform())
        self.features.remove(EXPLORABLE)

        # render
        print('Pod koreňmi palmy si objavil schovanú uniformu!')
