from rich import print

from .features import MOVABLE, USABLE, EXAMINABLE
from .item import Item
from .key import Key


class NaziUniform(Item):
    name = 'nemecka uniforma'
    description = 'Zachovalá dôstojnícka uniforma.'
    features = [MOVABLE, USABLE, EXAMINABLE]

    def on_examine(self, context):
        # action
        context.current_room.items.append(Key())
        self.features.remove(EXAMINABLE)

        # render
        print('V jednom jej vrecku si objavil [bold yellow]kľúč[/bold yellow]!')

    def on_use(self, context):
        # action
        self.name = 'nemecka uniforma (oblecena)'

        # render
        print('Obliekol si si [bold yellow]uniformu[/bold yellow]... Padne ti ako uliata.')

        return True

    def on_drop(self, context):
        self.name = 'nemecka uniforma'
