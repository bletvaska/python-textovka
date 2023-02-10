from rich import print

from .features import EXAMINABLE
from .item import Item
from .nazi_uniform import NaziUniform


class CoconutPalmTree(Item):
    name = 'kokosova palma'
    description = 'Zdá sa, že na jej plody nedosiahneš.'
    features = [EXAMINABLE]

    def on_examine(self, context):
        # action
        context.current_room.items.append(NaziUniform())
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú [yellow]uniformu[/yellow].')
