from rich import print

from .features import MOVABLE, USABLE, EXAMINABLE
from .item import Item
from .key import Key


class NaziUniform(Item):
    name = 'nemecku uniformu'
    description = 'Zachovalá dôstojnícka uniforma.'
    features = [MOVABLE, USABLE, EXAMINABLE]
    is_dressed = False

    def on_examine(self, context):
        # action
        context.current_room.items.append(Key())
        self.features.remove(EXAMINABLE)

        # render
        print('V jednom jej vrecku si objavil [bold magenta]kľúč[/bold magenta]!')

    def on_use(self, context):
        # action
        self.is_dressed = True

        # render
        print('Obliekol si si [bold magenta]uniformu[/bold magenta]... Padne ti ako uliata.')

        return True

    def on_drop(self, context):
        self.is_dressed = False

    def __str__(self):
        if self.is_dressed is True:
            return f'{self.name} (oblečená)'
        else:
            return self.name
