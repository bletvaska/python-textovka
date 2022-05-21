from dataclasses import dataclass, field

from context import Context
from helpers import get_item_by_name
from items.features import USABLE, MOVABLE
from items.item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody. Ťažko povedať, či aj pitnej.'
    features: list[int] = field(default_factory=lambda: [MOVABLE, USABLE])

    def use(self, context: Context):
        # 1. preconditions
        # som v miestnosti s dverami?
        # horia dvere?
        door = get_item_by_name('horiace dvere', context.current_room.items)
        if door is None:
            print('Nabral si si vodu do dlaní, chlipol si si, poprevaľoval si si vodu v papuľke a vypľul si ju naspäť. '
                  'Na neskôr.')
            return

        # 2. action
        # aktualizujem vedro
        # - nebude USABLE
        self.features.remove(USABLE)
        # - aktualizujem opis (prazdne vedro)
        self.description = 'Prázdne vedro'
        # aktualizujem dvere
        # - odstranim dvere z hry (zmazem ich z room['items']
        context.current_room.items.remove(door)
        # otvorim prechod do novej miestnosti
        # - na zapad -> garden
        # FIXME
        # context.current_room.exits['west'] = 'záhradka'

        # 3. render
        print('Masaker. ta si zahasil poziar a sa dvere rozpadli.')
