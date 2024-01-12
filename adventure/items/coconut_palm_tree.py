from rich import print

from .features import EXAMINABLE
from .item import Item
from .nazi_uniform import NaziUniform


class CoconutPalmTree(Item):
    name: str = 'kokosovu palmu'
    description: str = 'Zdá sa, že na jej plody nedosiahneš.'
    features: list[int] = [EXAMINABLE]

    def on_examine(self, context):
        # action
        context.current_room.items.append(NaziUniform())
        self.features.remove(EXAMINABLE)

        # render
        print('Pod koreňmi palmy si objavil ukrytú [bold magenta]uniformu[/bold magenta].')
