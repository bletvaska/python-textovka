from dataclasses import dataclass

from commands.command import Command
from helpers import get_item_by_name
from items.features import USABLE


@dataclass
class Use(Command):
    name: str = 'pouzi'
    description: str = 'použije zvolený predmet'

    def exec(self, context, line):
        name = line.split('pouzi')[1].lstrip()

        # check if there is something to examine
        if name == '':
            print('Neviem, čo chceš použiť.')
        else:
            # check if item is in backpack
            item = get_item_by_name(name, context.backpack)
            if item is None:
                print('Taký predmet tu nikde nevidím.')
            else:
                if USABLE in item.features:
                    item.use()
                else:
                    print(f'Tento predmet sa nedá použiť.')
