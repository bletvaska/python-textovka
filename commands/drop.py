from dataclasses import dataclass

from context import Context
from helpers import get_item_by_name


@dataclass
class Drop:
    name: str = 'poloz'
    description: str = 'položí predmet z batohu do aktuálnej miestnosti'

    def exec(self, context: Context):
        # init
        name = self.param

        # if no item was entered...
        if len(name) == 0:  # name == ''
            print('Neviem, čo chceš položiť.')
            return

        # is the item in backpack?
        item = get_item_by_name(name, context.backpack)

        if item is None:
            print('Taký predmet pri sebe nemáš.')
            return

        # drop item
        # remove item from backpack
        context.backpack.remove(item)

        # add item to room items
        context.current_room.items.append(item)

        # render
        print(f'Do miestnosti si položil predmet {item.name}.')
