from dataclasses import dataclass

from context import Context
from utils import get_item_by_name
from .features import MOVABLE, USABLE
from .item import Item


@dataclass
class Bucket(Item):
    name: str = 'vedro'
    description: str = 'Vedro plné vody.'

    def __post_init__(self):
        self.features += [MOVABLE, USABLE]

    def use(self, context: Context):
        # init
        room = context.room
        door = get_item_by_name('horiace dvere', room.items)

        # scenario
        # 1. overim, ci su dvere v stave 'on fire'
        if door is None or door.state != 'on fire':
            print('Si sa sklonil, otvoril papuľku a celú si si ju naplnil vodou z vedra. Uľavilo sa ti.')
            return

        # 2. aktualizujeme vedro
        #    - je prazdne
        #    - nebude pouzitelne
        self.name = 'prazdne vedro'
        self.description = 'Prázdne vedro.'
        self.features.remove(USABLE)

        # 3. zmazem dvere z miestnosti/hry
        room.items.remove(door)

        # 4. nastavim pred z miestnosti na vychod do garden
        room.exits['east'] = 'garden'

        # 5. rendering - ta si uhasil dvere a sa rozpadli
        print('Teplo v miestnosti narastalo a ty si sa nestíhal chladiť chlípaním vody z vedra. Osvietila ťa ale '
              'spásna myšlienka a obsah vedra si vyvrátil smerom na dvere v plameňoch. Vody bolo dostatok na to, '
              'aby sa plameň uhasil, ale bolo jej dosť na to, aby sa horiace dvere pod jej tlakom rozpadli. Horenisko '
              'halí hustá hmla.')
