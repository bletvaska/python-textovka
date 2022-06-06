from dataclasses import dataclass

from commands.command import Command
from context import Context
from helpers import get_item_by_name
from items.features import USABLE


@dataclass
class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context: Context, name: str):
        # check if there is something to examine
        if name == '':
            print('Neviem, čo chceš použiť.')
        else:
            # check if item is in backpack
            item = get_item_by_name(name, context.backpack + context.current_room.items)
            if item is None:
                print('Taký predmet tu nikde nevidím.')
            else:
                if USABLE in item.features:
                    item.use(context)
                else:
                    print(f'Tento predmet sa nedá použiť.')
