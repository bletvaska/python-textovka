from dataclasses import dataclass

from helpers import get_item_by_name
from items.features import USABLE
from .command import Command


@dataclass
class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context):
        if self.parameter == '':
            print('Neviem čo chceš použiť.')
        else:
            item = get_item_by_name(self.parameter, context.backpack + context.current_room.items)

            if item is None:
                print('Taký predmet tu nikde nevidím.')
            else:
                if USABLE not in item.features:
                    print('Tento predmet sa nedá použiť.')
                else:
                    item.use(context)
