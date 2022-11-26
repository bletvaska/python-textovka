from items.features import EXAMINABLE
from items.item import Item
from items.nazi_uniform import NaziUniform


class CoconutPalmTree(Item):
    name = 'kokosova palma'
    description = 'Zdá sa, že na jej plody nedosiahneš.'
    features = [EXAMINABLE]

    def examine(self, context):
        # action
        context.current_room.items.append(NaziUniform())
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú uniformu.')
